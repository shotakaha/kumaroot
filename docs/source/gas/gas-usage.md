# Google Apps Script の使い方

`Google Apps Script (GAS)`は、Googleスプレッドシートやフォームなどのサービスと連携し、
作業の自動化や簡易アプリケーションの構築ができるスクリプト実行環境です。
現在は[V8ランタイムに対応（2020年3月17日）](https://cloud.google.com/blog/ja/products/g-suite/data-processing-just-got-easier-apps-scripts-new-v8-runtime)していて、モダンなJavaScript環境のひとつとして使うことができます。
ブラウザだけで開発・実行できるのが大きな特徴です。

一方で、GAS特有の制約として、モジュール分割（ESModule）や`import/export`文がそのままでは利用できません。
そのため、コード量が増えてくるにつれて構造化が難しくなり、
保守性の低下といった課題に直面しやすくなります。

このページでは、GASエディターを直接編集するのではなく、
ローカルで開発・ビルドしてからGASにデプロイするという開発スタイルを紹介します。
具体的には、
`TypeScript`で型安全にコードを記述し、
`rollup`でバンドルし、
`clasp`でGAS環境にデプロイします。

:::{note}

GASの情報を検索すると、新しい書き方と古い書き方が混在したコード片が多く見つかります。
とくにV8ランタイム以前の記述や、現在では推奨されない書き方がそのまま紹介されているケースもあります。
そのため、単にサンプルコードを流用するだけでは、動かないこともたくさんあります。

このページでは、ウェブに落ちているコードを、どのように読み替えるかについても整理することを目指します。

:::

## 環境構築したい

```{toctree}
---
maxdepth: 1
---
gas-typescript
gas-rollup
gas-typedoc
gas-clasp
js-jest
js-biome
```

## GAS操作したい

```{toctree}
---
maxdepth: 1
---
gas-builtins
gas-logger
gas-variables
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
gas-trigger
gas-properties
gas-quota
gas-version
gas-exports
```

## JavaScript / TypeScriptしたい

```{toctree}
---
maxdepth: 2
---
js-usage
```

## リファレンス

- [Drive Service](https://developers.google.com/apps-script/reference/drive)
- [Forms Service](https://developers.google.com/apps-script/reference/forms)
- [Gmail Service](https://developers.google.com/apps-script/reference/gmail)
- [Spreadsheet Service](https://developers.google.com/apps-script/reference/spreadsheet)
- [Group Service](https://developers.google.com/apps-script/reference/groups)
- [V8 Runtime Overview / Syntax Examples](https://developers.google.com/apps-script/guides/v8-runtime#v8_syntax_examples)
