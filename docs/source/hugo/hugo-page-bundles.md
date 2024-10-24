# コンテンツ管理したい

```txt
プロジェクト/
├── archetypes
│   └── default.md
├── config          <-- サイト設定用
│   ├── _default
│   │   ├── hugo.toml
│   │   ├── languages.en.toml
│   │   ├── languages.ja.toml
│   │   ├── menus.en.toml
│   │   ├── menus.ja.toml
│   │   └── params.toml
│   └── production     <-- プロダクション用の設定
│       └── hugo.toml
├── content         <-- コンテンツ用
│   ├── _index.ja.md
│   ├── about
│   │   ├── _index.en.md
│   │   ├── _index.ja.md
│   ├── posts
│   │   ├── _index.ja.md
│   │   ├── 2020
│   │   ├── 2021
│   │   ├── 2022
│   │   ├── 2023
│   │   └── 2024
├── data            <-- データテンプレート用
│   └── authors
│       └── first_last.json
├── layouts         <-- レイアウト用
│   └── shortcodes
├── static          <-- 静的ファイル
│   ├── favicon.ico
│   └── favicons
│       ├── android-chrome-192x192.png
│       ├── android-chrome-512x512.png
│       ├── apple-touch-icon.png
│       ├── favicon-16x16.png
│       ├── favicon-32x32.png
│       ├── favicon.ico
│       └── site.webmanifest
├── assets          <-- アセット用
│   ├── background.jpg
│   ├── featured.jpg
│   └── logo
│       └── logo.png
│
├── themes
│    └── theme_name    <-- git submoduleで追加したテーマ
│
├── resources           <-- ビルド時に生成（キャッシュ）
│   └── _gen
└── public              <-- ビルド時に生成
```

Hugoの基本的なディレクトリ構造です。
それぞれのディレクトリの用途は以下の通りです。

1. `config` : サイト設定用
2. `content` : コンテンツ用
3. `layouts` : レイアウト用
4. `themes` : テーマ用
5. `assets` : アセット用
6. `static` : 静的ファイル用
7. `archetypes` : コンテンツのテンプレート用
8. `data` : データテンプレート用（JSON形式）
9. `public` : 公開用（ビルド時に自動生成）
10. `resources` : アセットのキャッシュ用（ビルド時に自動生成）

:::{caution}

ディレクトリ構造はテーマの機能にも依存します。
テーマ間の互換性はとくに保証されていないので、ディレクトリ構成を検討する前に、テーマを決めるほうがよいと思います。

:::

Hugo 0.32から[Page Bundles機能](https://gohugo.io/content-management/page-bundles/)が追加され、
``Leaf Bundle``と``Branch Bundle``を使ってコンテンツ構造とメディア管理を設計できるようになりました。

ロゴ画像など、サイト全体に共通するファイルは``/static/``に配置すればよいですが、
ブログ記事のカバー画像は、その記事の周辺に配置したほうが管理の観点から便利です。
そんな運用を可能にしてくれる機能です。

## Leaf Bundle（`index.md` / `single.html`）

```console
/content/
 |--- about/
 |     |--- index.md
 |     |--- cover.jpg
 |     |--- heading1.md
 |     |--- heading2.md
 |     |--- heading3.md
 |
 |--- section1/
       |--- subsection1/
       |     |--- index.md
       |     |--- cover.jpg
       |     |--- heading1.md
       |
       |--- subsection2/
             |--- index.md
             |--- cover.jpg
             |--- heading1.md
             |--- heading2.md
```

`index.md`を作成します。
ページテンプレート（``single.html``）が適用されます。
同じディレクトリの`.md`ファイルも`index.html`の中に取り込まれます。

## Branch Bundle（`_index.md` / `list.html`）

```console
/content/
 |--- about/
       |--- _index.md
       |--- cover.jpg
```

`_index.md`を作成します。
リストテンプレート（``list.html``）が適用されます。
同じディレクトリの`.md`ファイルは単体ページとして`index.html`にリスト化されます。

## リファレンス

- [Directory Structure](https://gohugo.io/getting-started/directory-structure/)
- [Page Bundles](https://gohugo.io/content-management/page-bundles/)
