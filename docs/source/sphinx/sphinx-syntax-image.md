# 画像したい（``image``）

````md
```{image} 画像のパス
:alt: 代替テキスト
:class: CSSクラス
:width: 画像の横幅（px / %）
:align: 画像の位置（"top" / "middle" / "bottom" / "left" / "center", "right"）
:name: ターゲット名（＝HTMLタグのID属性）
```
````

画像の挿入には``image``ディレクティブを使います。
画像のサイズ（横幅／縦幅）や位置などをオプションで指定できます。
Markdown記法を使う場合に比べて、柔軟に配置できます。

````{seealso}
Markdown形式でも画像を挿入できます。

```md
![](画像のパス)
![代替テキスト](画像のパス)
```

この形式では細かなオプションを指定できません。
````

## キャプションしたい（``figure-md``）

````md
:::{figure-md} ターゲット名
![代替テキスト](画像のパス){.クラス width=画像の幅px}

**Markdown**を使った簡単なキャプション
:::
````

簡単なキャプションを追加するには``figure-md``ディレクティブを使います。
Markdownと同じ記法で画像を挿入できます。

## 複雑なキャプションしたい（``figure``）

````md
```{figure} 画像のパス
:figclass: figureのクラス
:figwidth: figureの幅

画像のキャプションを、
複数行にわたって入力できます。

キャプションにいろいろ追加できます。（しないほうがいいと思いますが）
```
````

複数行にわたるようなキャプションを追加するには``figure``ディレクティブを使います。
``image``ディレクティブのオプションすべてに加えて``figclass``と``figwidth``のオプションを指定できます。

## リファレンス

- [Images and figures - MyST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/images_and_figures.html)
- [Markdown Figures - MYST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/optional.html#syntax-md-figures)
