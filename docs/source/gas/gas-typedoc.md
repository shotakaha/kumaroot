# APIドキュメントしたい（`typedoc`）

```console
$ npm install --save-dev typedoc
$ npx typedoc
```

`TypeDoc`は、TypeScriptのソースコードに書かれたコメントを
使ってAPIドキュメントを生成するツールです。
TSDoc形式とJSDoc形式に対応しています。
デフォルトではHTML形式のドキュメントが生成され、
これだけでブラウザで閲覧できるAPIリファレンスとして完結します。

:::{note}

TSDoc形式はTypeScriptの中にドキュメントを記述するための標準的な仕様です。
Microsoftが中心となって開発し、現在はオープンソースとして管理されています。

TypeScript自体の標準機能ではないですが、
TypeDocと組み合わせてAPIドキュメントを生成するのが、
デファクトスタンダードになっています。

:::

## 設定したい（`typedoc.json`）

```json
{
    "entryPoints": ["src/index.ts"],
    "out": "docs/api",
    "excludePrivate": true,
    "excludeProtected": true,
    "excludeExternals": true,
    "excludeInternal": true
}
```

設定ファイルは`typedoc.json`です。
エントリーポイント（`entryPoints`）と出力先（`out`）を指定すればOKです。

`excludePrivate`・`excludeProtected`・`excludeExternals`・`excludeInternal`は、
外部に公開したくないメンバー（`private`/`protected`や`@internal`が付いたもの）を
出力から除外するオプションです。
公開APIだけをドキュメント化したい場合に指定します。

その他のオプションはお好みで設定してください。

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "scripts": {
        "docs:api": "typedoc",
        "...": "..."
    }
}
```

```console
$ npm run docs:api
```

`npm scripts`に`docs:api`を登録しておくと、
`npx typedoc`を直接打たなくても`npm run docs:api`だけで実行できます。
他のビルドタスク（`build`や`bundle`）と並べて管理しやすくなります。

## ホットリロードしたい

```console
$ npx typedoc --watch
```

`--watch`オプションでホットリロードできます。
ドキュメントを整理しているときに、自動で再生成してくれるので便利です。

## Markdownで出力したい（`typedoc-plugin-markdown`）

ここから先はオプションです。
TypeDoc単体で完結させたい場合は、ここまでの設定で十分です。

```console
$ npm install --save-dev typedoc-plugin-markdown
```

```json
{
    "entryPoints": ["src/index.ts"],
    "out": "docs/api",
    "plugin": ["typedoc-plugin-markdown"],
    "excludePrivate": true,
    "excludeProtected": true,
    "excludeExternals": true,
    "excludeInternal": true,
    "disableSources": true,
    "readme": "none",
    "hideBreadcrumbs": true,
    "hideGenerator": true
}
```

`TypeDoc`が生成するファイルはデフォルトでHTML形式ですが、
`plugin`に`typedoc-plugin-markdown`を追加すると、Markdown形式で生成できます。

`disableSources`は、各項目にソースファイルへのリンクを付けないオプションです。
`hideGenerator`は、生成されたページ末尾のTypeDocへのリンクを非表示にします。
どちらも、他のツールで作ったドキュメントサイトに違和感なく溶け込ませたいときに便利です。

:::{hint}

Markdown形式で出力しておくと、Sphinx（本サイト）やMkDocs、
Python製の[Zensical](../zensical/zensical-usage.md)のような、
TypeScript以外のドキュメントツールにもそのまま取り込めます。
API部分だけTypeDocに任せ、それ以外のドキュメント本体は
好きなツールで書く、という構成にできます。

:::

## ドキュメントサイトに組み込みたい

`typedoc-plugin-markdown`で出力すると、
`out`で指定したディレクトリ（例：`docs/api/`）に
`README.md`（インデックス）と、
`classes/`・`functions/`・`type-aliases/`などのサブディレクトリが生成されます。

```console
$ npx typedoc
$ ls docs/api
README.md  classes/  functions/  interfaces/  type-aliases/  variables/
```

あとは、Sphinx（本サイト）やMkDocs、Zensicalなど、
使っているドキュメントツールのナビゲーション設定に
`docs/api/README.md`を登録すれば、
TypeDocが生成したAPIリファレンスをドキュメントサイトの一部として組み込めます。

:::{hint}

`out`をドキュメントツールのソースディレクトリ配下（例：`docs/api`）に指定しておくと、
`npx typedoc`を実行するだけでドキュメントサイトのビルド対象にそのまま含められます。

:::

## リファレンス

- [TypeDoc](https://typedoc.org/)
- [typedoc-plugin-markdown](https://typedoc-plugin-markdown.org/docs)
- [TSDoc](https://tsdoc.org/)
