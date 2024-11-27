# プロパティしたい（`Properties Service`）

```js
const sp = PropertiesService.getScriptProperties();
const keys = sp.getKeys();
const properties = sp.getProperties();

const p = sp.getProperty(キー);
```

`PropertiesService`で、プロジェクトに設定したプロパティを管理できます。
プロジェクトごとに設定できるため、一時的なキャッシュとして利用することもできます。

また、ソースコードをGit管理している場合、
非公開のドキュメントIDはソースにベタ書きして残したくないと思います。
そのような場合、この機能がちょうどよいです。

:::{caution}

プロジェクトのプロパティは、シークレット情報を保存するためのものではないそうです。
APIトークンなど、漏れてはいけないキーは別の方法を使ってください。

:::

## リファレンス

- [Properties Service](https://developers.google.com/apps-script/reference/properties)
