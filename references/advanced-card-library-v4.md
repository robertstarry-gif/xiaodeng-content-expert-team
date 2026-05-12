# Advanced Card Library V4

V4 uses a card stack, not a loose card list. A draft should be built from several cards that pressure-test each other:

1. Reader reality
2. Hidden tension
3. Domain material
4. Platform shape
5. Evidence boundary
6. Sentence repair
7. Review standard

Do not show the card stack to the user unless asked. Use it to produce writing that feels specific, useful, and hard to replace with a generic model answer.

## How To Use

For any substantial Chinese public-facing content, choose one card from at least five groups:

- `READER`: who is really reading and what state they are in.
- `TENSION`: what conflict makes the piece worth reading.
- `MATERIAL`: what concrete details prevent empty prose.
- `STRUCTURE`: how the article should unfold.
- `PLATFORM`: how the surface changes by channel.
- `SENTENCE`: what language trap to avoid.
- `REVIEW`: what must be attacked before delivery.

If the piece is factual, commercial, medical, legal, financial, or current, also choose one `EVIDENCE` card.

## Card Stack Protocol

Use this order before drafting:

```text
1. Pick reader state.
2. Pick hidden tension.
3. Pick domain material.
4. Pick platform shape.
5. Pick evidence boundary if needed.
6. Pick sentence traps.
7. Draft.
8. Review with matching review card.
9. Revise exact weak lines.
```

## Reader Cards

### READER-001 技术小白但很想试

- State: 想体验新工具，但害怕终端、API、英文文档和报错。
- Need: 先知道该不该入坑，再知道怎么降低门槛。
- Write with: 具体卡点、普通解释、替代路径。
- Avoid: 嘲笑小白、堆命令、默认读者懂开发。

### READER-002 重度工具玩家

- State: 愿意折腾，关心自由度、权限、扩展、稳定性和成本。
- Need: 判断工具是否值得投入时间。
- Write with: 架构、边界、对比、真实坑位。
- Avoid: 只讲体验，不讲可控性和维护代价。

### READER-003 内容创作者

- State: 不一定懂技术，但想用 AI 提高选题、写作、分发效率。
- Need: 能直接转成工作流的建议。
- Write with: 选题、素材、草稿、审核、发布场景。
- Avoid: 把工具介绍写成开发文档。

### READER-004 决策者 / 老板

- State: 关心投入产出、风险、团队效率、可控性。
- Need: 判断是否值得试点。
- Write with: 成本、风险、人员要求、试点路线。
- Avoid: 只说酷，不说落地条件。

### READER-005 焦虑型普通用户

- State: 被热度吸引，但怕错过，也怕折腾半天没结果。
- Need: 清楚地知道“先做什么，后做什么”。
- Write with: 轻重路径、避坑、推荐顺序。
- Avoid: 制造 FOMO。

## Tension Cards

### TENSION-001 演示很轻，落地很重

- Core: 视频里一句话能跑任务，自己安装时遇到环境、模型、API、渠道、日志。
- Use when: 写 AI agent 工具、自动化工具、开源工具。
- Strong turn: “真正难的不是安装，而是安装后每一步都引出新概念。”

### TENSION-002 自由度越高，配置成本越高

- Core: 开源工具给控制权，也把选择、配置、排错交给用户。
- Use when: 比较 OpenClaw、WorkBuddy、Dify、n8n、AutoGPT 等。
- Strong turn: “省心和自由，很难同时拉满。”

### TENSION-003 会说话的 AI 到能接活的 AI

- Core: 用户不再满足于问答，希望 AI 进工作流。
- Use when: 解释 agent 爆火、助手产品、办公自动化。
- Strong turn: “大家要的不是更长的回答，而是更少的手动搬运。”

### TENSION-004 产品化体验 vs 工程化底座

- Core: 产品化工具降低门槛，工程化工具保留控制。
- Use when: 推荐小白先用 WorkBuddy，再进阶 OpenClaw。
- Strong turn: “一个适合先用起来，一个适合深度改造。”

### TENSION-005 能力越强，边界越重要

- Core: 能读文件、发消息、跑命令的工具，比普通聊天工具更需要权限管理。
- Use when: 讲安全、隐私、公司内部使用。
- Strong turn: “它不是说错一句话那么简单，它可能真的去执行。”

## Material Cards

### MATERIAL-001 安装后的第一堵墙

- Details: 终端、Node、npm、环境变量、配置文件、服务启动、日志。
- Convert to prose: “看到终端还能坚持，看到配置文件很多人就开始退。”
- Avoid: 把命令堆给普通读者。

