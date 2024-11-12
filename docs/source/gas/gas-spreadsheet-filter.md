# フィルター操作したい（`FilterCriteria`）

```js
const criteria = SpreadsheetApp.newFilterCriteria();
criteria.条件();
criteria.build();
```

`FilterCriteriaBuilder`でフィルター条件を新規作成できます。
「空白セルを除外」や「ある日付で判定」「ある文字列ではじまる」などの条件メソッドを呼び`.build()`することでフィルター用の`FilterCriteria`オブジェクトが作成できます。
よく使うフィルター条件は、定義しておくとよいです。

## 空白セルを除外したい（`whenCellNotEmpty`）

```js
const criteria = SpreadsheetApp.newFilterCriteria().whenCellNotEmpty().build();

const range = ...
const filter = range.getFilter();
filter.setColumnFilterCriteria(インデックス, criteria);
```

`whenCellNotEmpty`で空白セルを除外できます。
もっともよく使う条件だと思います。
