# SpreadsheetAppの使い方

## スプレッドシートを開きたい（``openById``）

```js
const sheet = SpreadsheetApp.openById("シートID")
```

## シートを選択したい（``getSheetByName``）

```js
sheet.getSheetByName("シート名")
```

## シート名を変更したい（``setName``）

```js
sheet.getSheetByName("シート名").setName("変更後のシート名")
```

## シートを削除したい（``deleteSheet``）

```js
sheet.deleteSheet(sheet.getSheetByName("シート名"))
```
