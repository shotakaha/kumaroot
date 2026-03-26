# プロパティしたい（`PropertiesService`）

```js
// スクリプトプロパティを取得
const props = PropertiesService.getScriptProperties();
const p = props.getProperty("キー名");
```

`PropertiesService`で、プロジェクトに設定したプロパティを管理できます。
プロパティは、GASのプロジェクトごとに設定できます。
ソースコードをGit管理している場合に、
非公開のドキュメントIDをベタ書きしたくないときに、
この機能がちょうどよいです。

:::{caution}

プロジェクトのプロパティは、シークレット情報を保存するためのものではないそうです。
APIトークンなど、漏れてはいけないキーは、外部のシークレット管理を使ってください。

:::

## ユーザープロパティしたい（`getUserProperties`）

```ts
const props = PropertiesService.getUserProperties();
```

`getUserProperties`は、ユーザー単位で分離できるプロパティです。

## ドキュメントプロパティしたい（`getDocumentProperties`）

```ts
const props = PropertiesService.getDocumentProperties();
```

`getDocumentProperties`は、スプレッドシートなどのドキュメント単位で分離できるプロパティです。

## リファレンス

- [Properties Service](https://developers.google.com/apps-script/reference/properties)
