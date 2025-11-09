# ダウンロードしたい（``wget``）

```bash
wget URL
```

``wget``で指定したURLのコンテンツをダウンロードできます。

## インストールしたい（`wget`）

```console
$ brew install wget
$ wget --version
GNU Wget 1.25.0 built on darwin23.6.0.
```

`wget`はHomebrewでインストールできます。

## ファイル名を指定したい（`-O`）

```console
$ wget -O ファイル名 URL
$ wget --output-document ファイル名 URL
```

`-O ファイル名`オプションで、指定したURLを任意のファイル名で保存できます。


:::{seealso}

- [](./command-curl.md)
- [](./command-httpie.md)
- [](./command-xh.md)

:::
