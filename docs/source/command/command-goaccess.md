# アクセス解析したい（``goaccess``）

```console
$ brew install goaccess
$ goaccess --version
GoAccess - 1.9.1.
```

## ログ形式したい（``--log-format``）

```console
$ goaccess --log-format COMMON ログファイル
$ goaccess --log-format COMBINED ログファイル
```

``--log-format``でログで形式を指定できます。
ログファイルに適した形式を選択します。

## ファイル出力したい（``-o``）

```console
$ goaccess --log-format COMMON ログファイル -o 出力ファイル名.csv
$ goaccess --log-format COMMON ログファイル -o 出力ファイル名.json
$ goaccess --log-format COMMON ログファイル -o 出力ファイル名.html
$ open 出力ファイル名.html
```

``-o 出力ファイル名.[csv|json|html]``で集計結果をファイルに出力できます。
ダッシュボードで確認したい場合はHTMLが便利です。
自身で可視化する場合はJSON形式が便利かもしれません。
（CSV形式はPandasで読み込むのがちょっと大変そうです）

## ダイアログ設定（``-c``）

```console
$ goaccess -c ログファイル
$ goaccess -c ssl_access_log
$ goaccess -c access_log
```

``-c``オプションを使って、ダイアログ形式でログフォーマットを選択できます。
ログ形式がわからない場合に有効です。

矢印キーでカーソルを移動し、``SPC``ーで選択トグル、``Enter``で決定します。
ログファイルのフォーマットと一致していると、ログがパースされ、アクセス解析の結果が表示されます。
選択したフォーマットでない場合、エラーが表示されます。
``q``でダイアログを一度閉じたあと、別のフォーマットを選択できます。
