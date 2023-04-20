# Goole Apps Script の使い方

``Google Apps Script (GAS)``はGoogleのサービスを自動化させるためのスクリプト言語です。
現在は[V8ランタイムに対応（2020年3月17日）](https://cloud.google.com/blog/ja/products/g-suite/data-processing-just-got-easier-apps-scripts-new-v8-runtime)していて、モダンなJavaScript環境のひとつとして使うことができます。

GASの情報を検索すると、新しい書き方と古い書き方が混ぜこぜで書いてあるコードがたくさんヒットします。
このドキュメントでは、GASをゼロから作成する方法というより、ウェブに落ちているコードを、どのように読み替えるかを中心に整理しようと思います。

```{toctree}
---
maxdepth: 1
---
gas-variables.md
gas-class.md
gas-date.md
gas-spreadsheet.md
gas-document.md
gas-gmail.md
gas-groups.md
```

## リファレンス

- [Drive Service](https://developers.google.com/apps-script/reference/drive)
- [Forms Service](https://developers.google.com/apps-script/reference/forms)
- [Gmail Service](https://developers.google.com/apps-script/reference/gmail)
- [Spreadsheet Service](https://developers.google.com/apps-script/reference/spreadsheet)
- [Group Service](https://developers.google.com/apps-script/reference/groups)
- [V8 Runtime Overview / Syntax Examples](https://developers.google.com/apps-script/guides/v8-runtime#v8_syntax_examples)
