# AI Trading Boundary HTML 发布仓库

这个仓库用于发布「AI 与人在交易中的效率与边界」项目相关 HTML 演示页。根目录 `index.html` 是公开索引，每个演示内容放在独立目录中，保证链接稳定。

## 当前内容

- AI 与人在交易中的效率与边界：`pages/ai-trading-boundary/`
- AI 与人在交易中的效率与边界 - Dark Atlas v2：`pages/ai-trading-boundary-dark-atlas-v2/`

## 目录结构

```text
.
├── index.html                    # 发布索引页
├── html/                         # 原始 HTML 上传件，按时间码留档
├── pages/
│   └── ai-trading-boundary/
│       └── index.html            # 当前演示页
├── site-manifest.json            # 内容清单
├── upload-log.md                 # HTML 上传记录
├── scripts/
│   └── publish_html.py           # HTML 快速整理脚本
├── GITHUB_ADMIN_BOOTSTRAP.md      # GitHub 管理员启动总览
├── PROJECT_ARCHIVING.md           # 项目资料留档规则
├── templates/                     # 项目备份和 HTML 发布启动模板
├── PUBLISHING.md                 # 发布与维护流程
├── assets/                       # 全站共享资源
└── .nojekyll
```

## 本地预览

```bash
python3 -m http.server 8000
```

访问：

```text
http://localhost:8000/
```

## 快速添加或更新 HTML

新增内容：

```bash
python3 scripts/publish_html.py /path/to/file.html --slug ai-trading-boundary-new-demo --title "页面标题"
git add .
git commit -m "Publish my-new-demo"
git push
```

更新已有内容：

```bash
python3 scripts/publish_html.py /path/to/new-file.html --slug ai-trading-boundary --title "AI 与人在交易中的效率与边界"
git add .
git commit -m "Update ai-trading-boundary"
git push
```

同一个 `slug` 会覆盖同一路径，避免重复堆出很多旧页面；历史版本由 Git 保存。

脚本会同时把原始 HTML 留档到 `html/YYYY-MM-DD_HHMMSS_<slug>.html`，并追加 `upload-log.md`。

如果页面依赖 CSS 或图片资源，可以同时复制资源并调整公开页面路径：

```bash
python3 scripts/publish_html.py /path/to/index.html \
  --slug ai-trading-boundary-dark-atlas-v2 \
  --title "AI 与人在交易中的效率与边界 - Dark Atlas v2" \
  --resource /path/to/styles.css:styles.css \
  --resource /path/to/assets/generated:assets/generated \
  --replace '../../assets/generated/=./assets/generated/'
```

## 管理员启动模板

不同项目新开对话时，可以使用：

- 项目资料备份：`templates/github-project-backup-startup-doc.md` + `templates/github-project-backup-startup-prompt.md`
- HTML 演示发布：`templates/html-demo-upload-startup-doc.md` + `templates/html-demo-upload-startup-prompt.md`
