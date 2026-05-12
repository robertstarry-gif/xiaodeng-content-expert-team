#!/usr/bin/env python3
"""Validate the public Creator Content Expert Team skill package.

No third-party dependencies.
"""
from pathlib import Path
import base64
import json
import py_compile
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"

required = [
    "references/reverse-engineered-workflow-v2.md",
    "references/advanced-card-library-v4.md",
    "references/basic-card-library-v3.md",
    "references/chinese-real-context-guide-v3.md",
    "references/remote-writing-library-architecture-v3.md",
    "references/anti-ai-style-guide-v2.md",
    "references/domain-risk-guide.md",
    "references/platform-and-format-guide.md",
    "references/open-source-maintenance.md",
    "templates/remote-context-request-v3.json",
    "templates/context-pack-v3.md",
    "templates/card-stack-brief-v4.md",
    "templates/content-quality-test-v4.md",
    "templates/source-scout-report-v3.md",
    "templates/review-card-v3.md",
    "templates/revision-ticket-v2.md",
    "templates/content-kernel-card-v1.md",
    "templates/writer-brief-v1.md",
    "templates/writer-brief-v2.md",
    "templates/audit-card-v1.md",
    "templates/evidence-ledger-v1.md",
    "scripts/fetch_writing_context.py",
    "scripts/select_content_cards.py",
    "scripts/validate_creator_content_expert_team.py",
    "agents/openai.yaml",
    "README.md",
    "install.sh",
    "LICENSE",
]

errors: list[str] = []

if not skill.exists():
    errors.append("missing SKILL.md")
    content = ""
else:
    content = skill.read_text(encoding="utf-8")

frontmatter = ""
if not content.startswith("---\n"):
    errors.append("SKILL.md must start with frontmatter")
else:
    close = content.find("\n---\n", 4)
    if close == -1:
        errors.append("SKILL.md missing closing frontmatter")
    else:
        frontmatter = content[4:close]

top_keys = []
for raw in frontmatter.splitlines():
    if not raw.strip() or raw.lstrip().startswith("#"):
        continue
    if raw.startswith((" ", "\t")):
        continue
    if ":" in raw:
        top_keys.append(raw.split(":", 1)[0].strip())

top_key_set = set(top_keys)
allowed_top_keys = {"name", "description", "metadata"}
for key in ["name", "description"]:
    if key not in top_key_set:
        errors.append(f"missing required frontmatter key: {key}")
for key in sorted(top_key_set - allowed_top_keys):
    errors.append(f"unexpected top-level frontmatter key: {key}")

if "name: creator-content-expert-team" not in frontmatter:
    errors.append("frontmatter name must be creator-content-expert-team")
if "version: 4.0.0" not in frontmatter:
    errors.append("metadata version must be 4.0.0")
if "license: MIT" not in frontmatter:
    errors.append("metadata license must be MIT")

required_triggers = [
    "美食",
    "情感",
    "投资",
    "法律",
    "医学",
    "小说",
    "品牌广告",
    "rewriting",
    "auditing",
    "platform adaptation",
    "anti-AI",
]
for trigger in required_triggers:
    if trigger not in frontmatter:
        errors.append(f"description missing trigger: {trigger}")

for rel in required:
    if not (root / rel).exists():
        errors.append(f"missing linked file: {rel}")

must_contain = [
    "用能保证质量的最小流程",
    "小灯主编 -> 栗栗采风员 -> 小墨执笔人 -> 豆豆挑刺官 -> 小剪修订员 -> 最终交付",
    "V4 卡片栈",
    "references/advanced-card-library-v4.md",
    "scripts/select_content_cards.py",
    "远程语境包",
    "CREATOR_CONTENT_LIBRARY_URL",
    "scripts/fetch_writing_context.py",
    "中文真实感检查",
    "读者场景",
    "中心矛盾",
    "中文真实语境",
    "高风险内容",
    "不做个性化诊断",
    "金融/投资内容不提供个性化买卖建议",
    "只提供教育信息",
    "TEST-PUBLISH",
    "No private paths, names, memories, or local workflows",
]
for needle in must_contain:
    if needle not in content:
        errors.append(f"SKILL.md missing required phrase: {needle}")

banned_role_name_tokens = [
    "6IuP5a+75rqQ",
    "5Lil5a6h5LmL",
    "5pSv56yU55Sf",
]
banned_role_names = [
    base64.b64decode(term).decode("utf-8") for term in banned_role_name_tokens
]
for name in banned_role_names:
    for path in root.rglob("*"):
        if path.is_dir() or path.name == ".DS_Store":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if name in text:
            errors.append(f"old role name {name!r} found in {path.relative_to(root)}")

encoded_private_terms = [
    "THVjYXM=",
    "L2FpMQ==",
    "T2JzaWRpYW4=",
    "VGVsZWdyYW0=",
    "L1VzZXJzL3JvYmVydA==",
    "YWktZGV2ZWxvcG1lbnQtY2FyZWVyLWFwcGxpY2F0aW9u",
]
banned_private_terms = [
    base64.b64decode(term).decode("utf-8") for term in encoded_private_terms
]
for path in root.rglob("*"):
    if path.is_dir() or path.name == ".DS_Store":
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for term in banned_private_terms:
        if term in text:
            errors.append(f"private term {term!r} found in {path.relative_to(root)}")

if (root / ".DS_Store").exists():
    errors.append(".DS_Store should not be included")

request_template = root / "templates/remote-context-request-v3.json"
if request_template.exists():
    try:
        json.loads(request_template.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"remote context request template is invalid JSON: {exc}")

fetch_script = root / "scripts/fetch_writing_context.py"
if fetch_script.exists():
    try:
        with tempfile.TemporaryDirectory() as tmp:
            py_compile.compile(
                str(fetch_script),
                cfile=str(Path(tmp) / "fetch_writing_context.pyc"),
                doraise=True,
            )
    except py_compile.PyCompileError as exc:
        errors.append(f"fetch_writing_context.py does not compile: {exc}")

select_script = root / "scripts/select_content_cards.py"
if select_script.exists():
    try:
        with tempfile.TemporaryDirectory() as tmp:
            py_compile.compile(
                str(select_script),
                cfile=str(Path(tmp) / "select_content_cards.pyc"),
                doraise=True,
            )
    except py_compile.PyCompileError as exc:
        errors.append(f"select_content_cards.py does not compile: {exc}")

readme = root / "README.md"
if readme.exists():
    readme_text = readme.read_text(encoding="utf-8")
    for target in ["codex", "gpt-codex", "hermes", "openclaw", "claude-code"]:
        if f"--target {target}" not in readme_text:
            errors.append(f"README missing install command for {target}")
    if "__GITHUB_REPO__" not in readme_text and "raw.githubusercontent.com/" not in readme_text:
        errors.append("README should include the repository placeholder or a released GitHub raw URL")
    for phrase in [
        "小灯主编",
        "栗栗采风员",
        "豆豆挑刺官",
        "V4 卡片栈",
        "私有远程写作库",
        "好不容易到了周末",
    ]:
        if phrase not in readme_text:
            errors.append(f"README missing V3 phrase: {phrase}")

install = root / "install.sh"
if install.exists():
    install_text = install.read_text(encoding="utf-8")
    for target in ["codex", "gpt-codex", "hermes", "openclaw", "claude-code"]:
        if target not in install_text:
            errors.append(f"installer missing target {target}")

if errors:
    print("FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("OK: Creator Content Expert Team public skill valid")
