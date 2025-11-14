# 統計情報したい（`TH1::SetStats`）

```cpp
#include <TH1D.h>

TH1D *h = new TH1D("h", "Data", 100, 0, 10);
// ...データを入力...

// 統計ボックスを表示
h->SetStats();
// または
h->SetStats(1);

// 統計ボックスを非表示
h->SetStats(0);

h->Draw();
```

`TH1::SetStats`メソッドで、統計ボックスを操作できます。
`SetStats(1)`で統計ボックスを表示し、`SetStats(0)`で非表示にします。
統計ボックスには平均値、RMS、エントリー数などが表示されます。
