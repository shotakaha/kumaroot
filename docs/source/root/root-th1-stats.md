# 統計情報したい（`TH1::SetStats`）

```cpp
// 統計ボックスを表示
h->SetStats();
// または
h->SetStats(1);

// 統計ボックスを非表示
h->SetStats(0);
```

`TH1::SetStats`メソッドで、統計ボックスの表示／非表示を切り替えることができます。

統計ボックスの表示内容は
[TStyle::SetOptStat](./root-gstyle-setoptstat.md)で設定できます。
