# C++の構文チェック（リンター）したい（``clang-format``）

```console
$ brew install clang-format
$ clang-format --version
clang-format version 18.1.1
```

## 構文チェック（リンター）したい

```console
$ clang-format ファイル名
```

ファイル名を引数にして、リンターできます。
チェックした結果は標準出力に表示されます。
ファイルの内容は変更されません。

## ファイルを変更したい（``-i``）

```console
$ clang-format -i ファイル名
```

``-i``（inplace）オプションでファイルの内容を上書きできます。

## スタイルを指定したい（``--style``）

```console
$ clang-format --style=スタイル名 ファイル名
$ clang-format --style=LLVM ファイル名
$ clang-format --style=Google ファイル名
```

``--style``オプションで、リンターのスタイルを指定できます。
スタイルのオプションは
``LLVM|GNU|Google|Chromium|Microsoft|Mozilla|Webkit``から選択できます。

## 設定ファイルしたい（``.clang-format``）

```console
// .clang-format から読み込む
$ clang-format --style=file ファイル名
```

``--style=file``で設定ファイル（``.clang-format``）からスタイルを読み込むことができます。

設定ファイルの初期値は``--dump-config``で確認できます。
利用するスタイルを決めたら、次のコマンドで設定ファイルを生成できます。

```console
$ clang-format --style=スタイル名 --dump-config > .clang-format
```

このように作成した``.clang-format``を少しずつカスタマイズするとよいと思います。





