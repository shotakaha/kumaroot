# ウェブページを生成したい（``make html``）

```bash
$ make html
$ make dirhtml
$ make singlehtml
```

ウェブページを生成するときは{command}`make html`を実行します。
生成したファイルは{file}`build/html/`以下に出力されます。
URLはいわゆる``UglyURL``形式で生成されます。

```bash
$ cd $MyPROJECT/docs/
$ make html
$ open build/html/index.html
```

``PrettyURL``形式にしたい場合は{command}``make dirhtml``を使います。

```bash
$ cd $MyPROJECT/docs/
$ make dirhtml
$ open build/dirhtml/index.html
```

:::{hint}

ローカル開発で``make dirhtml``したファイルを開くと、ディレクトリの中身が表示されます。
これは、URLの末尾が``/``になっているときに``index.html``へリダイレクトされるのはサーバーの機能です。
なので、ローカルでビルドする場合は``make html``がオススメです。

:::

HTMLを生成するには、テーマの設定が必要です。
デフォルトは``alabaster``に設定されています。
僕は``sphinx_rtd_theme``をよく使っています。

テーマごとに設定オプションが異なるので、詳細はテーマの公式ドキュメントを参照してください。

```{note}
Sphinxのテーマなので、Sphinxドキュメントで生成されています。
ソースコードを読むだけでもとても参考になります。
```

```{toctree}
---
maxdepth: 1
---
sphinx-html-title
sphinx-html-css
sphinx-html-rtd
sphinx-html-book
```

% あとでsphinx-designのページを作る
% sphinx-html-sd

## リファレンス

- [HTML出力のオプション - Sphinxドキュメント](https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-html-output)
