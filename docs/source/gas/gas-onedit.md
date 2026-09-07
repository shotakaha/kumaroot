# セルを編集したときに処理したい（`onEdit`）

```js
function onEdit(e) {
    // 編集されたセルに、編集時刻をメモとして残す
    e.range.setNote(`最終更新: ${new Date()}`);
}
```

`onEdit`関数は、スプレッドシートのセルを手動で編集したときに自動で呼ばれる関数です。

`onEdit`は**シンプルトリガー**なので、トリガーの登録は不要です。
その代わり、次の制約があります。

- 手動の編集でのみ実行される（`setValue`などスクリプトからの変更では実行されない）
- メールの送信など、認可が必要な操作はできない
- 実行時間は30秒まで

## 引数したい（`e`）

`onEdit(e)`の引数`e`には、編集の情報が入っています。

| プロパティ | 内容 |
| --- | --- |
| `e.range` | 編集されたセル（`Range`） |
| `e.value` | 編集後の値。**単一セルのときだけ**入る |
| `e.oldValue` | 編集前の値。**単一セルのときだけ**入る |
| `e.source` | スプレッドシート（`Spreadsheet`） |
| `e.user` | 編集したユーザー（`User`） |
| `e.authMode` | 認可モード（`ScriptApp.AuthMode`） |

複数セルをまとめて編集したときは`e.value`と`e.oldValue`が`undefined`になります。
その場合は`e.range.getValues()`で範囲の値を取得します。

## ステータスの変更で処理したい

```js
function onEdit(e) {
    const sheet = e.range.getSheet();

    // 「申請」シートのC列（ステータス列）だけを対象にする
    if (sheet.getName() !== "申請") return;
    if (e.range.getColumn() !== 3) return;

    // 「未処理」→「承認」に変わったときだけ発動する
    if (e.oldValue === "未処理" && e.value === "承認") {
        // 承認した日時を隣のD列に書き込む
        e.range.offset(0, 1).setValue(new Date());
    }
}
```

`e.range`から`getSheet`・`getColumn`で編集位置を絞り、
`e.oldValue`と`e.value`で「どの値からどの値に変わったか」を判定します。
`e.oldValue`と`e.value`は単一セルの編集でしか入らないので、
このパターンはセルを1つずつ編集する運用に向いています。

## リファレンス

- [シンプルなトリガー | Apps Script](https://developers.google.com/apps-script/guides/triggers?hl=ja)
- [イベントオブジェクト | Apps Script](https://developers.google.com/apps-script/guides/triggers/events?hl=ja)