### MATERIAL-002 模型配置

- Details: 模型不是工具自带；要有 API Key、Base URL、模型名称、余额、调用权限。
- Convert to prose: “房子搭好了，但里面还没有大脑。”
- Avoid: 说“配置一下模型就行”。

### MATERIAL-003 中转站

- Details: 统一转发、兼容接口、网络可达、计费管理、稳定性。
- Convert to prose: “你和模型之间多了一个代收代转的前台。”
- Avoid: 把中转站写成万能加速器。

### MATERIAL-004 聊天入口

- Details: 聊天机器人、Token、long polling、webhook、企业 IM app、群机器人、扫码绑定。
- Convert to prose: “想从手机发一句话，背后其实是一套消息接入工程。”
- Avoid: 让读者以为所有平台都是扫码秒通。

### MATERIAL-005 额外成本

- Details: 模型 token、云服务器、长期运行设备、中转服务、时间维护、报错排查。
- Convert to prose: “开源的是框架，不是算力、时间和稳定性。”
- Avoid: 只讲金钱，不讲维护成本。

### MATERIAL-006 专家团 / 小团队写作

- Details: 选题、采风、写作、审核、修订分工；用户只提交想法。
- Convert to prose: “你不用懂 skill，它把分工包装成一个可直接使用的入口。”
- Avoid: 夸成全自动完美内容工厂。

### MATERIAL-007 二维码 / 社群转化

- Details: 公众号二维码、关注提示、GitHub README 底部、文章末尾。
- Convert to prose: “想继续看实测和工具拆解，可以关注公众号。”
- Avoid: 放在正文中间打断阅读。

## Structure Cards

### STRUCTURE-001 体验评测型

- Flow: 期待 -> 上手 -> 卡点 -> 替代路线 -> 适合谁 -> 结论。
- Best for: 新工具体验、AI 工具测评、公众号文章。
- Must include: 真实卡点，不只夸功能。

### STRUCTURE-002 小白解释型

- Flow: 一句话解释 -> 生活类比 -> 一个例子 -> 常见误区 -> 下一步。
- Best for: API、中转站、Webhook、agent、MCP 等概念解释。
- Must include: 概念只解释到够用，不展开教科书。

### STRUCTURE-003 对比推荐型

- Flow: 同一需求 -> A 的优势 -> A 的门槛 -> B 的优势 -> 谁适合谁。
- Best for: OpenClaw vs WorkBuddy。
- Must include: 不制造无脑站队。

### STRUCTURE-004 开源项目介绍型

- Flow: 它是什么 -> 为什么值得关注 -> 能做什么 -> 难在哪里 -> 怎么开始。
- Best for: GitHub README、技术介绍文章。
- Must include: 安装、边界、贡献方式。

### STRUCTURE-005 转化型结尾

- Flow: 总结价值 -> 适用人群 -> 下一步行动 -> 关注/安装。
- Best for: 公众号、README、发布帖。
- Must include: 不喊空口号，给具体行动。

## Platform Cards

### PLATFORM-001 公众号

- Surface: 短段落、真实体验、具体例子、轻标题、结尾收束。
- Avoid: 连续技术名词、过长列表、硬广告。

### PLATFORM-002 GitHub README

- Surface: 快速定位、安装命令、能力列表、中英文说明、示例、许可证。
- Avoid: 公众号式长铺垫、过度营销。

### PLATFORM-003 小红书

- Surface: 开头给结论，人群明确，步骤短，适合截图。
- Avoid: 大段背景和复杂技术。

### PLATFORM-004 技术博客

- Surface: 概念准确、图示/流程、边界、复现路径。
- Avoid: 只有体验没有证据。

### PLATFORM-005 Landing Page

- Surface: 痛点、承诺、证明、异议处理、CTA。
- Avoid: 无证据地说“最好”“第一”“断档领先”。

## Evidence Cards

### EVIDENCE-001 官方功能声明

- Use when: 写产品支持什么功能。
- Need: 官方文档、帮助命令、配置页、版本号。
- Rewrite rule: “支持”只写有来源或本机验证过的功能。

### EVIDENCE-002 个人体验声明

- Use when: 写“我用下来觉得”。
- Need: 明确是主观体验，不写成行业事实。
- Rewrite rule: “最好”改成“我目前用过里面体验最顺的一款”。

### EVIDENCE-003 成本声明

- Use when: 写价格、API 成本、云服务器成本。
- Need: 官方价格页或不写具体数。
- Rewrite rule: 不确定价格时写“取决于模型和调用量”。

### EVIDENCE-004 高风险边界

