# xargs

あるコマンドの実行結果に対して、さらにコマンド操作をしたい場合に使うコマンドです。
ただのパイプとちょっと違うのですが、これ以上、説明できません。

```bash
find | xargs grep 検索文字列
```

## ファイルのパーミッションを一括変更したい

```bash
$ find . -type f | xargs chmod 664
$ find . -type d | xargs chmod 775
```

``find``コマンドと``chmod``コマンドを組み合わせて、ファイルのパーミッションを一括して変更できる。
``find . -type f -name "*.html"``とすれば、HTMLファイルだけに限定することもできる。
