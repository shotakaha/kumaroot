# プロパティしたい（`PropertiesService`）

```js
const props = PropertiesService.getScriptProperties();

props.setProperty("DOC_ID", "1Abc...xyz");   // 値を保存する
const docId = props.getProperty("DOC_ID");   // 値を読み出す
```

`PropertiesService`は、キーと値のペアをGASのプロジェクトに保存する機能です。
ソースコードをGitで管理していて、非公開のドキュメントIDなどをベタ書きしたくないときに便利です。

:::{caution}

プロパティの値は暗号化されずに保存されます。
APIキーやアクセストークンなど、漏れてはいけない情報の保存には使わないでください。

:::

## スコープを選びたい

`PropertiesService`には、共有範囲の違う3つのストアがあります。

| メソッド | 共有範囲 | 用途 |
| --- | --- | --- |
| `getScriptProperties` | プロジェクト全体（全ユーザー共通） | 設定値、外部リソースのID |
| `getUserProperties` | 実行したユーザーごと | ユーザー個人の設定 |
| `getDocumentProperties` | バインド先のドキュメントごと | そのシート固有の状態 |

```js
const scriptProps = PropertiesService.getScriptProperties();
const userProps = PropertiesService.getUserProperties();
const docProps = PropertiesService.getDocumentProperties();
```

`getDocumentProperties`は、スプレッドシートなどにバインドされたスクリプトでのみ使えます。
スタンドアロンのスクリプトで呼ぶと`null`が返るので注意してください。

## 値を設定したい（`setProperty`）

```js
const props = PropertiesService.getScriptProperties();

// 1件ずつ設定する
props.setProperty("DOC_ID", "1Abc...xyz");

// 複数まとめて設定する
props.setProperties({
    DOC_ID: "1Abc...xyz",
    SHEET_NAME: "集計",
});
```

`setProperties`に`true`を第2引数で渡すと、既存のキーをすべて削除してから設定します。

## 値を読み出したい（`getProperty`）

```js
const props = PropertiesService.getScriptProperties();

const docId = props.getProperty("DOC_ID");   // 値。なければ null
const keys = props.getKeys();                // キーの配列
const all = props.getProperties();           // { DOC_ID: "1Abc...", SHEET_NAME: "集計" }
```

## 値を削除したい（`deleteProperty`）

```js
const props = PropertiesService.getScriptProperties();

props.deleteProperty("DOC_ID");     // 1件削除する
props.deleteAllProperties();        // すべて削除する
```

## 文字列以外を保存したい（`JSON.stringify`）

プロパティの値は、かならず文字列で保存されます。
数値やオブジェクトを保存するときは`JSON.stringify`で変換し、読み出すときに`JSON.parse`で戻します。

```js
const props = PropertiesService.getScriptProperties();

// 保存する
props.setProperty("config", JSON.stringify({ retry: 3, verbose: true }));

// 読み出す
const config = JSON.parse(props.getProperty("config"));
config.retry;   // 3
```

`setProperty("count", 5)`のように数値をそのまま渡すと`"5"`として保存され、
オブジェクトを渡すと`"[object Object]"`になってしまいます。

## エディターから設定したい

コードを書かずに、GASエディターからスクリプトプロパティを登録することもできます。

1. `[プロジェクトの設定]`（歯車アイコン）を開く
2. `[スクリプト プロパティ]` > `[スクリプト プロパティを追加]`
3. プロパティとキーと値を入力して保存

Gitにコミットしたくない値は、この画面から登録するとソースコードに残りません。

## リファレンス

- [Class PropertiesService | Apps Script](https://developers.google.com/apps-script/reference/properties/properties-service?hl=ja)
- [Class Properties | Apps Script](https://developers.google.com/apps-script/reference/properties/properties?hl=ja)
