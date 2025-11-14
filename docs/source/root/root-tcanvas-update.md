# キャンバスの表示を更新したい（`TCanvas::Update`）

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Canvas", 800, 600);
TGraph *g = new TGraph();

// グラフに点を追加して随時更新
for (int i = 0; i < 100; i++) {
    g->SetPoint(i, i, i * i);
    if (i % 10 == 0) {
        g->Draw("AL");
        c->Update();  // キャンバスを更新して表示
    }
}
```

`TCanvas::Update`メソッドでキャンバスの表示を強制的に更新できます。
グラフやヒストグラムを動的に変更する場合に、画面表示を即座に反映させるために使用します。

```python
from ROOT import TCanvas, TGraph

c = TCanvas("c", "Canvas", 800, 600)
g = TGraph()

# グラフに点を追加して随時更新
for i in range(100):
    g.SetPoint(i, i, i * i)
    if i % 10 == 0:
        g.Draw("AL")
        c.Update()
```

## メソッドのシグネチャ

```cpp
void Update()
```

### 引数と戻り値

このメソッドは引数を取らず、戻り値もありません。

## キャンバスの更新が必要な場面

### リアルタイム描画

キャンバスに描画しながら、同時に画面に表示を反映させたい場合に使用します。

| 場面 | 説明 |
|------|------|
| アニメーション描画 | グラフやヒストグラムを段階的に描画 |
| インタラクティブな処理 | ユーザー操作に応じてリアルタイム更新 |
| 長時間処理 | ループ処理中の進捗を表示 |
| 動的データ処理 | データを追加しながら描画を更新 |

## 使用例

### グラフを段階的に描画したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Progressive Drawing", 800, 600);
TGraph *g = new TGraph();

// グラフを10個の点ごとに段階的に描画
for (int i = 0; i < 100; i++) {
    double x = i * 0.1;
    double y = sin(x);
    g->SetPoint(i, x, y);

    // 10個の点ごとに描画を更新
    if (i % 10 == 0) {
        g->Draw("AL");
        c->Update();

        // 描画の更新を視覚的に確認するための待機
        gSystem->Sleep(100);  // 100ミリ秒待機
    }
}

// 最終的なグラフを描画
g->Draw("AL");
c->Update();
```

グラフを段階的に描画することで、どのようにグラフが構成されているかを確認できます。

### ヒストグラムを動的に埋めたい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TRandom.h>

TCanvas *c = new TCanvas("c", "Dynamic Histogram", 800, 600);
TH1D *h = new TH1D("h", "Random Data Distribution", 100, -3, 3);

// ヒストグラムにデータを段階的に追加
for (int i = 0; i < 10000; i++) {
    // ガウス分布に従う乱数を追加
    h->Fill(gRandom->Gaus(0, 1));

    // 1000個のデータごとに描画を更新
    if (i % 1000 == 0 && i > 0) {
        h->Draw();
        c->Update();

        std::cout << "Added " << i << " entries" << std::endl;
    }
}

// 最終的なヒストグラムを描画
h->Draw();
c->Update();
```

ヒストグラムの形状が段階的にどのように変わるか観察できます。

### 複数のオブジェクトを同時に更新したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TGraph.h>

TCanvas *c = new TCanvas("c", "Multiple Objects", 1200, 400);

// キャンバスを3つに分割
c->Divide(3, 1);

// 各パッドにオブジェクトを配置
c->cd(1);
TH1D *h1 = new TH1D("h1", "Histogram 1", 50, -3, 3);

c->cd(2);
TH1D *h2 = new TH1D("h2", "Histogram 2", 50, -3, 3);

c->cd(3);
TGraph *g = new TGraph();

// 複数のオブジェクトを同時に更新
for (int i = 0; i < 5000; i++) {
    // パッド1にデータを追加
    c->cd(1);
    h1->Fill(gRandom->Gaus(0, 1));

    // パッド2にデータを追加
    c->cd(2);
    h2->Fill(gRandom->Gaus(1, 1.5));

    // パッド3にグラフの点を追加
    c->cd(3);
    g->SetPoint(i, i * 0.001, sin(i * 0.01));

    // 500個のデータごとに全パッドを更新
    if (i % 500 == 0 && i > 0) {
        c->cd(1);
        h1->Draw();

        c->cd(2);
        h2->Draw();

        c->cd(3);
        g->Draw("AL");

        c->Update();  // 全パッドの表示を更新
    }
}

// 最終表示
c->cd(1);
h1->Draw();
c->cd(2);
h2->Draw();
c->cd(3);
g->Draw("AL");
c->Update();
```

