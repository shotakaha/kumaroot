# アクセス解析したい（`goaccess`）

```console
$ goaccess --log-format COMMON ログファイル
$ goaccess --log-format COMMON ログファイル1 ログファイル2
$ goaccess --log-format COMMON ログファイル -o 出力ファイル名.html
```

`goaccess`は、ウェブサイトのアクセスログを解析できるコマンドです。
理屈はわからないのですが、めちゃくちゃ高速です。

## インストールしたい（`goaccess`）

```console
$ brew install goaccess
$ goaccess --version
GoAccess - 1.9.1.
```

## ログ形式したい（`--log-format`）

```console
$ goaccess --log-format COMMON ログファイル
$ goaccess --log-format COMBINED ログファイル
```

`--log-format`でログで形式を指定できます。
ログファイルに適した形式を選択します。

## ファイル出力したい（`-o` / `--output`）

```console
$ goaccess --log-format COMMON ログファイル --output 出力ファイル名.csv
$ goaccess --log-format COMMON ログファイル --output 出力ファイル名.json
$ goaccess --log-format COMMON ログファイル --output 出力ファイル名.html
$ open 出力ファイル名.html
```

`--output`（`-o`）で、集計結果をファイルに出力できます。
ファイル名もしくは拡張子で出力形式を指定できます。
出力形式は`[csv|json|html]`が使えます。

ダッシュボードで確認したい場合はHTMLが便利です。
自身で可視化する場合はJSON形式が便利かもしれません。
（CSV形式はPandasで読み込むのがちょっと大変そうです）

## ダイアログ設定（`-c` / `--config-dialog`）

```console
$ goaccess -c ログファイル
$ goaccess -c ssl_access_log
$ goaccess -c access_log
```

`--config-dialog`（`-c`）で、ダイアログ形式でログフォーマットを選択できます。
ログ形式がわからない場合に有効です。

矢印キーでカーソルを移動し、`SPC`ーで選択トグル、`Enter`で決定します。
ログファイルのフォーマットと一致していると、ログがパースされ、アクセス解析の結果が表示されます。
選択したフォーマットでない場合、エラーが表示されます。
`q`でダイアログを一度閉じたあと、別のフォーマットを選択できます。
