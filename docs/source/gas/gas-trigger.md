# トリガーしたい（`ScriptApp.newTrigger`）

```js
const triggerBuilder = ScriptApp.newTrigger("関数名")
    .timeBased()     // トリガーの種類
    .atHour(9)       // 午前9時
    .everyDays(1)    // 毎日
triggerBuilder.create();
```

`ScriptApp.newTrigger`でトリガーを作成できます。
トリガーの種類ごとに`TriggerBuilder`が用意されているので、目的にあったビルダーを呼び出して設定し、`create`します。

## トリガーを確認したい

```js
function getProjectTriggers() {
    const triggers = ScriptApp.getProjectTriggers();
    const n = triggers.length;
    Logger.log(`Found {$n} triggers`);
    if (n === 0) return []

    const triggerList = triggers.map(trigger => ({
        functionName: trigger.getHandlerFunction(),
        eventType: trigger.getEventType(),
        triggerSource: trigger.getTriggerSource(),
        triggerSourceId: trigger.getTriggerSourceId(),  // ソースの固有ID。クロックイベントはnull
        uniqueId: trigger.getUniqueId(),
    }))
}

function logProjectTriggers(triggerList) {
    if (triggerList.length == 0) {
        Logger.log("現在設定されているトリガーはありません");
        return;
    }

    triggerList.forEach(trigger => {
        Logger.log(`関数名: ${trigger.functionName}`);
        Logger.log(`種類  : ${trigger.eventType}`);
        Logger.log(`ソース: ${trigger.triggerSource}`);
        Logger.log(`ソースID: ${trigger.triggerSourceId}`);
        Logger.log(`ユニークID: ${trigger.uniqueId}`);
        logger.log("-----");
    })
}

function showProjectTriggers() {
    const triggers = getProjectTriggers();
    logProjectTriggers(triggers);
}
```

`getProjectTriggers`で、現在のプロジェクトに設定されているすべてのトリガーを取得できます。
`get...`、`log...`、`show...`のように、
用途を意識したコンポーネントに分離しておくと、便利です。

## トリガーを追加したい

```js
function addTriggerOnce(triggerBuilder, eventType) {
    const fnName = triggerBuilder.getHandlerFunction();

    const isRegistered = ScriptApp.getProjectTriggers().some(trigger =>
        trigger.getHandlerFunction() === fnName &&
        trigger.getEventType() === eventType &&
        trigger.getTriggerSource() === ScriptApp.TriggerSource.CLOCK
    );

    if (isRegistered) {
        Logger.log("トリガーはすでに登録済みです");
        return;
    }

    triggerBuilder.create();
    Logger.log("新しいトリガーを追加しました");
}

function addTrigger(fnName) {
    const triggerBuilder = ScriptApp.newTrigger(fnName)
        .timeBased()
        .atHour(9)
        .everyDays(1);

    addTriggerOnce(triggerBuilder, ScriptApp.EventType.CLOCK);
}
```

トリガーを追加するサンプルです。
設定済みのトリガーがないことを確認してから追加しています。

:::{note}

このサンプルは、ひとつの関数に対してひとつの時間帯だけ登録するようにしてあります。
ひとつの関数を異なる複数の時間帯に登録したい場合は、改良が必要です。

:::

## トリガーを削除したい（`deleteTrigger`）

```js
function deleteTriggerByFnName(fnName) {
    const triggers = ScriptApp.getProjectTriggers();

    triggers.forEach(trigger => {
        if (trigger.getHandlerFunction() === fnName) {
            ScriptApp.deleteTrigger(trigger);
            Logger.log(`トリガーを削除しました: ${fnName}`);
        }
    })
}
```

`deleteTrigger`で指定したトリガーを削除できます。
関数名で削除できるようにしておくと便利です。

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
