# ファイルを表示したい（`bat`）

```console
$ bat ファイル名
$ bat ファイル名1 ファイル名2
```

`bat`コマンドで、ファイルの内容を表示できます。
複数のファイルを一括して表示できます。

`bat`は`cat`のRust代替コマンドです。

## インストールしたい（`bat`）

```console
$ brew install bat
$ bat --version
bat 0.26.1
```

`bat`はHomebrewでインストールできます。

## 装飾なしにしたい（`--plain` / `-p`）

```console
$ bat --plain ファイル名
$ bat --plain --plain ファイル名

// クリップボードにコピー
$ bat -pp ファイル名 | pbcopy
```

`--plain`（`-p`）で、行番号や罫線などの装飾なしでファイルの内容を表示できます。
コピペしたいときに便利です。
`-p`を2回指定（`-pp`）すると、ページャーも無効になります。

:::{note}

`bat`は、デフォルトで装飾が付いており、読みやすいのが特徴です。
ただし、コピペするときには邪魔です。

:::

## 行番号したい（`--number` / `-n`）

```console
$ bat --number ファイル名
$ bat -n ファイル名
```

`--number`（`-n`）で、行番号だけを表示できます。
`grep`の結果と見比べて、該当行を探したいときに便利です。

## 行範囲したい（`--line-range` / `-r`）

```console
$ bat --line-range 30:40 ファイル名
$ bat -r 30:40 ファイル名
```

`--line-range`（`-r`）で、指定した範囲の行だけを表示できます。
`30:40`で30〜40行目、`:40`で1〜40行目、`40:`で40行目から最後まで、`40`で40行目だけを表示できます。
ログファイルの一部分だけを確認したいときに便利です。

## 差分したい（`--diff` / `-d`）

```console
$ bat --diff ファイル名
$ bat -d ファイル名
$ bat --diff-context 5 ファイル名
```

`--diff`（`-d`）で、Gitのインデックスと比較して変更のある行だけを表示できます。
`--diff-context`オプションで、変更行の前後何行を含めるか指定できます。

## 不可視文字を表示したい（`--show-all` / `-A`）

```console
$ bat --show-all ファイル名
$ bat -A ファイル名
```

`--show-all`（`-A`）で、タブや改行などの不可視文字を表示できます。
バイナリファイルの中身を確認したいときにも使えます。

## 特定の行をハイライトしたい（`--highlight-line` / `-H`）

```console
$ bat --highlight-line 40 ファイル名
$ bat -H 30:40 ファイル名
```

`--highlight-line`（`-H`）で、指定した行の背景色を変えて目立たせることができます。
プレゼンテーションやコードレビューで、注目してほしい行を示したいときに便利です。

## シンタックスを変更したい（`--language`）

```console
$ bat --language cfg 設定ファイル
$ bat 設定ファイル --language cfg
```

シンタックスは、ファイルの拡張子から自動で判断してくれます。
拡張子がないファイルの場合は、`--language 言語名`で指定できます。

```console
$ bat --list-languages
```

利用できる言語名は`--list-languages`で確認できます。

## シンタックスの配色を変更したい（`--theme`）

```console
$ bat --theme ansi ファイル名
$ bat ファイル名 --theme ansi
```

`--theme 配色名`でファイルの内容の配色を変更できます。

```console
$ bat --list-themes
```

利用できる配色は`--list-themes`で確認できます。

## リファレンス

- [bat - GitHub](https://github.com/sharkdp/bat)
