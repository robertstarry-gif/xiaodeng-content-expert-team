#!/usr/bin/env python3
"""Suggest a V4 content card stack from simple task metadata.

No third-party dependencies. This helper is intentionally lightweight: it does
not replace editorial judgment, but it prevents drafts from starting without a
reader, tension, material, platform, sentence, and review standard.
"""
from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Suggest V4 content cards.")
    parser.add_argument("--domain", default="")
    parser.add_argument("--platform", default="")
    parser.add_argument("--audience", default="")
    parser.add_argument("--topic", default="")
    parser.add_argument("--risk", default="low")
    return parser.parse_args()


def pick_reader(text: str) -> str:
    if any(word in text for word in ["小白", "新手", "入门", "不懂"]):
        return "READER-001 技术小白但很想试"
    if any(word in text for word in ["老板", "决策", "团队", "公司"]):
        return "READER-004 决策者 / 老板"
    if any(word in text for word in ["创作者", "写作", "内容", "公众号"]):
        return "READER-003 内容创作者"
    if any(word in text for word in ["开发", "技术", "开源", "部署"]):
        return "READER-002 重度工具玩家"
    return "READER-005 焦虑型普通用户"


def pick_tension(text: str) -> str:
    if any(word in text for word in ["安装", "配置", "API", "中转", "Bot", "Webhook"]):
        return "TENSION-001 演示很轻，落地很重"
    if any(word in text for word in ["自由", "开源", "控制"]):
        return "TENSION-002 自由度越高，配置成本越高"
    if any(word in text for word in ["WorkBuddy", "替代", "对比"]):
        return "TENSION-004 产品化体验 vs 工程化底座"
    return "TENSION-003 会说话的 AI 到能接活的 AI"


def pick_material(text: str) -> str:
    if "模型" in text or "API" in text:
        return "MATERIAL-002 模型配置"
    if "中转" in text:
        return "MATERIAL-003 中转站"
    if any(word in text for word in ["飞书", "微信", "企微", "Bot", "机器人", "聊天"]):
        return "MATERIAL-004 聊天入口"
    if any(word in text for word in ["费用", "花销", "成本", "价格"]):
        return "MATERIAL-005 额外成本"
    return "MATERIAL-001 安装后的第一堵墙"


def pick_structure(text: str) -> str:
    if any(word in text for word in ["对比", "WorkBuddy", "推荐"]):
        return "STRUCTURE-003 对比推荐型"
    if any(word in text for word in ["是什么", "解释", "API", "中转", "Webhook"]):
        return "STRUCTURE-002 小白解释型"
    if any(word in text for word in ["GitHub", "README", "开源"]):
        return "STRUCTURE-004 开源项目介绍型"
    return "STRUCTURE-001 体验评测型"


def pick_platform(text: str) -> str:
    if any(word in text for word in ["README", "GitHub"]):
        return "PLATFORM-002 GitHub README"
    if any(word in text for word in ["小红书", "笔记"]):
        return "PLATFORM-003 小红书"
    if any(word in text for word in ["博客", "技术"]):
        return "PLATFORM-004 技术博客"
    return "PLATFORM-001 公众号"


def pick_evidence(risk: str, text: str) -> str:
    if any(word in text for word in ["价格", "费用", "成本"]):
        return "EVIDENCE-003 成本声明"
    if any(word in text for word in ["爆火", "版本", "最新", "支持"]):
        return "EVIDENCE-005 当前信息"
    if risk.lower() in {"high", "medical", "legal", "finance"}:
        return "EVIDENCE-004 高风险边界"
    return "EVIDENCE-002 个人体验声明"


def main() -> int:
    args = parse_args()
    text = " ".join([args.domain, args.platform, args.audience, args.topic])
    cards = [
        ("Reader", pick_reader(text)),
        ("Tension", pick_tension(text)),
        ("Material", pick_material(text)),
        ("Structure", pick_structure(text)),
        ("Platform", pick_platform(text)),
        ("Evidence", pick_evidence(args.risk, text)),
        ("Sentence", "SENTENCE-005 技术词先翻译成人话"),
        ("Review", "REVIEW-001 小白能不能跟上"),
    ]

    print("# Suggested V4 Card Stack\n")
    for label, card in cards:
        print(f"- {label}: {card}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
