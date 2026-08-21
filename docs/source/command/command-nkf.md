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

## エンコーディングを調べたい（`--guess` / `-g`）

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

## Shift_JISに変換したい（`-s`）

```console
$ nkf -s path/to/file.txt
```

`-s`オプションで、ファイルをShift_JISに変換します。
`-w`（UTF-8への変換）とは逆方向で、古いWindows環境向けにファイルを渡すときに使います。

## 改行コードを変換したい（`-L`）

```console
// LF（Unix/macOS）に統一
$ nkf -Lu path/to/file.txt

// CRLF（Windows）に統一
$ nkf -Lw path/to/file.txt

// CR（旧Mac OS）に統一
$ nkf -Lm path/to/file.txt
```

`-L`オプションで、改行コードを変換できます。
Windowsで作成したファイルはCRLFになっていることが多いので、
`-Lu`でLFに統一しておくと、Unix系のツールと相性がよくなります。

:::{note}

改行コードがOSによって異なるのは、タイプライターやテレタイプ端末の動作に由来する歴史的経緯があります。
本来「CR（Carriage Return、復帰）」は印字ヘッドを行頭に戻す動作、「LF（Line Feed、改行）」は紙送りで次の行に進める動作で、
別々の物理動作でした。

- CR（`\r`）: 旧Mac OS（〜OS 9）が採用。復帰の動作のみ
- LF（`\n`）: Unix系OSが、復帰と改行をまとめて簡略化
- CRLF（`\r\n`）: DOS/Windowsが、テレタイプ由来の2動作をそのまま踏襲

:::

## ひらがな・カタカナを変換したい（`--hiragana` / `--katakana`）

```console
// カタカナに変換
$ echo "こんにちは" | nkf --katakana

// ひらがなに変換
$ echo "コンニチハ" | nkf --hiragana
```

`--katakana`でひらがなをカタカナに、`--hiragana`でカタカナをひらがなに変換できます。

## ファイルを上書きしたい（`--overwrite`）

```console
// UTF-8に変換して上書き
$ nkf -w --overwrite path/to/file.txt
```

`--overwrite`オプションで、入力ファイルをそのまま上書きして保存できます。

:::{note}

似たオプションに`--in-place`があります。
`--overwrite`は元ファイルのタイムスタンプを保持しますが、`--in-place`は上書き時にタイムスタンプが更新されます。

:::
