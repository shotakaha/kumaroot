```{eval-rst}
.. index::
    single: CLI; tldr
    single: ヘルプしたい; fd
    single: Rust Alternatives; tldr
```

# ヘルプしたい（`tldr`）

```console
// tldr [コマンド名]
$ tldr git
$ tldr uv

// tldr自身も確認できる
$ tldr tldr
```

`tldr`は、コマンドの典型的な使い方を簡単に確認できるコマンドです。
"Too Long; Don't Read"という英語圏のミームをもじったコマンド名です。

ほぼすべてのコマンドの使い方は{command}`man`コマンドで確認できますが、
詳細に書かれているため、目的にあった使い方をさっと調べるのはなかなかコツが必要です。
`tldr`は、そこから用例を抜粋して教えてくれます。
すぐに使い方を知りたい場合にとても重宝しています。

```{note}
`TL;DR`は
開発者側は "Too Long; Don't Read"（ドキュメントの肝はここだよ！）、
ユーザー側は"Too Long; Didn't Read"（簡単に説明してよ！）
という意味で使うことができるみたいです。
```

## インストールしたい（`tldr`）

```console
$ brew install tealdeer
$ tldr --version
tealdeer 1.8.1
```

`tldr`はHomebrewでインストールできます。
フォーミュラ名は`tealdeer`です。

## キャッシュを更新したい（`--update`）

```console
$ tldr --update
$ tldr -u
```

`--update`オプションで、キャッシュを更新できます。
初回実行時とキャッシュが古くなっている場合は、更新を促す警告（warning）が表示されるので、更新しておくとよいです。

## 設定ファイルを作成したい

```console
$ tldr --seed-config
Successfully created seed config file here: ~/Library/Application Support/tealdeer/config.toml
```

`--seed-config`オプションで、設定ファイルを作成できます。
デフォルトでは、`~/Library/Application Support/tealdeer/config.toml`に作成されます。

`[updates]`セクションでキャッシュ更新の自動化を設定できます。

## リファレンス

- [tealdeer - GitHub](https://github.com/dbrgn/tealdeer)
- [tldr-pages - GitHub](https://github.com/tldr-pages/tldr)
