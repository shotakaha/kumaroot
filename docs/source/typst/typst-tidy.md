# APIドキュメントしたい（`tidy`）

```typst
#import "@preview/tidy:0.4.3"

#let docs = tidy.parse-module(read("relative/path/to/source.typ"))
#tidy.show-module(docs, style: tidy.styles.default)
```

`tidy`パッケージで、Typstのソースコードをパースして、
docstringからAPIドキュメントを生成できます。

## 複数モジュールをドキュメント化したい

```typst
#import "@preview/tidy:0.4.3"

/// 表示したいモジュールを定義
#let sources = (
  "module1.typ": read("relative/path/to/module1.typ"),
  "module2.typ": read("relative/path/to/module2.typ"),
  "module3.typ": read("relative/path/to/module3.typ"),
)

/// ドキュメントの設定
#title("API Docs")
#outline()
#pagebreak()

/// APIドキュメントを生成
#for (name, content) in sources {
  pagebreak(weak: true)
  heading(level: 2)[#name]
  let docs = tidy.parse-module(content)
  tidy.show-module(docs, style: tidy.styles.default, title: name)
}
```

`tidy.show-module`関数は、単一のモジュールをドキュメント化するための関数です。
複数のモジュールで構成したライブラリをドキュメント化したい場合は、
それぞれのファイルを読み込んで処理する必要があります。

上記のサンプルでは、`sources`という変数名で、
モジュールのファイル名と`read`関数で読み込んだ内容をマップにして定義しています。
あとは、`for`ループでモジュールごとにドキュメントを生成していくだけです。
ファイル名は見出しとして表示しています。
