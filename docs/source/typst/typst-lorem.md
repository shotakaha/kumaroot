# ダミーテキストしたい（``lorem``）

```typ
#lorem(単語数)
```

[lorem関数](https://typst.app/docs/reference/text/lorem/)を使ってダミーテキストを生成できます。

## 日本語ダミーテキストしたい（``roremu``）

```typ
#import "@preview/roremu:0.1.0": roremu

#roremu(単語数)

// 公式サンプル
#roremu(8) // 吾輩は猫である。
#roremu(8, offset: 8) // 名前はまだ無い。
#roremu(17, custom-text: "私はその人を常に先生と呼んでいた。")
```

[rorem](https://github.com/typst/packages/tree/main/packages/preview/roremu/)パッケージを使って、日本語のダミーテキストを生成できます。
テキストは夏目漱石の「吾輩は猫である」が元になっています。
``lorem関数``と同じように、生成する単語数を指定します。

``offset``オプションで、テキストの開始位置を変更できます。
``custom-text``オプションで、任意のダミーテキストに変更できます。

:::{seealso}

- [](../latex/latex-bxjalipsum.md)

:::
