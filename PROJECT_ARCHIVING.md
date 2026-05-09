# 项目资料留档与备份工作流

这份文档用于规划项目资料的上传、备份和留档。它不要求在总控对话里处理每个项目的具体文件；每个项目可以在自己的对话中独立完成归档，但遵守同一套结构和安全规则。

## 目标

- 每个项目独立留档，避免资料混在一起。
- 重要材料有稳定位置、版本记录和说明。
- 公开演示材料与私密项目资料分开保存。
- 后续只要把文件丢给 Codex，就能快速判断、整理、上传和记录。

## 推荐仓库分工

### 1. 公开演示仓库

用途：存放可以公开访问的 HTML 演示页、对外展示页。

当前仓库：

```text
ai-trading-boundary-presentation
```

规则：

- 只放可公开内容。
- 每个页面使用稳定路径：`pages/<slug>/`。
- 同一主题更新时覆盖原路径，由 Git 历史保留旧版本。
- 不放客户隐私、合同、报价、账号、内部策略、原始会议记录。

### 2. 私有项目留档仓库

建议新建一个私有仓库，例如：

```text
project-archive-private
```

用途：

- 项目资料归档。
- 文档、方案、会议纪要、交付版本、关键截图、小型附件。
- 记录大文件在网盘或本地备份盘中的位置。

建议保持私有，不开启 GitHub Pages。

### 3. 大文件备份区

GitHub 不适合长期存放大量视频、录音、大型压缩包、超大 PPT 或设计源文件。

建议使用：

- Google Drive / 飞书云文档 / 百度网盘 / iCloud Drive。
- 本地移动硬盘或 NAS。
- 如以后有技术需要，再考虑 Git LFS。

私有仓库只保存这些大文件的索引、摘要、下载位置和校验信息。

## 项目目录结构

每个项目单独一个目录：

```text
projects/
  2026/
    2026-05-project-name/
      README.md
      manifest.md
      source/
      working/
      final/
      references/
      exports/
```

目录含义：

- `README.md`：项目说明、状态、负责人、关键链接。
- `manifest.md`：文件清单、版本说明、外部备份位置。
- `source/`：原始材料，原则上只追加、不覆盖。
- `working/`：处理中间稿，可更新。
- `final/`：最终交付物或稳定版本。
- `references/`：参考资料、截图、链接摘录。
- `exports/`：导出的 PDF、HTML、图片、压缩包等。

## 文件命名规则

推荐格式：

```text
YYYY-MM-DD_project-name_content-type_version.ext
```

示例：

```text
2026-05-08_ai-trading_client-brief_v1.md
2026-05-08_ai-trading_solution-final_v1.pdf
2026-05-08_ai-trading_meeting-notes_raw.md
```

规则：

- 文件名使用英文小写、数字和短横线。
- 避免 `最终版`、`final-final`、`新新新` 这类不可追踪命名。
- 原始文件如需保留中文名，可以放入 `source/`，但在 `manifest.md` 中登记说明。

## 版本策略

### 原始资料

原始资料进入 `source/` 后不覆盖。新收到的材料另存新文件。

### 工作稿

工作稿可以覆盖，但重要节点建议另存版本，例如 `v1`、`v2`、`reviewed`。

### 最终稿

最终稿放入 `final/`，并在 `manifest.md` 中标记当前有效版本。

### 对外展示页

公开 HTML 放到 Pages 发布仓库，不放在私有归档仓库里承担展示职责。私有仓库只记录公开链接和源文件位置。

## 安全边界

归档前必须检查：

- 是否包含客户姓名、手机号、邮箱、身份证、地址等个人信息。
- 是否包含账号、密码、API Key、Cookie、Token、证书。
- 是否包含合同金额、报价、未公开商业策略。
- 是否包含客户授权范围不明确的录音、截图、聊天记录。
- 是否包含不能公开的第三方版权材料。
- 是否误放到公开 Pages 仓库。

处理原则：

- 能公开的放公开仓库。
- 不能公开但需要版本管理的放私有仓库。
- 大且敏感的原始文件放云盘或本地备份，仓库只放索引。
- 密钥、密码、Token 不进入任何仓库。

## 单个项目的标准归档流程

1. 收集文件和背景说明。
2. 判断项目类别、敏感级别和归档目标。
3. 创建项目目录。
4. 将资料分入 `source/`、`working/`、`final/`、`references/`、`exports/`。
5. 统一文件名，保留必要的原始文件名映射。
6. 更新 `README.md` 和 `manifest.md`。
7. 本地检查是否有危险内容或超大文件。
8. 提交到私有仓库。
9. 如有公开 HTML，再同步发布到 Pages 仓库，并在项目 `manifest.md` 记录链接。

## 前期测试清单

第一次正式使用前，建议在测试项目里跑一遍：

```text
projects/2026/2026-05-archive-test/
```

测试内容：

- 放入一个 Markdown 文档。
- 放入一个 PDF 或小型 Office 文件。
- 放入一个 HTML 演示页链接记录。
- 模拟一个大文件，只在 `manifest.md` 记录外部位置。
- 提交到私有仓库。
- 确认 GitHub 私有权限正确。
- 确认不会被 GitHub Pages 公开访问。

## 日常使用规则

- 每个项目单开对话，由项目内对话执行归档。
- 这个总控对话只维护规则、模板和安全检查。
- 项目资料备份对话开始时，先提供 `templates/github-project-backup-startup-doc.md`，再发送 `templates/github-project-backup-startup-prompt.md`。
- HTML 演示发布对话开始时，先提供 `templates/html-demo-upload-startup-doc.md`，再发送 `templates/html-demo-upload-startup-prompt.md`。
- 每次归档后，让 Codex 返回：放置位置、文件清单、风险检查结果、提交记录或待办。

## 不建议做的事

- 不要把所有项目都塞进一个无结构文件夹。
- 不要在公开 Pages 仓库里备份私密资料。
- 不要把大视频、大录音直接提交到普通 Git 仓库。
- 不要靠文件名里的“最终版”管理版本。
- 不要只上传文件而不写 `manifest.md`。
