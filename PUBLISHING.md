# 发布与维护流程

## 1. 更新已有内容

已有主题固定使用同一个 `slug`。例如本次演示的稳定路径是：

```text
pages/ai-trading-boundary/index.html
```

更新时覆盖这个文件即可，不新增 `v2`、`final`、`fixed` 等重复文件。需要追溯旧版本时查看 Git 历史。

## 2. 上传新内容

以后你可以直接把 HTML 文件发给 Codex，我会：

1. 检查是否有 `/Users/...`、`Downloads/...`、`file://` 等本机路径。
2. 检查外部图片、字体、脚本是否会影响稳定访问。
3. 判断是更新已有页面，还是新建页面。
4. 选择稳定 `slug`。
5. 发布到 `pages/<slug>/index.html`。
6. 更新根目录 `index.html` 和 `site-manifest.json`。
7. 提交并等待 GitHub Pages 生效。

## 3. 稳定性规则

- 页面入口统一命名为 `index.html`。
- URL 中的 `slug` 一旦对外发出，默认不再改名。
- 关键资源优先内嵌，或放在页面目录下的 `assets/`。
- 不使用本机绝对路径。
- `.nojekyll` 保留在根目录，避免 GitHub Pages 进行 Jekyll 处理。
- 每次发布后检查线上链接是否可访问。

## 4. 当前公开链接

```text
https://iwufai-dotcom.github.io/ai-trading-boundary-presentation/
https://iwufai-dotcom.github.io/ai-trading-boundary-presentation/pages/ai-trading-boundary/
```
