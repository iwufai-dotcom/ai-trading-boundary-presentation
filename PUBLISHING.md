# AI Trading Boundary HTML 发布与维护流程

## 目标

这个仓库按“一个内容一个稳定路径”的方式管理「AI 与人在交易中的效率与边界」项目的公开 HTML 页面：

```text
https://<user>.github.io/<repo>/pages/<slug>/
```

根目录 `index.html` 只做索引，不直接承载某一个具体页面。这样后续新增内容不会破坏旧链接，更新已有内容也不会越堆越乱。

原始 HTML 上传件统一留档到：

```text
html/YYYY-MM-DD_HHMMSS_<slug>.html
```

公开稳定访问入口统一为：

```text
pages/<slug>/index.html
```

## 1. 更新已有内容

当一个页面只是内容更新，不要创建新目录，继续使用原来的 `slug`：

```bash
python3 scripts/publish_html.py /path/to/new.html --slug ai-trading-boundary --title "AI 与人在交易中的效率与边界"
git add .
git commit -m "Update ai-trading-boundary"
git push
```

原则：

- 同一主题固定同一个 `slug`。
- 新版本覆盖 `pages/<slug>/index.html`。
- 不手动复制 `v1`、`v2`、`final`、`final_fixed` 这类文件到发布目录。
- 需要追溯历史时用 Git 历史，而不是在网站上堆旧文件。
- 只有确实需要长期保留给别人访问的旧版本，才放到 `archive/<slug>/<date>/`。

## 2. 上传新内容

给我一个新的 HTML 文件时，我会按这个流程处理：

1. 检查是否有本地绝对路径、外部资源、缺失图片或脚本。
2. 确定是否是已有主题更新，还是新主题。
3. 选择稳定 `slug`。
4. 放到 `pages/<slug>/index.html`。
5. 更新 `site-manifest.json` 和根目录索引。
6. 将原始 HTML 留档到 `html/`。
7. 追加 `upload-log.md`。
8. 本地预览确认入口可打开。
9. 提交并推送。

命令模板：

```bash
python3 scripts/publish_html.py /path/to/file.html --slug stable-slug --title "页面标题"
git add .
git commit -m "Publish stable-slug"
git push
```

如果 HTML 依赖本地 CSS、图片或脚本资源，应把资源复制到该页面目录下，并把公开版 HTML 的资源路径调整为页面内相对路径：

```bash
python3 scripts/publish_html.py /path/to/index.html \
  --slug ai-trading-boundary-dark-atlas-v2 \
  --title "AI 与人在交易中的效率与边界 - Dark Atlas v2" \
  --resource /path/to/styles.css:styles.css \
  --resource /path/to/assets/generated:assets/generated \
  --replace '../../assets/generated/=./assets/generated/'
```

## 3. 稳定性规则

- 发布入口必须是 `index.html`。
- 原始 HTML 必须进入 `html/`，文件名带时间码和 `slug`。
- 页面资源优先内嵌，或者使用相对路径放在同目录的 `assets/` 下。
- 不使用 `/Users/...`、`Downloads/...` 这类本机路径。
- 不依赖临时外链资源；关键图片、字体、脚本应随仓库一起提交。
- 不随意改已有 `slug`，因为 URL 会变化。
- 每次发布必须更新 `upload-log.md`。
- 每次发布前至少检查一次本地预览。
- `.nojekyll` 保留在根目录，避免 GitHub Pages 对下划线目录等资源做 Jekyll 处理。

## 4. GitHub Pages 设置

仓库首次发布时，在 GitHub 页面设置：

```text
Settings -> Pages
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

设置完成后，推送到 `main` 分支会自动触发重新发布。
