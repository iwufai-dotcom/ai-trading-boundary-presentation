# GitHub Pages 发布库

这个仓库用于集中发布 HTML 演示页。根目录 `index.html` 是内容索引，每个演示内容放在独立目录中，保证链接稳定。

## 当前内容

- AI 与人在交易中的效率与边界：`pages/ai-trading-boundary/`

## 管理原则

- 新内容使用新的稳定 `slug`，放到 `pages/<slug>/index.html`。
- 更新已有内容时继续使用原 `slug`，直接覆盖同一路径，避免堆积 `v1/final/fixed` 文件。
- 旧版本由 Git 历史保存，不在网站目录里重复堆放。
- 关键资源随仓库提交，避免依赖本机路径或临时外链。

## GitHub Pages

Pages 源建议设置为：

```text
Settings -> Pages -> Deploy from a branch -> main / root
```

公开访问地址：

```text
https://iwufai-dotcom.github.io/ai-trading-boundary-presentation/
```
