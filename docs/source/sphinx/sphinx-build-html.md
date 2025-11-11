# HTMLしたい（`sphinx-build`）

```console
# -b html: 標準的なHTML出力（UglyURL形式）
$ sphinx-build -b html source build/html

# -b dirhtml: ディレクトリベースのHTML出力（PrettyURL形式）
$ sphinx-build -b dirhtml source build/dirhtml

# -b singlehtml: 単一HTMLファイル出力
$ sphinx-build -b singlehtml source build/singlehtml
```

`sphinx-build`コマンドでHTML形式で出力できます。

## HTMLしたい（`make html`）

```console
$ make html
$ make dirhtml
$ make singlehtml
```

[sphinx-quickstart](./sphinx-quickstart.md)で初期化するとドキュメントには`Makefile`が自動生成されます。
`Makefile`があるディレクトリで`make html`を実行するとHTML形式で出力できます。

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
