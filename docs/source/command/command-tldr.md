# tldr

``man``ページやコマンドのヘルプをさっと確認するためのコマンドです。
``TL;DR``（Too Long; Don't Read）という英語圏のミームをもじったコマンド名です。

ほぼすべてのコマンドの使い方は{command}`man`コマンドで確認できますが、
詳細に書かれているため、目的にあった使い方をさっと調べるのはなかなかコツが必要です。
``tldr``は、そこから用例を抜粋して教えてくれます。
すぐに使い方を知りたい場合にとても重宝しています。


```{note}
``TL;DR``は
開発者側は "Too Long; Don't Read"（ドキュメントの肝はここだよ！）、
ユーザー側は"Too Long; Didn't Read"（簡単に説明してよ！）
という意味で使うことができるみたいです。
```

## インストール

{command}`brew`を使ってインストールします。

```bash
brew install tealdeer
```

## 使い方

```bash
tldr コマンド名
```

``tldr``自身の使い方も{command}`tldr`コマンドで確認できます。


```bash
tldr tldr
```

## リポジトリ

- https://github.com/dbrgn/tealdeer
