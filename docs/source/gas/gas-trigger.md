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

## リファレンス

- [Class ScriptApp](https://developers.google.com/apps-script/reference/script/script-app)
- [Class TriggerBuilder](https://developers.google.com/apps-script/reference/script/trigger-builder)
- [Class ClockTriggerBuilder](https://developers.google.com/apps-script/reference/script/clock-trigger-builder)
