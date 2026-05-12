# 小灯内容专家团 / Xiaodeng Content Expert Team

一个中文真实语境优先的开源内容创作 skill。它可以用于写作、改写、审核、平台适配和商业文案，覆盖美食、情感、投资/金融、法律、医学/健康、小说、品牌广告、博客、短视频脚本、SEO、newsletter、落地页和产品文案。

An open-source, Chinese-first content creation skill for drafting, rewriting, auditing, and adapting content across domains. It uses an editor-led workflow plus a V4 advanced card stack to reduce generic AI-feel and produce reader-specific, publishable writing.

## 核心特点 / Highlights

- **V4 卡片栈**：读者卡、矛盾卡、材料卡、结构卡、平台卡、证据卡、句子修复卡、审核卡组合使用。
- **真实中文语境**：优先处理场景、例子、日常表达、怪句和假比喻。
- **专家团流程**：小灯主编 -> 栗栗采风员 -> 小墨执笔人 -> 豆豆挑刺官 -> 小剪修订员。
- **高风险边界**：医学、法律、金融/投资内容默认只写通用科普或信息稿。
- **开箱可用**：不依赖私有远程库；包内自带高级卡片库和推荐脚本。
- **可扩展**：保留私有远程写作库接口，后续可接入自己的语境包服务。

English:

- **V4 card stack**: reader, tension, material, structure, platform, evidence, sentence repair, and review cards.
- **Chinese realism first**: scenes, examples, natural phrasing, anti-weird-metaphor checks.
- **Editorial workflow**: lead editor, context scout, draft writer, skeptical reviewer, revision executor.
- **Risk boundaries**: medical, legal, and financial/investing content stays educational unless qualified sources are provided.
- **Works out of the box**: no private remote library required.
- **Extensible**: optional remote context-pack API is included for future private libraries.

## 一行安装 / One-Line Install

安装到所有支持的本地工具：

```bash
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh
```

只安装到某一个工具：

```bash
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh -s -- --target codex
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh -s -- --target gpt-codex
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh -s -- --target hermes
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh -s -- --target openclaw
curl -fsSL https://raw.githubusercontent.com/robertstarry-gif/xiaodeng-content-expert-team/main/install.sh | sh -s -- --target claude-code
```

默认安装位置：

- Codex / GPT-Codex: `~/.codex/skills/creator-content-expert-team`
- Hermes: `~/.hermes/skills/creator-content-expert-team`
- OpenClaw: `~/.openclaw/workspace/skills/creator-content-expert-team`
- Claude Code: `~/.claude/skills/creator-content-expert-team`

## 使用示例 / Usage

```text
Use $creator-content-expert-team.
领域：生活方式
题目：为什么周末明明休息了，反而更累
平台：公众号文章
读者：工作日压力很大的城市上班族
语气：真实、具体、不要鸡汤、不要 AI 感
要求：先用真实场景进入，不要用“不是 A 而是 B”的抽象句式开头
```

```text
Use $creator-content-expert-team.
Domain: brand advertising
Product: an AI note-taking app
Platform: landing page
Audience: consultants and researchers
Voice: clear, credible, not hype
Need: conversion copy with proof, objections, and safe claims
```

## V4 卡片栈 / V4 Card Stack

写作前会先选择一组卡片：

- Reader: 读者是谁，读到这里时处在什么状态。
- Tension: 这篇内容为什么值得读下去。
- Material: 哪些具体场景和细节能托住观点。
- Structure: 内容应该怎样展开。
- Platform: 公众号、GitHub、短视频、小红书、落地页等表面结构。
- Evidence: 哪些话能说，哪些话必须降级。
- Sentence: 哪些句式容易有 AI 感。
- Review: 最后按什么标准挑刺。

可用脚本推荐卡片：

```bash
python3 scripts/select_content_cards.py --domain "AI tools" --platform "公众号" --audience "技术小白" --topic "OpenClaw 安装门槛和替代方案"
```

## 质量测试 / Quality Test

Prompt:

```text
Use $creator-content-expert-team.
领域：生活方式
题目：为什么周末明明休息了，反而更累
平台：公众号短文
读者：工作日压力很大的城市上班族
语气：真实、具体、不要鸡汤、不要 AI 感
长度：短文章
```

Sample opening:

```markdown
# 好不容易到了周末，为什么还是累？

周五晚上，你可能已经想好了：明天一定要好好休息。

睡到自然醒，吃点好的，把没看的电影补上，顺便收拾一下房间。最好还能出门走走，见个朋友，或者什么都不做。

结果到了周六中午，你躺在床上刷手机。
```

测试重点：

- 开头先进入真实读者场景，不先抛抽象金句。
- 用日常选择解释疲惫，而不是用怪比喻硬撑观点。
- 结尾收住具体问题，不喊口号。

## 私有远程写作库 / Optional Private Library

当前公开版不依赖私有库。包里保留了私有远程写作库接口，未来可以通过 `CREATOR_CONTENT_LIBRARY_URL` 返回语境包，但默认使用内置 V4 卡片栈。

## 安全边界 / Safety

- 医学内容不能诊断或开治疗方案。
- 法律内容不能提供个性化法律策略。
- 金融/投资内容不能告诉具体个人买什么、卖什么或怎么配置。

## 验证 / Validate

```bash
python3 scripts/validate_creator_content_expert_team.py
```

Expected:

```text
OK: Creator Content Expert Team public skill valid
```

## License

MIT

## 关注公众号 / Follow

如果你想继续看 AI 工具实测、内容专家团升级记录和中文写作工作流，可以扫码关注公众号。

![公众号二维码](assets/wechat-qrcode.png)
