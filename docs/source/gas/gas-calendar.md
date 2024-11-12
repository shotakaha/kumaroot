# カレンダーしたい（`CalendarApp`）

```js
const calendar = CalendarApp.getCalendarById("ID");
const events = calendar.getEvents(開始日, 終了日);
for (const event of events) {
    Logger.log(event.getTitle());
    Logger.log(event.getDescription());
    Logger.log(event.getStartTime());
    Logger.log(event.getEndTime());
};
```

## イベントを取得したい

```js
const event = calendar.getEventsForDay(日時);
const events = calendar.getEvents(開始日, 終了日);
```

`getEventsForDay`で指定した1日のイベント、
`getEvents`で指定した期間のイベントを取得できます。

:::{note}

`getEventById`もありますが、あまり使わないと思います。

:::

## イベントを追加したい

```js
calendar.createEvent(タイトル, 開始日時, 終了日時, オプション);
calendar.createAllDayEvent(タイトル, 日時);
```

`createEvent`でイベントを追加できます。
`createAllDayEvent`で終日イベントを追加できます。
