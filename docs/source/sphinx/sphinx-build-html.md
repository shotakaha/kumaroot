# HTMLしたい（``make html``）

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

## PrettyURLしたい（``make dirhtml``）

```bash
$ cd $MyPROJECT/docs/
$ make dirhtml
$ open build/dirhtml/index.html
```

``PrettyURL``形式にしたい場合は{command}``make dirhtml``を使います。

:::{hint}

ローカル開発で``make dirhtml``したファイルを開くと、ディレクトリの中身が表示されます。
これは、URLの末尾が``/``になっているときに``index.html``へリダイレクトされるのはサーバーの機能です。
なので、ローカルでビルドする場合は``make html``がオススメです。

## リファレンス

[HTML出力のオプション - Sphinxドキュメント](https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-html-output)
: ウェブページを生成するときのオプションを確認するときに参照します。頭から読んでもあまり参考にならず、「〇〇したいから設定ないかなぁ」と逆引きする使い方がよいと思います。
