# トリガーを作成したい（`ScriptApp.newTrigger`）

```js
ScriptApp.newTrigger("関数名")
    .timeBased()     // 時間主導型トリガー（ClockTriggerBuilder）
    .atHour(9)       // 午前9時
    .everyDays(1)    // 毎日
    .create();
```

`ScriptApp.newTrigger`でトリガーを作成できます。
トリガーの種類ごとに`TriggerBuilder`が用意されているので、目的にあったビルダーを呼び出して設定し、`create`します。
上のサンプルでは`timeBased`で時間主導型の`ClockTriggerBuilder`を作成し、`atHour`と`everyDays`で「毎日午前9時」を設定しています。

## トリガーを確認したい

```js
function showProjectTriggers() {
    const triggers = ScriptApp.getProjectTriggers();

    if (triggers.length === 0) {
        Logger.log("現在設定されているトリガーはありません");
        return;
    }

    triggers.forEach(trigger => {
        Logger.log(`関数名: ${trigger.getHandlerFunction()}`);
        Logger.log(`種類  : ${trigger.getEventType()}`);
        Logger.log(`ソース: ${trigger.getTriggerSource()}`);
        Logger.log(`ソースID: ${trigger.getTriggerSourceId()}`);  // クロックイベントはnull
        Logger.log(`ユニークID: ${trigger.getUniqueId()}`);
        Logger.log("-----");
    });
}
```

`ScriptApp.getProjectTriggers`で、現在のプロジェクトに設定されているすべてのトリガーを取得できます。
`Trigger`オブジェクトの`get...`系メソッドで、関数名や種類などの詳細を確認できます。

## トリガーを追加したい

```js
function addTrigger(fnName) {
    // 同じ関数・同じ種類の既存トリガーを削除する
    ScriptApp.getProjectTriggers()
        .filter(trigger =>
            trigger.getHandlerFunction() === fnName &&
            trigger.getTriggerSource() === ScriptApp.TriggerSource.CLOCK
        )
        .forEach(trigger => ScriptApp.deleteTrigger(trigger));

    // 新しいトリガーを追加する
    ScriptApp.newTrigger(fnName)
        .timeBased()
        .atHour(9)
        .everyDays(1)
        .create();
    Logger.log("トリガーを追加しました");
}
```

トリガーを追加するサンプルです。
同じ関数に対するトリガーがすでに存在する場合は、いったん削除してから追加し直しています。
こうしておくと、`addTrigger`を何度実行してもトリガーが重複登録される心配がありません。

:::{note}

このサンプルは、ひとつの関数に対してひとつの時間帯だけ登録するようにしてあります。
ひとつの関数を異なる複数の時間帯に登録したい場合は、改良が必要です。

:::

## 複数のトリガーをまとめて追加したい

```js
function setupTriggers() {
    ["onFormSubmit", "onEdit", "onDaily"].forEach(fnName => addTrigger(fnName));
}
```

`addTrigger`は1つの関数につき1つのトリガーを登録する関数なので、
登録したい関数名を配列にして`forEach`で呼び出すだけで、複数のトリガーをまとめて追加できます。
プロジェクトの初回実行時に、この`setupTriggers`をエントリーポイントとして呼び出しておくと便利です。

## トリガーを削除したい（`deleteTrigger`）

```js
function deleteTriggerByFnName(fnName) {
    const triggers = ScriptApp.getProjectTriggers();

    triggers.forEach(trigger => {
        if (trigger.getHandlerFunction() === fnName) {
            ScriptApp.deleteTrigger(trigger);
            Logger.log(`トリガーを削除しました: ${fnName}`);
        }
    });
}
```

`deleteTrigger`で指定したトリガーを削除できます。
関数名で削除できるようにしておくと便利です。

## 曜日を指定してトリガーを作成したい（`onWeekDay`）

```js
ScriptApp.newTrigger("関数名")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.SUNDAY)
    .create();
```

`ClockTriggerBuilder`の`onWeekDay`で、トリガーを発行する曜日を指定できます。
`atHour`や`everyDays`のかわりに使うことで「毎週日曜日」のような設定ができます。

## リファレンス

- [Class ScriptApp](https://developers.google.com/apps-script/reference/script/script-app)
- [Class TriggerBuilder](https://developers.google.com/apps-script/reference/script/trigger-builder)
- [Class ClockTriggerBuilder](https://developers.google.com/apps-script/reference/script/clock-trigger-builder)