複数のパッドを持つキャンバスで、すべてのオブジェクトを一度に更新できます。

### アニメーション効果を作成したい

```cpp
#include <TCanvas.h>
#include <TGraph.h>
#include <TSystem.h>

TCanvas *c = new TCanvas("c", "Animation", 800, 600);
TGraph *g = new TGraph();

// アニメーションのフレームを描画
for (int frame = 0; frame < 100; frame++) {
    g->Clear();  // 前のフレームをクリア

    // 現在のフレームでグラフを描画
    for (int i = 0; i < 50; i++) {
        double x = i * 0.1;
        double y = sin(x + frame * 0.1);  // フレームごとに位相をシフト
        g->SetPoint(i, x, y);
    }

    g->SetTitle(Form("Animation Frame %d", frame));
    g->Draw("AL");
    c->Update();

    // フレーム間の待機時間（16ミリ秒 ≈ 60fps）
    gSystem->Sleep(16);
}
```

`gSystem->Sleep()`を組み合わせることで、アニメーション効果を実現できます。

### 長時間処理中の進捗を表示したい

```cpp
#include <TCanvas.h>
#include <TH1D.h>
#include <TText.h>

TCanvas *c = new TCanvas("c", "Progress", 800, 600);

TH1D *h = new TH1D("h", "Processing Progress", 100, 0, 10000);

// 処理ループ
for (int i = 0; i < 10000; i++) {
    // 実際の処理
    h->Fill(gRandom->Gaus(5000, 2000));

    // 100個のデータごとに進捗を表示
    if (i % 100 == 0) {
        h->Draw();

        // 進捗パーセンテージを表示
        TText *txt = new TText(0.5, 0.95, Form("Progress: %.1f%%", i / 100.0));
        txt->SetNDC();
        txt->SetTextAlign(22);
        txt->Draw();

        c->Update();
    }
}

h->Draw();
c->Update();
```

処理の進捗状況をリアルタイムで表示できます。

## Update の効果

### Update を使用しない場合

```cpp
// ❌ 表示されない可能性がある
for (int i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus());
}
h->Draw();  // ここで初めて表示
```

### Update を使用する場合

```cpp
// ✅ リアルタイムで表示が更新される
h->Draw();
for (int i = 0; i < 1000; i++) {
    h->Fill(gRandom->Gaus());
    if (i % 100 == 0) {
        c->Update();  // 段階的に表示を更新
    }
}
```

## パフォーマンスに関する注意

### Update の頻度に気をつける

```cpp
// ❌ 非効率：毎回 Update を呼び出す
for (int i = 0; i < 100000; i++) {
    h->Fill(value);
    c->Update();  // 毎回更新は遅い
}

// ✅ 効率的：定期的に Update を呼び出す
for (int i = 0; i < 100000; i++) {
    h->Fill(value);
    if (i % 1000 == 0) {
        c->Update();  // 1000個ごとに更新
    }
}
```

Updateの頻度が高すぎると、処理が遅くなります。
目的に応じて適切な間隔で呼び出すことが重要です。

### 大規模データの処理

```cpp
#include <TCanvas.h>
#include <TH1D.h>

TCanvas *c = new TCanvas("c", "Large Dataset", 800, 600);
TH1D *h = new TH1D("h", "Data", 1000, -10, 10);

// 大規模データセット：1000万個のデータ
const int LARGE_SIZE = 10000000;
const int UPDATE_INTERVAL = 100000;  // 10万個ごとに更新

h->Draw();

for (int i = 0; i < LARGE_SIZE; i++) {
    h->Fill(gRandom->Gaus());

    if (i % UPDATE_INTERVAL == 0 && i > 0) {
        c->Update();
    }
}

c->Update();
```

## 関連メソッド

- [キャンバスを作成したい（`TCanvas`）](./root-tcanvas.md)
- [キャンバスを描画したい（`TCanvas::Draw`）](./root-tcanvas-draw.md)
- [キャンバスを分割したい（`TCanvas::Divide`）](./root-tcanvas-divide.md)
- [複数のキャンバスをPDFに保存したい（`TCanvas::Print`）](./root-tcanvas-pdf.md)

## 参考資料

- [ROOT TCanvas::Update Documentation](https://root.cern/doc/master/classTCanvas.html)
- [ROOT Graphics Documentation](https://root.cern/doc/master/group__Graphics.html)
