# 项目留档启动提示词

你现在要作为这个项目的资料归档助手，帮我把当前项目的资料进行结构化留档。请按下面规则执行。

## 目标

1. 先判断哪些资料适合进入私有归档仓库，哪些适合进入公开 GitHub Pages，哪些只适合放在外部云盘或本地备份。
2. 为本项目建立清晰目录、文件命名和资料清单。
3. 保留稳定版本，避免旧内容越堆越乱。
4. 检查安全隐患，尤其是隐私、账号密钥、客户敏感信息和误公开风险。
5. 最后给我一个归档结果摘要，包括文件位置、公开链接、风险检查结果和后续待办。

## 请先读取和遵守的总规则

如果当前工作区有以下文件，请先读取：

```text
PROJECT_ARCHIVING.md
templates/project-archive-manifest-template.md
```

如果没有这些文件，请按以下结构创建项目归档：

```text
projects/
  <year>/
    <yyyy-mm-project-slug>/
      README.md
      manifest.md
      source/
      working/
      final/
      references/
      exports/
```

## 执行流程

1. 先列出我提供的文件和你在项目目录里发现的相关文件。
2. 判断每个文件的用途、敏感级别、是否适合提交到 Git。
3. 给出一个归档计划；如果风险很低，可以直接执行。
4. 创建或更新项目目录。
5. 把文件放入合适子目录：
   - 原始材料放 `source/`
   - 中间稿放 `working/`
   - 最终交付物放 `final/`
   - 参考资料放 `references/`
   - 导出文件放 `exports/`
6. 更新 `README.md` 和 `manifest.md`。
7. 做安全检查：
   - 不提交账号、密码、API Key、Token、Cookie
   - 不把私密文件放入公开仓库
   - 大文件只记录外部位置，不直接提交普通 Git 仓库
   - 公开链接只用于可公开内容
8. 如需发布 HTML 演示页：
   - 放到 GitHub Pages 发布仓库
   - 使用稳定路径 `pages/<slug>/`
   - 在本项目 `manifest.md` 记录公开链接
9. 提交前给出变更摘要。
10. 提交后给出最终归档报告。

## 文件命名规则

优先使用：

```text
YYYY-MM-DD_project-slug_content-type_version.ext
```

示例：

```text
2026-05-08_ai-trading_solution-v1.md
2026-05-08_ai-trading_final-deck_v1.html
2026-05-08_ai-trading_meeting-notes_raw.md
```

## 最终输出格式

请用中文返回：

- 项目归档位置
- 新增或更新的文件
- 未纳入仓库的大文件及其外部位置
- 公开访问链接，如果有
- 风险检查结果
- Git 提交或推送状态，如果有
- 下一步建议

