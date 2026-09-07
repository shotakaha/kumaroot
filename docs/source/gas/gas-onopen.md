# ファイルを開いたときに処理したい（`onOpen`）

```js
function onOpen(e) {
    const ui = SpreadsheetApp.getUi();
    ui.createMenu("カスタムメニュー")
        .addItem("実行する", "myFunction")
        .addToUi();
}
```

`onOpen`関数は、スプレッドシート・ドキュメント・スライド・フォームを開いたときに自動で呼ばれる関数です。
主にカスタムメニューを追加する用途で使います。

`onOpen`は**シンプルトリガー**なので、トリガーの登録は不要です。
その代わり、外部サービスへのアクセスやファイルの読み書きなど、
認可が必要な操作はできません（メニューの追加はできます）。

## サービスごとに`getUi`したい

`getUi`は開いているファイルの種類にあわせて使い分けます。

| ファイルの種類 | UIの取得 |
| --- | --- |
| スプレッドシート | `SpreadsheetApp.getUi()` |
| ドキュメント | `DocumentApp.getUi()` |
| スライド | `SlidesApp.getUi()` |
| フォーム | `FormApp.getUi()` |

メニューを組み立てる`createMenu`・`addItem`・`addToUi`の使い方はどのサービスでも共通です。

## 引数したい（`e`）

`onOpen(e)`の引数`e`には、次の情報が入っています。

| プロパティ | 内容 |
| --- | --- |
| `e.source` | 開いたファイルのオブジェクト（`Spreadsheet`など） |
| `e.user` | ファイルを開いたユーザー（`User`） |
| `e.authMode` | 認可モード（`ScriptApp.AuthMode.NONE`など） |

シンプルトリガーの`e.authMode`は基本的に`NONE`または`LIMITED`です。
認可が必要な処理をしたいときは、`onOpen`からメニュー経由で別の関数を呼び出します。

## リファレンス

- [シンプルなトリガー | Apps Script](https://developers.google.com/apps-script/guides/triggers?hl=ja)
- [メニュー | Apps Script](https://developers.google.com/apps-script/guides/menus?hl=ja)
