# Google Apps Script の使い方

``Google Apps Script (GAS)``はGoogleのサービスを自動化させるためのスクリプト言語です。
現在は[V8ランタイムに対応（2020年3月17日）](https://cloud.google.com/blog/ja/products/g-suite/data-processing-just-got-easier-apps-scripts-new-v8-runtime)していて、モダンなJavaScript環境のひとつとして使うことができます。

GASの情報を検索すると、新しい書き方と古い書き方が混ぜこぜで書いてあるコードがたくさんヒットします。
このドキュメントでは、GASをゼロから作成する方法というより、ウェブに落ちているコードを、どのように読み替えるかを中心に整理しようと思います。

```{toctree}
---
maxdepth: 1
---
gas-variables
gas-function
gas-namespace
gas-class
gas-logger
gas-date
gas-filter
gas-id
gas-drive
gas-spreadsheet
gas-document
gas-gform
gas-gmail
gas-groups
gas-calendar
gas-request
gas-doget
gas-clasp
gas-quota
gas-version
```

## リファレンス

- [Drive Service](https://developers.google.com/apps-script/reference/drive)
- [Forms Service](https://developers.google.com/apps-script/reference/forms)
- [Gmail Service](https://developers.google.com/apps-script/reference/gmail)
- [Spreadsheet Service](https://developers.google.com/apps-script/reference/spreadsheet)
- [Group Service](https://developers.google.com/apps-script/reference/groups)
- [V8 Runtime Overview / Syntax Examples](https://developers.google.com/apps-script/guides/v8-runtime#v8_syntax_examples)
