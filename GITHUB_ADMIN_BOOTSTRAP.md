# GitHub 管理员启动总览

这份总览用于把新开的项目对话变成对应项目的 GitHub 管理员。管理员不是负责讨论项目内容本身，而是负责上传、备份、留档、发布和记录。

## 两类管理员

### 1. 项目资料备份管理员

适用场景：

- 项目资料、方案、会议纪要、交付物、截图、参考资料的长期留档。
- 不同项目之间必须隔离。
- 主要进入私有 GitHub 仓库。

启动文档：

```text
templates/github-project-backup-startup-doc.md
```

启动提示词：

```text
templates/github-project-backup-startup-prompt.md
```

### 2. HTML 演示发布管理员

适用场景：

- 单文件 HTML 演示页上传。
- 上传后需要从任何地方用浏览器稳定访问。
- 所有原始 HTML 上传件统一进入 `html/` 文件夹，使用时间码和 slug 命名。
- 对外稳定访问入口为 `pages/<slug>/`。

启动文档：

```text
templates/html-demo-upload-startup-doc.md
```

启动提示词：

```text
templates/html-demo-upload-startup-prompt.md
```

## 管理员共同职责

每个新项目对话启动后，管理员需要：

1. 确认当前任务属于项目备份、HTML 发布，还是两者都有。
2. 确认目标 GitHub 仓库和访问权限。
3. 创建或定位对应项目文件夹。
4. 上传或更新文件。
5. 更新本地记录和仓库内清单。
6. 提交并推送到 GitHub。
7. 返回本次操作报告。

## 共同风险边界

管理员必须避免：

- 把私密资料放进公开 Pages 仓库。
- 把账号、密码、API Key、Token、Cookie、证书提交到 GitHub。
- 把多个项目资料混进同一个项目目录。
- 只上传文件但不更新清单和日志。
- 依赖本机路径、临时下载路径或不稳定外链。

## 推荐仓库

### 公开 HTML 发布仓库

```text
iwufai-dotcom/ai-trading-boundary-presentation
```

用途：

- 公开 HTML 演示页。
- GitHub Pages 发布。
- 不存放私密项目资料。

### 私有项目归档仓库

建议准备：

```text
iwufai-dotcom/project-archive-private
```

用途：

- 项目资料长期留档。
- 私密资料、内部资料、客户资料。
- 不开启 GitHub Pages。

如果私有仓库尚未创建，项目资料备份管理员启动后应先创建或要求确认目标仓库。

## 自动备份能力说明

这里的“自动备份”指：在对应项目对话中，只要你发送启动提示词并提供文件，管理员会自动执行标准流程，包括分类、命名、创建目录、上传、更新清单、提交和返回报告。

如果需要定时自动检查某个本地目录并备份，需要额外配置 Codex 自动化、GitHub Actions 或本地定时任务。默认启动提示词不会在没有你触发的情况下后台运行。

## 建议使用方式

1. 在当前总控对话维护这些规则和模板。
2. 每个项目新开一个对话。
3. 把对应启动文档丢进去。
4. 发送对应启动提示词。
5. 再提供文件、目录或 HTML。
6. 让该对话长期担任该项目的 GitHub 管理员。

