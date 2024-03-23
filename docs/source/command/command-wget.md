# ダウンロードしたい（``wget``）

```console
$ brew install wget
$ wget --version
GNU Wget 1.24.5 built on darwin22.6.0.
```

```console
$ wget URL
```

``wget``で指定したURLのコンテンツをダウンロードできます。

## ファイル名を指定したい（``-O``）

```console
$ wget --output-document ファイル名 URL
$ wget -O ファイル名 URL
```

:::{seealso}

- [](./command-curl.md)

:::
