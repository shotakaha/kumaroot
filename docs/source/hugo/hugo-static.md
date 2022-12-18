# 静的ファイルを置きたい

```toml
staticDir = ["static"]
```

静的ファイルを配置するディレクトリは``staticDir``で変更できます。
デフォルトは``/static/``です。
基本的に変更する必要はないと思っています。

Hugo 0.32からは``Page Bundles``機能が追加され、``Leaf Bundle``と``Branch Bundle``でコンテンツ構造を設計できるようになりました。
詳細は[バンドルの使い方](./hugo-bundles.md)に整理しました。

## リファレンス

- [Static Files](https://gohugo.io/content-management/static-files/)
- [Page Bundles](https://gohugo.io/content-management/page-bundles/)
