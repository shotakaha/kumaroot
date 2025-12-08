# テーマしたい（`theme`）

```yaml
theme:
  name: mkdocs  # or readthedocs
  language: ja
```

`mkdocs.yml` の `theme` セクションでドキュメントサイトの外観を設定できます。

## 標準テーマしたい（`mkdocs`）

```yaml
theme:
  name: mkdocs
```

`mkdocs`はデフォルトのテーマ名です。
Bootstrapをベースにした設計で、MkDocsのほぼすべての機能をサポートしています。シンプルで軽量なテーマです。

## Read The Docsしたい（`readthedocs`）

```yaml
theme:
  name: readthedocs
```

`readthedocs`はRead the Docsサイトのデフォルトテーマと同じデザインです。
サイドバーナビゲーションが特徴で、より限定的な機能セットです。

## 言語を設定したい

```yaml
theme:
  name: mkdocs
  language: ja
```

`language` キーで表示言語を指定できます。
`ja`で日本語、`en`で英語、その他17以上の言語に対応しています。

## パレットしたい

```yaml
theme:
  name: mkdocs
  palette:
    color_mode: light  # light, dark, auto
    user_color_mode_toggle: true
    nav_style: primary  # primary, dark, light
```

`theme.palette`セクションで、サイト全体の色を設定できます。
設定できる項目はテーマによって異なります。

**paletteの標準オプション：**

- `color_mode`: カラーモード（`light`、`dark`、`auto`）
- `user_color_mode_toggle`: ユーザーがカラーモードを切り替え可能にする（デフォルト: false）
- `nav_style`: ナビゲーションバーのスタイル（`primary`、`dark`、`light`）

## features（機能）を有効にしたい

### mkdocs テーマで利用可能な機能

```yaml
theme:
  name: mkdocs
  features:
    - code.highlight.js
    - search.suggest
    - search.share
```

**標準で利用可能な機能：**

- `code.highlight.js` - highlight.jsによるソースコードのシンタックスハイライト
- `search.suggest` - 検索候補の表示
- `search.share` - 検索結果の共有機能
- `nav.instant` - ページ遷移時のプリロード（読み込み速度向上）
- `toc.integrate` - 目次をサイドバーに統合

## ロゴを設定したい（`theme.logo`）

```yaml
theme:
  name: mkdocs
  logo: img/logo.png
  favicon: img/favicon.ico
```

`theme.logo`キーでロゴ画像を設定できます。
ロゴ画像はナビゲーションバーの左上に表示されます。

`theme.favicon`キーでファビコンを設定できます。
ファビコンはブラウザタブに表示されます。

## フォントを設定したい（`theme.font`）

```yaml
theme:
  name: mkdocs
  font:
    text: Noto Sans JP
    code: Source Code Pro
```

`theme.font`セクションで表示フォントを指定できます。
指定したフォントがインストールされていることが前提です。

## ナビゲーション深さを設定したい（`theme.nav_depth`）

```yaml
theme:
  name: mkdocs
  nav_depth: 3  # デフォルト: 2
```

`theme.nav_depth`でナビゲーションで表示する見出しの深さを設定できます。
`mkdocs`は最大2レベル、
`readthedocs`は最大4レベルです。

## リファレンス

- [MkDocs 公式ドキュメント - Configuration](https://www.mkdocs.org/user-guide/configuration/)
- [MkDocs テーマの選択](https://www.mkdocs.org/user-guide/choosing-your-theme/)
- [MkDocs テーマのカスタマイズ](https://www.mkdocs.org/user-guide/customizing-your-theme/)
