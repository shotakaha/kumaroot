```{eval-rst}
.. index::
    single: CLI; lsd
    single: List directory contents; lsd
    single: Rust Alternatives; lsd
```

# ファイル情報したい（`lsd`）

```console
$ lsd
$ lsd -l ファイル名
$ lsd -a
$ lsd -ltr
```

`lsd`は、ディレクトリの中身を一覧表示するコマンドです。
[ls](./command-ls.md)のRust代替コマンドです。
オプションは`ls`と同じです。

## インストールしたい（`lsd`）

```bash
$ brew install lsd
$ lsd --version
lsd 0.23.1
```

`lsd`はHomebrewでインストールできます。

## 最新ファイルを確認したい

```bash
$ lsd -ltr
$ lsd -ltra
```

:::{seealso}

- [](./command-exa.md)
- [](./command-ls.md)

:::
