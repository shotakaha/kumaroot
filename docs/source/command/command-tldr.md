```{eval-rst}
.. index::
    single: CLI; tldr
    single: ヘルプしたい; fd
    single: Rust Alternatives; tldr
```

# ヘルプしたい（``tldr``）

`man`ページやコマンドのヘルプをさっと確認するためのコマンドです。
`TL;DR`（Too Long; Don't Read）という英語圏のミームをもじったコマンド名です。

ほぼすべてのコマンドの使い方は{command}`man`コマンドで確認できますが、
詳細に書かれているため、目的にあった使い方をさっと調べるのはなかなかコツが必要です。
`tldr`は、そこから用例を抜粋して教えてくれます。
すぐに使い方を知りたい場合にとても重宝しています。

```{note}
``TL;DR``は
開発者側は "Too Long; Don't Read"（ドキュメントの肝はここだよ！）、
ユーザー側は"Too Long; Didn't Read"（簡単に説明してよ！）
という意味で使うことができるみたいです。
```

## インストール

```console
$ brew install tealdeer
```

{command}`brew`を使ってインストールします。

## 使い方

```console
$ tldr コマンド名
```

`tldr`自身の使い方も{command}`tldr`コマンドで確認できます。

```console
$ tldr tldr
```

## キャッシュを更新したい

```console
$ tldr --update
$ tldr -u
```

初回とキャッシュが古くなっている場合は、更新を促す警告（warning）が表示されます。

## 設定ファイルを作成したい

```console
$ tldr --seed-config
Successfully created seed config file here: ~/Library/Application Support/tealdeer/config.toml
```

設定ファイルでキャッシュの更新を自動化できます。

## リポジトリ

-   https://github.com/dbrgn/tealdeer
