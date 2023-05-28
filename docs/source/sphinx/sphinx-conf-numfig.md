# 図表番号したい（``numfig``）

```python
numfig = True

# 図表番号を表示するときのカスタム設定
# フォーマット文字列を辞書型で指定
# デフォルトの設定を書いた後、カスタム設定で上書き
numfig_format = {
    "figure": "Fig. %s",
    "table": "Table %s",
    "code-block": "Listing %s"
}
numfig_format["figure"] = "図 %s"
numfig_format["table"] = "表 %s"
numfig_format["code-block"] = "コード %s"

# 図表番号のスコープ
# 0: 全てのドキュメントで通し番号
# 1: セクション毎に番号を付与（x.1, x.2, x.3, ...）
# 2: サブセクション毎に番号を付与（x.x.1, x.x.2, x.x.3, ...）
# デフォルトは 1
numfig_secnum_depth = 1
```

``numfig``をONにすると、図や表、コードブロックに自動で番号を振ることができます。
また``numref``ロールも使えるようになります。

``numfig_format``を使って、図表番号の表示形式を設定できます。
``%s``は図表番号に置換されます。
デフォルトは英語になっているので、日本語で設定しなおしています。

たくさんの図表を含む文書の場合、図番号はセクションごとに振られているほうが読みやすいかもしれません。
どのように採番するか``numfig_secnum_depth``で設定できます。