- Use when: 医学、法律、金融、投资。
- Need: 通用信息、日期、地域、专业边界。
- Rewrite rule: 不给个人诊断、法律策略、买卖建议。

### EVIDENCE-005 当前信息

- Use when: 新闻、爆火、版本、平台功能。
- Need: 当前日期、来源、查证时间。
- Rewrite rule: 不把热度感觉写成硬数据。

## Sentence Cards

### SENTENCE-001 别把形式当观点

- Trap: “不是 A，而是 B”反复出现。
- Diagnosis: 句子看起来有力，但没有展示真实原因。
- Fix: 先给场景，再说判断。

### SENTENCE-002 别提前升华

- Trap: 小体验直接上升到人生、时代、革命。
- Diagnosis: 结论过大，读者不信。
- Fix: 让结论只覆盖当前场景。

### SENTENCE-003 别用假熟口吻

- Trap: “姐妹们”“家人们”“闭眼冲”不看平台乱用。
- Diagnosis: 语气不属于作者。
- Fix: 用自然叙述，不强行贴近。

### SENTENCE-004 别堆抽象名词

- Trap: 效率、闭环、赋能、生态、范式、重构连续出现。
- Diagnosis: 信息密度看似高，画面密度很低。
- Fix: 换成动作、界面、文件、消息、付款、等待。

### SENTENCE-005 技术词先翻译成人话

- Trap: API、Webhook、long polling、agent、gateway 不解释。
- Diagnosis: 读者被排除在门外。
- Fix: 先给生活类比，再给技术名词。

### SENTENCE-006 不替产品吹牛

- Trap: “最强”“断档领先”“全网第一”。
- Diagnosis: 没有证据，像广告。
- Fix: 改成具体优势、适用人群、体验感受。

## Review Cards

### REVIEW-001 小白能不能跟上

- Ask: 没有技术背景的人读到这里会不会掉队？
- Fix: 每出现一个新术语，至少给一句人话解释。

### REVIEW-002 有没有真实踩坑

- Ask: 文章是不是只讲优点？
- Fix: 加一个具体卡点、一个排查成本、一个替代路径。

### REVIEW-003 有没有把主观写成事实

- Ask: “最好、最强、爆火、全面”有没有证据？
- Fix: 用“我体验下来”“更适合”“目前看到”降低过度确定性。

### REVIEW-004 读者下一步清不清楚

- Ask: 读完知道先做什么吗？
- Fix: 给两条路径：小白先产品化工具，重度用户再开源折腾。

### REVIEW-005 有没有 AI 腔

- Ask: 开头是否泛泛，结尾是否口号，例子是否假？
- Fix: 换成具体场景、真实动作、可执行建议。

## Domain Mini Cards

### DOMAIN-AI-TOOLS

- Materials: 安装、模型、API、Key、日志、渠道、权限、成本、替代路线。
- Strong angle: “AI 工具的真实门槛，不在功能，而在连接和维护。”

### DOMAIN-CONTENT

- Materials: 选题、采风、初稿、审核、改写、分发、复盘。
- Strong angle: “好内容不是多一层润色，而是多一轮真实问题检查。”

### DOMAIN-BRAND

- Materials: 人群、痛点、场景、证据、反对意见、转化路径。
- Strong angle: “先让读者相信你理解他，再让他相信产品。”

### DOMAIN-FINANCE

- Materials: 现金流、风险、期限、手续费、波动、流动性。
- Strong angle: “收益之前先讲承受能力。”

### DOMAIN-LEGAL

- Materials: 事实、证据、时间线、地域、合同、聊天记录、流程。
- Strong angle: “法律内容先讲边界，再讲原则。”

### DOMAIN-HEALTH

- Materials: 症状、持续时间、严重程度、检查、红旗信号、就医边界。
- Strong angle: “科普的价值是帮助判断下一步，不是替代诊断。”

### DOMAIN-FOOD

- Materials: 火候、时间、口感、清洗、剩菜、食材价格、厨房动线。
- Strong angle: “美食内容别只写好吃，要写怎么真的做到。”

### DOMAIN-FICTION

- Materials: 欲望、阻碍、物件、动作、沉默、后果。
- Strong angle: “让人物做事，不让作者解释主题。”

## Minimum V4 Stack

For a normal public article, use:

```text
READER + TENSION + MATERIAL + STRUCTURE + PLATFORM + SENTENCE + REVIEW
```

For factual/commercial/high-stakes content, use:

```text
READER + TENSION + MATERIAL + STRUCTURE + PLATFORM + EVIDENCE + SENTENCE + REVIEW
```
