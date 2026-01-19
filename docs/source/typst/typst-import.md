# インポートしたい（`#import`）

```typst
#import "ファイルパス"
```

`#import`文でファイルをモジュールとして読み込むことができます。
ドキュネントの全体設定などを専用のファイルに保存して、ファイル内容を整理できます。

## ローカルパッケージを読み込みたい

```typst
#import "@local/パッケージ名:バージョン": *

// 個人開発中のパッケージ
#import "@local/inkstep:0.5.1" as inkstep
#import "@local/deckdocs:0.8.0": deckdocs, deck, docs, section
```

自作したパッケージを
`~/library/Application Support/typst/packages/local/`（macOSの場合）に配置すると、
`"@local/パッケージ名"`でインポートできます。

:::{note}

ローカルパスへの配置（コピー）は
Typst CLIでは対応していないため
`tyler`を使っています。

- [](./typst-tyler.md)

:::

:::{hint}

上記サンプルで読み込んでいるパッケージは、
個人開発中の以下のパッケージです。

- [InkStep](https://gitlab.com/qumasan/inkstep) -- A Document-Embedded Logging library for Typst documents
- [DeckDocs](https://gitlab.com/qumasan/deckdocs) -- Provides logical switcher to generate both "Decks" (16:9 presentation slides) and "Docs" (A4 documentation) from a single Typst source

:::

## パッケージを読み込みたい

```typst
#import "@preview/zebraw:0.6.1": *
```

[Typst Universe](https://typst.app/universe/)で公開されているパッケージも`#import`文で読み込むことができます。
上記サンプルは、コードブロックをいいい感に表示してくれる`zebraw`パッケージをインポートしています。
最新バージョンや、具体的な使い方はそれぞれのパッケージのREADMEを参照してください。

:::{note}

パッケージ管理システムは2023年6月リリースの[v0.6.0](https://github.com/typst/typst/releases/tag/v0.6.0)で導入されました。

:::
