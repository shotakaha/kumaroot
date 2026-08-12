# フィルターを操作したい（`FilterCriteria`）

```js
// SpreadsheetApp.newFilterCriteria()
//   .条件メソッド()
//   .build();

const criteria = SpreadsheetApp.newFilterCriteria()
  .whenCellNotEmpty()
  .build();
```

`FilterCriteriaBuilder`でフィルター条件を新規作成できます。
「空白セルを除外」や「ある日付で判定」「ある文字列ではじまる」などの条件メソッドを呼び`.build()`することでフィルター用の`FilterCriteria`オブジェクトが作成できます。
よく使うフィルター条件は、定義しておくとよいです。

## フィルターを作成・取得したい（`createFilter` / `getFilter`）

```js
const range = sheet.getDataRange();

// すでにフィルターがあれば取得し、なければ新規作成する
const filter = sheet.getFilter() || range.createFilter();
```

シートに設定できるフィルターはひとつだけです。
`getFilter`は、シートにフィルターがない場合`null`を返すため、
`createFilter`と組み合わせて使うとよいです。

## 空白セルを除外したい（`whenCellNotEmpty`）

```js
const criteria = SpreadsheetApp.newFilterCriteria().whenCellNotEmpty().build();

// 2列目（B列）に条件を設定する。列番号は1はじまり
filter.setColumnFilterCriteria(2, criteria);
```

`whenCellNotEmpty`で空白セルを除外できます。
もっともよく使う条件だと思います。
`setColumnFilterCriteria`の列番号は1はじまりです（2ならB列）。
