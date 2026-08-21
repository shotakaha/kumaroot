# エンコーディングを変換したい（`nkf`）

```console
$ nkf -g path/to/file.txt
UTF-8

$ nkf -w --overwrite path/to/file.txt
```

`nkf`は、ファイルのエンコーディングや改行コードを変換するコマンドです。

最近は使うことが少なくなってきましたが、昔のファイルを開く際に役に立つことがあります。
また、Windowsのメモ帳で作成されたテキストファイルは、
Shift JIS になっていることがあるので、
macOSで読むにはUTF-8への変換が必要です。

## インストールしたい（`nkf`）

```console
$ brew install nkf
$ nkf --version
Network Kanji Filter Version 2.1.5 (2018-12-15)
Copyright (C) 1987, FUJITSU LTD. (I.Ichikawa).
Copyright (C) 1996-2018, The nkf Project.
```

`nkf`はHomebrewでインストールできます。

## エンコーディングを調べる（`--guess` / `-g`）

```console
$ nkf --guess path/to/file.txt
$ nkf -g path/to/file.txt
UTF-8
```

`--guess`オプションで、ファイルのエンコーディングを調べることができます。

## UTF-8に変換したい（`-w`）

```console
// 標準出力
$ nkf -w path/to/file.txt

// ファイルにリダイレクト
$ nkf -w path/to/file.txt > path/to/file_utf8.txt
```

`-w`オプションで、ファイルをUTF-8に変換します。
変換した結果は標準出力に表示されます。
リダイレクトしてファイルに保存できます。

## ファイルを上書きしたい（`--overwrite`）

```console
// UTF-8に変換して上書き
$ nkf -w --overwrite path/to/file.txt
```

`--overwrite`オプションで、入力ファイルをそのまま上書きして保存できます。
