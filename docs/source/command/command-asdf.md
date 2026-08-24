# ランタイム管理したい（`asdf`）

```console
$ asdf
```

`asdf`は、開発環境で使うランタイム（実行環境）を切り替えるコマンドです。
Read the Docsのビルド手順で、Pythonのバージョン指定に使われていたのを見て知りました。

## インストールしたい（`asdf`）

```console
$ brew install asdf
```

`asdf`はHomebrewでインストールできます。

## ランタイムを切り替えたい（`asdf global`）

```console
$ asdf global python 3.12.13
```

`asdf global`で、システム全体のランタイムを指定できます。
上記は、Read the Docsのビルド手順で実行されているコマンドです。

:::{note}

`asdf` v0.15以降では`global`/`local`/`shell`コマンドが廃止され、`asdf set -u python 3.12.13`（グローバル）／`asdf set python 3.12.13`（ローカル）に統一されています。

:::

## リファレンス

- [asdf](https://asdf-vm.com/)
- [asdf-python](https://github.com/asdf-community/asdf-python)
