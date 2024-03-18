# アクセス解析したい（``goaccess``）

```console
$ brew install goaccess
$ goaccess --version
GoAccess - 1.9.1.
```

## ダイアログ設定（``-c``）

```console
$ goaccess -c ログファイル
$ goaccess -c ssl_access_log
$ goaccess -c access_log
```

``-c``オプションを使って、ダイアログ形式でログフォーマットを選択できます。
矢印キーでカーソルを移動し、``SPC``ーで選択トグル、``Enter``で決定します。

ログファイルのフォーマットと一致していると、ログがパースされ、アクセス解析の結果が表示されます。

選択したフォーマットでない場合、エラーが表示されます。
``q``でダイアログを一度閉じたあと、別のフォーマットを選択できます。
