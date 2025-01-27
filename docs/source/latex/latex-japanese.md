# 日本語LaTeX

TeX／LaTeXの開発はASCII文字を中心にはじまったため、
日本語対応は一筋縄ではいかなかったようで、
先人たちのさまざまな苦労の上に成り立っています。

## 2020年からの話

```console
$ lualatex --help  # ヘルプを表示
$ lualatex hoge    # LuaLaTeXの場合
```

欧文では`pdfLaTeX`を使うのが一般的になった感じがしました。
また、和文で`XeLaTeX`や`LuaLaTeX`の利用が広がってきたと思います。
ただし、コンパイル速度の観点から
`(u)pLaTeX + dvipdfmx`を使う人も周りに多かった印象です。

```console
$ latexmk main.tex
```

この頃から`latexmk`コマンドを使うようになりました。
このコマンド自体はずいぶん前からあるようですが、
全然知りませんでした。

## 2015年ころの話

```{warning}
【2021-01-18に追記】
(u)pLaTeXを使うのは少し昔の話。
2020年からはLuaLaTeXを使うのをオススメします。
```

```console
$ platex hoge.tex
$ dvipdfmx hoge.dvi
```

長い間、和文LaTeXの作成には
`(u)pLaTeX`と
`dvipdfmx`を使うのが定番でした。

まず`(u)platex` コマンドでLaTeXファイルからDVIファイルを作成し、
次に`dvipdfmx` コマンドでDVIファイルをPDFファイルに変換する、
という二段構えの処理でPDFを生成します。

```console
// ヘルプを表示
$ ptex2pdf -h

// platex + dvipdfmx で処理
$ ptex2pdf -l hoge

// uplatex + dvipdfmx で処理
$ ptex2pdf -l -u hoge
```

この一連の処理をいい感じにまとめてくれたのが
`ptex2pdf`コマンドです。
このコマンドは、MacTeX（もしくはTeXLive）と一緒にインストールされます。

```console
$ which ptex2pdf
/Library/TeX/texbin/ptex2pdf

$ less /Library/TeX/texbin/ptex2pdf
```

`ptex2pdf`自体は、Luaスクリプトなので、気になる人は中を見てみるとよいでしょう。
