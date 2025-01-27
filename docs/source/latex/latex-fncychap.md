# 章見出しを装飾したい（``fncychap``）

```latex
\usepackage[Sonny]{fncychap}
\usepackage[Lenny]{fncychap}
\usepackage[Glenn]{fncychap}
\usepackage[Conny]{fncychap}
\usepackage[Rejne]{fncychap}
\usepackage[Bjarne]{fncychap}
\usepackage[Bjornstrup]{fncychap}
```

``fncychap``パッケージで章見出しをいい感じに装飾できます。
オプションにテーマ名を指定します。
テーマは``Sonny`` / ``Lenny`` / ``Glenn`` / ``Conny`` / ``Rejne`` / ``Bjarne`` / ``Bjornstrup``があります。

日本語の文書の場合は``Bjornstrup``を選択するとよいと思います。
それ以外のテーマは「第○」と表示されてしまうため、不格好に感じることが多いです。
とくに``Bjarne``は、章番号が「第ONE」「第TWO」のように英語で表記されるため、日本語向きではないと思います。

## リファレンス

- {command}``texdoc fncychap``
