# 設定ファイルしたい（``latexmkrc``）

:::{literalinclude} ../_static/latex/templates/lualatex-jlreq/latexmkrc
:::

[latexmk](./latex-latexmk.md) のオプションは、すべて{file}``latexmkrc``に書いておくことができます。
LaTeX文書は繰り返しコンパイルすることが多いです。
毎回指定するのは面倒なので、一番はじめに作成しておきましょう。

## 複数ファイルしたい（``@default_files``）

```text
@default_files = ("ファイル名1", "ファイル名2");
```

``@default_files``で設定した複数の文書を一括でタイプセットできます。
ただし、ライブプレビューの設定とは一緒に使えません。

## ライブプレビューしたい（``preview_continuous_mode``）

```text
## latexmkrc
$preview_continuous_mode = 1;
$pvc_timeout = 1;
$pvc_timeout_mins = 10;  # 30min; default
$sleep_time = 60; # in sec
```

{file}`latexmkrc`で設定する場合は``$preview_continuous_mode = 1``に設定します。
ライブプレビューをしたまま忘れてしまうことがあるので、一定時間更新がなかった場合に自動で終了するように``$pvc_timeout = 1``と``$pvc_timeout_mins = 分``も設定しておくとよいと思います。

文書を大量に作成していて、頻繁に更新しているフェーズは``$sleep_time = 秒``を長めに設定しておくとよいです。
こまめに保存している最中に、ムダにコンパイルされる回数を減らすことができます。

## 出力先を分けたい

```text
$out_dir = "_build";
$aux_dir = "_aux";
```

生成されるPDFファイルや中間ファイルを、別のディレクトリに保存できます。
ソースファイルと別ディレクトリにすることで、文書の管理が楽になると思います。
また、この設定は``latexmk -c / -C``するときにも便利です。
