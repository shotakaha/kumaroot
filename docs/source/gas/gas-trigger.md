# トリガーしたい（`ScriptApp.newTrigger`）

```js
ScriptApp.newTrigger("関数名")
  .トリガーの種類
  .create();
```

`ScriptApp.newTrigger`でトリガーを作成できます。
トリガーの種類ごとに`TriggerBuilder`が用意されているので、目的にあったビルダーを呼び出して設定し、`create`します。

## 時間主導型したい（`ClockTriggerBuilder`）

```js
ScriptApp.newTrigger("関数名")
  .timeBased()
  .onWeekDay(ScriptApp.WeekDay.SUNDAY)
  .create();
```

`timeBased`で時間主導型の`ClockTriggerBuilder`を作成できます。
ここでは`onWeekDay`でトリガーを発行する曜日を設定しています。

## トリガーを確認したい（`getProjectTriggers`）

```js
const triggers = ScriptApp.getProjectTriggers();
const n = triggers.length;
Logger.log(`Current project has ${n} triggers.`);

for (const trigger of triggers) {
    // トリガーするイベントタイプ
    const eventType = trigger.getEventType();
    // トリガーで呼び出される関数
    const handlerFunction = trigger.getHandlerFunction();
    // トリガーを起動するイベントのソース
    const triggerSource = trigger.getTriggerSource();
    // ソースに固有のID
    // クロックイベントの場合 null
    const triggerSourceId = trigger.getTriggerSourceId();
    // ユニークなトリガーID
    const uniqueId = trigger.getUniqueId();
}
```

`getProjectTriggers`で、現在のプロジェクトとユーザーに
関連づけられているトリガーをすべて取得できます。

## トリガーを削除したい（`deleteTrigger`）

```js
const fn = someFunction;
const triggers = ScriptApp.getProjectTriggers();
for (const trigger of triggers) {
    if (trigger.getHandlerFunction() === fn) {
        ScriptApp.deleteTrigger(trigger);
    }
}
```

`deleteTrigger`で任意のトリガーを削除できます。
`Trigger.getHandlerFunction`で判定することで、
特定のトリガーを削除できます。

## リファレンス

- [Class ScriptApp](https://developers.google.com/apps-script/reference/script/script-app)
- [Class TriggerBuilder](https://developers.google.com/apps-script/reference/script/trigger-builder)
- [Class ClockTriggerBuilder](https://developers.google.com/apps-script/reference/script/clock-trigger-builder)
