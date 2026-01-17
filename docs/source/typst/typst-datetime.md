# 日付したい（`#datetime`）

```typst
#datetime(
  year: 2026,
  month: 1,
  day: 17,
).display()
// => 2026-01-17
```

`datetime`関数で日付オブジェクトを作成できます。
`.display()`メソッドで文字列に変換して、本文中に表示できます。

## 現在日時したい（`datetime.today`）

```typst
#datetime.today().display()
```

`#datetime.today`メソッドで、ビルド時の現在日時を取得できます。

## 表示フォーマットしたい（`datetime.display`）

```typst
#datetime(
  year: 2026,
  month: 1,
  day: 17
).display("[year]/[month]")
// => 2026/01
```

`#datetime.display`メソッドで、表示フォーマットを変更できます。
デフォルトでは設定した日時の情報に応じて
`[year]-[month]-[day] [hour]:[minute]:[second]`のISO8601形式で表示されます。
