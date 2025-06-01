# APIドキュメントしたい（`typedoc`）

```console
$ npm install --save-dev typedoc
$ npx typedoc
```

`TypeDoc`は、TypeScriptのソースコードに書かれたコメントを
使ってAPIドキュメントを生成するツールです。
TSDoc形式とJSDoc形式に対応しています。

:::{note}

TSDoc形式はTypeScriptの中にドキュメントを記述するための標準的な仕様です。
Microsoftが中心となって開発し、現在はオープンソースとして管理されています。

TypeScript自体の標準機能ではないですが、
TypeDocと組み合わせてAPIドキュメントを生成するのが、
デファクトスタンダードになっています。

:::

## Markdownしたい（`typedoc-plugin-markdown`）

```console
$ npm install --save-dev typedoc-plugin-markdown
```

`TypeDoc`が生成するファイルはHTML形式です。
Markdown形式で生成するためには`typedoc-plugin-markdown`プラグインが必要です。

## 設定したい（`typedoc.json`）

```json
{
    "entryPoints": ["src/index.ts"],
    "out": "docs/api",
    "plugin": ["typedoc-plugin-markdown"],
    "excludePrivate": true,
    "excludeProtected": true,
    "excludeExternals": true,
    "readme": "none",
    "hideBreadcrumbs": true,
}
```

設定ファイルは`typedoc.json`です。
エントリーポイント（`entryPoints`）、
出力先（`out`）、
利用するプラグイン（`plugin`）
を指定すればOKです。
その他のオプションはお好みで設定してください。

## ホットリロードしたい

```console
$ npx typedoc --watch
```

`--watch`オプションでホットリロードできます。
ドキュメントを整理しているときに、自動で再生成してくれるので便利です。

## リファレンス

- [TypeDoc](https://typedoc.org/)
- [typedoc-plugin-markdown](https://typedoc-plugin-markdown.org/docs)
- [TSDoc](https://tsdoc.org/)
