# ファイルを表示したい（``bat``）

```console
$ brew install bat
$ bat ファイル名
$ bat ファイル名1 ファイル名2
```

``cat``のRust代替コマンドです。
複数のファイルを一括して表示できます。

## シンタックスを変更したい（``--language``）

```console
$ bat --language cfg 設定ファイル
$ bat 設定ファイル --language cfg
```

シンタックスは、ファイルの拡張子から自動で判断してくれます。
拡張子がないファイルの場合は、``--language 言語名``で指定できます。

```console
$ bat --list-languages
```

利用できる言語名は``--list-languages``で確認できます。

## シンタックスの配色を変更したい（``--theme``）

```console
$ bat --theme ansi ファイル名
$ bat ファイル名 --theme ansi
```

``--theme 配色名``でファイルの内容の配色を変更できます。

```console
$ bat --list-themes
```

利用できる配色は``--list-themes``で確認できます。
