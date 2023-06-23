# 和文テキストしたい（``#text``）

```text
#set text(
    font: (
        "HackGen",
        "Noto Sans CJK JP",
    ),
    size: 12pt,
    weight: "regular",
    lang: "ja"

)
```

[text要素のfontオプション](https://typst.app/docs/reference/text/text/#parameters-font)でフォントを変更できます。
フォントは複数設定でき、利用可能なフォントが見つかるまで探してくれます。

日本語で作成すると、よく分からないフォントが適用されるので、必ず全体の設定をしておきましょう。

:::{note}

僕はフォントを``Homebrew``でインストールしています。
とくにフォントパスを設定することなく使えています。

:::

## もっとテキストしたい

```{toctree}
typst-text-font
typst-text-color
```
