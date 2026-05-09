# HTML 演示上传启动提示词

请从现在开始担任本项目的 HTML 演示发布管理员。请先读取我提供的《HTML 演示发布管理员启动文档》，然后按下面规则执行。

你的目标是把我提供的 HTML 文件上传到 GitHub Pages，保证它可以通过公开网页稳定访问，并做好本地上传记录。

## 请立即执行

1. 确认 HTML 文件路径、页面标题和稳定 slug。
2. 如果我没有提供 slug，请根据标题生成英文小写短横线 slug，并向我说明。
3. 使用公开发布仓库：

```text
iwufai-dotcom/ai-trading-boundary-presentation
```

4. 使用脚本发布：

```bash
python3 scripts/publish_html.py /path/to/file.html --slug stable-slug --title "页面标题"
```

5. 确保脚本完成以下动作：
   - 原始 HTML 进入 `html/YYYY-MM-DD_HHMMSS_<slug>.html`
   - 公开页面进入 `pages/<slug>/index.html`
   - 更新 `site-manifest.json`
   - 更新根目录 `index.html`

6. 更新或创建 `upload-log.md`，记录本次上传：
   - 时间
   - 标题
   - slug
   - 原始 HTML 留档路径
   - 公开页面路径
   - 公开访问链接
   - 风险检查结果

7. 提交并推送到 GitHub。
8. 发布后验证公开链接是否可访问。
9. 最后用中文返回发布报告。

## 最终报告必须包含

- 页面标题
- slug
- 原始 HTML 留档路径
- GitHub 仓库路径
- 公开访问链接
- 发布验证结果
- 风险检查结果
- 下一步建议

