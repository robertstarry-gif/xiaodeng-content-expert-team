#!/usr/bin/env python3
"""Fetch an optional context pack from a private writing-library API.

The helper has no third-party dependencies and fails soft: if the URL is not
configured or the request fails, it prints an unavailable pack so the skill can
continue with local rules.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch a writing context pack.")
    parser.add_argument("--request", help="Path to a JSON request file.")
    parser.add_argument("--domain", default="")
    parser.add_argument("--topic", default="")
    parser.add_argument("--platform", default="")
    parser.add_argument("--audience", default="")
    parser.add_argument("--risk-level", default="low")
    parser.add_argument("--voice", default="")
    parser.add_argument("--language", default="zh-CN")
    parser.add_argument(
        "--need",
        action="append",
        dest="needs",
        default=[],
        help="Need to request. Can be repeated.",
    )
    parser.add_argument("--output", choices=["json", "markdown"], default="markdown")
    return parser.parse_args()


def unavailable(reason: str) -> dict[str, Any]:
    return {
        "available": False,
        "reason": reason,
        "pack_id": "",
        "library_version": "",
        "domain_cards": [],
        "reader_scenes": [],
        "knowledge_points": [],
        "bad_sentence_warnings": [],
        "rewrite_pairs": [],
        "platform_notes": [],
        "claim_boundaries": [],
        "source_notes": [],
    }


def load_request(args: argparse.Namespace) -> dict[str, Any]:
    if args.request:
        path = Path(args.request)
        return json.loads(path.read_text(encoding="utf-8"))

    needs = args.needs or [
        "reader scenes",
        "domain texture",
        "bad sentence warnings",
        "rewrite moves",
        "platform notes",
        "claim boundaries",
    ]
    return {
        "skill": "creator-content-expert-team",
        "version": "4.0.0",
        "language": args.language,
        "domain": args.domain,
        "topic": args.topic,
        "platform": args.platform,
        "audience": args.audience,
        "risk_level": args.risk_level,
        "voice": args.voice,
        "needs": needs,
    }


def fetch_pack(payload: dict[str, Any]) -> dict[str, Any]:
    url = os.environ.get("CREATOR_CONTENT_LIBRARY_URL", "").strip()
    if not url:
        return unavailable("CREATOR_CONTENT_LIBRARY_URL is not configured")

    token = os.environ.get("CREATOR_CONTENT_LIBRARY_TOKEN", "").strip()
    timeout_raw = os.environ.get("CREATOR_CONTENT_LIBRARY_TIMEOUT", "12").strip()
    try:
        timeout = float(timeout_raw)
    except ValueError:
        timeout = 12.0

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent": "creator-content-expert-team/4.0.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            text = raw.decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        return unavailable(f"HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        return unavailable(f"network error: {exc.reason}")
    except TimeoutError:
        return unavailable("request timed out")

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {
            **unavailable("response was not valid JSON"),
            "raw_response": text[:2000],
        }

    if not isinstance(data, dict):
        return unavailable("response JSON must be an object")
    data.setdefault("available", True)
    return data


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def format_markdown(pack: dict[str, Any]) -> str:
    lines = [
        "# Context Pack V3",
        "",
        f"- Available: {'yes' if pack.get('available') else 'no'}",
        f"- Pack ID: {pack.get('pack_id', '')}",
        f"- Library version: {pack.get('library_version', '')}",
    ]
    if pack.get("reason"):
        lines.append(f"- Reason: {pack.get('reason')}")

    sections = [
        ("Reader Scenes", "reader_scenes"),
        ("Domain Cards", "domain_cards"),
        ("Knowledge Points", "knowledge_points"),
        ("Bad Sentence Warnings", "bad_sentence_warnings"),
        ("Rewrite Pairs", "rewrite_pairs"),
        ("Platform Notes", "platform_notes"),
        ("Claim Boundaries", "claim_boundaries"),
        ("Source Notes", "source_notes"),
    ]
    for title, key in sections:
        lines.extend(["", f"## {title}", ""])
        values = as_list(pack.get(key))
        if not values:
            lines.append("-")
            continue
        for item in values:
            if isinstance(item, (dict, list)):
                rendered = json.dumps(item, ensure_ascii=False)
            else:
                rendered = str(item)
            lines.append(f"- {rendered}")

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    try:
        payload = load_request(args)
    except Exception as exc:  # noqa: BLE001 - command-line helper should fail soft.
        pack = unavailable(f"could not load request: {exc}")
    else:
        pack = fetch_pack(payload)

    if args.output == "json":
        print(json.dumps(pack, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(format_markdown(pack))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
