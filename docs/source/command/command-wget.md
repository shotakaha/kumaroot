# ダウンロードしたい（`wget`）

```console
$ wget URL
```

`wget`は、指定したURLのコンテンツをダウンロードするコマンドです。

:::{seealso}

- [](./command-curl.md)
- [](./command-httpie.md)
- [](./command-xh.md)

:::

## インストールしたい（`wget`）

```console
$ brew install wget
$ wget --version
GNU Wget 1.25.0 built on darwin23.6.0.
```

`wget`はHomebrewでインストールできます。

## ファイル名を指定したい（`-O` / `--output-document`）

```console
$ wget -O ファイル名 URL
$ wget --output-document ファイル名 URL
```

`--output-document`（`-O`）で、任意のファイル名で保存できます。
