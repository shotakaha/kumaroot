# 章見出しを装飾したい（`fncychap`）

```latex
\usepackage[Sonny]{fncychap}
\usepackage[Lenny]{fncychap}
\usepackage[Glenn]{fncychap}
\usepackage[Conny]{fncychap}
\usepackage[Rejne]{fncychap}
\usepackage[Bjarne]{fncychap}
\usepackage[Bjornstrup]{fncychap}
```

`fncychap`パッケージで章見出しをいい感じに装飾できます。
オプションにテーマ名を指定します。
テーマは
`Sonny`、
`Lenny`、
`Glenn`、
`Conny`、
`Rejne`、
`Bjarne`、
`Bjornstrup`があります。

すべて欧文向けに作成されたテーマです。
それぞれの表示スタイルはパッケージのドキュメントにある
サンプルを確認してください（`$ texdoc fncychap`）

この中で`Bjornstrup`だけが、そのまま和文クラスと併用できると思います。
それ以外のテーマは「第○」と表示されてしまうため、不格好に感じました。
とくに`Bjarne`は、章番号が「第ONE」「第TWO」のように英語で表記されるため、
日本語には向かないと思います。
