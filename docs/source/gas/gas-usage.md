# Google Apps Script の使い方

`Google Apps Script (GAS)`は、Googleスプレッドシートやフォームなどのサービスと連携し、
作業の自動化や簡易アプリケーションの構築ができるスクリプト実行環境です。
現在は[V8ランタイムに対応（2020年3月17日）](https://cloud.google.com/blog/ja/products/g-suite/data-processing-just-got-easier-apps-scripts-new-v8-runtime)していて、モダンなJavaScript環境のひとつとして使うことができます。
ブラウザだけで開発・実行できるのが大きな特徴です。

GASのプロジェクトには、どのアプリにも紐づかない「スタンドアロンスクリプト」と、
Sheet・Doc・Formなどに紐づいた「コンテナバインドスクリプト」の2種類があります。
詳しくは[`clasp`](./gas-clasp.md)の「新規プロジェクトしたい」を参照してください。

一方で、GAS特有の制約として、モジュール分割（ESModule）や`import/export`文がそのままでは利用できません。
そのため、コード量が増えてくるにつれて構造化が難しくなり、
保守性の低下といった課題に直面しやすくなります。

このページでは、GASエディターを直接編集するのではなく、
ローカルで開発・ビルドしてからGASにデプロイするという開発スタイルを紹介します。
具体的には、次の3段階のワークフローになります。

1. `TypeScript`（`tsc --noEmit`）で型チェックする
2. `rollup`で1つのファイルにバンドルする
3. `clasp push`でGAS環境にアップロードする

このワークフローに加えて、テスト（`jest`）やフォーマッター／リンター（`biome`）、
APIドキュメント生成（`typedoc`）といった補助ツールも組み合わせることで、
GASプロジェクトを通常のTypeScriptプロジェクトと同じように開発・保守できるようになります。

:::{note}

GASの情報を検索すると、新しい書き方と古い書き方が混在したコード片が多く見つかります。
とくにV8ランタイム以前の記述や、現在では推奨されない書き方がそのまま紹介されているケースもあります。
そのため、単にサンプルコードを流用するだけでは、動かないこともたくさんあります。

このページでは、ウェブに落ちているコードを、どのように読み替えるかについても整理することを目指します。

:::

## 環境構築したい

`TypeScript` → `rollup` → `clasp`という開発チェーンと、
それを支える補助ツールの使い方をまとめています。

```{toctree}
---
maxdepth: 1
---
gas-npm
gas-typescript
gas-rollup
gas-clasp
gas-jest
gas-vitest
gas-biome
gas-typedoc
```

## JS/TSしたい

変数・関数・クラスなど、GASに限らないJavaScript/TypeScriptの基本文法をまとめています。

```{toctree}
---
maxdepth: 1
---
gas-builtins
gas-variables
gas-globalthis
gas-function
gas-class
gas-namespace
gas-exports
gas-version
gas-date
gas-filter
```

## GAS操作したい

`Logger`や`SpreadsheetApp`など、GAS固有のクラス・サービスAPIの使い方をまとめています。

```{toctree}
---
maxdepth: 1
---
gas-logger
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
gas-iterator
```

## リファレンス

- [Drive Service](https://developers.google.com/apps-script/reference/drive)
- [Forms Service](https://developers.google.com/apps-script/reference/forms)
- [Gmail Service](https://developers.google.com/apps-script/reference/gmail)
- [Spreadsheet Service](https://developers.google.com/apps-script/reference/spreadsheet)
- [Group Service](https://developers.google.com/apps-script/reference/groups)
- [V8 Runtime Overview / Syntax Examples](https://developers.google.com/apps-script/guides/v8-runtime#v8_syntax_examples)
