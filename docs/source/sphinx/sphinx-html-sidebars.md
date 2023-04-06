# サイドバーしたい（``html_sidebars``）

```python
# conf.py
html_sidebars = {
    # "ドキュメント名": ["テンプレート名", "テンプレート名", ...],
    "**": ["localtoc.html", "relations.html", "sourcelink.html", "searchbox.html"],
    "using/windows": ["windowssidebar.html", "searchbox.html"],
}
```

``html_sidebars``を使って、サイドバーに表示する内容をカスタマイズできます。
**ドキュメント名**と**テンプレート名**が対応した辞書型で定義します。
ドキュメント名は``*（glob-style pattern）``を使ってマッチできます。
テンプレート名は``str型``もしくは``list型``で書きます。

テーマごとによってサイドバーのデフォルト値は異なります。
テーマによってはサイドバー表示が無効になっている場合もあります。

ビルトインのテーマでは、``localtoc.html``、``relations.html``、``sourcelink.html``、``searchbox.html``が表示されます。
それぞれの表示内容は以下の通りです。

``localtoc.html``
: 現在のドキュメントの目次（見出しのリスト）

``globaltoc.html``
: すべてのドキュメントの目次（見出しのリスト）

``relations.html``
: 前と次のドキュメントへのリンク

``sourcelink.html``
: 現在のドキュメントのソース。``html_show_sourcelink = True``が必要

``searchbox.html``
: （簡易的な）検索ボックス

## サイドバーをカスタマイズしたい

サイドバーの表示内容と順番だけでなく、そのテンプレートをカスタマイズできるはずです。
どこにテンプレートを置けばいいのか、調べています。
（たぶん``_templates``みたいなパスのはず）
