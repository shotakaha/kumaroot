# TCanvas編

## 色見本を見たい

```cpp
root> TCanvas c
root> c.DrawColorTable()
```

ROOTのプロンプト内で上のように入力すると、簡単に確認できます。

## キャンバスを作成したい（``TCanvas``）

```cpp
TCanvas *c1 = TCanvas("c1", "title", 200, 10, 700, 900);
```

```python
import TCanvas from ROOT
c1 = TCanvas("c1", "title", 200, 10, 700, 900);
```

## キャンバスを分割したい（``Divide``）

```cpp
c1->Divide(2, 3);

// 5番目のキャンバスに描画する場合
c1->cd(5);
```

``Divide``でキャンバスを分割できます。
また``cd``でサブキャンバスを指定できます。

## グラフの軸をログ表示にしたい

```cpp
TCanvas *c1;
c1->SetLogy();
```

``SetLogy``でY軸をログ表示に変更できます。


キャンバスを分割している場合
--------------------------------------------------


まず、分割したいキャンバスに移動する

.. code:: cpp

    c1->cd(2)->SetLogy();
    h1->Draw();

gPadは current canvas へのポインタなので、下のようにも書くことができる。

.. code:: cpp

    c1->cd(2);
    gPad->SetLogy();


## 複数のキャンバスをPDFに保存したい

```cpp
// ファイル名を設定する
TString name;
name.Form("canvas.pdf");

// キャンバスを作成する
TCanvas *c1 = new TCanvas(name.Data(), name.Data(), 1000, 500);

// PDFファイルを開く
c1->Print(name + "[", "pdf");

for (Int_t ihist = 0; ihist < Nhists; ihist++) {
    // ヒストグラムを描画する
    hist[ihist]->Draw();
    // キャンバスをPDFファイルに追加する
    c1->Print(name, "pdf")
}

// PDFファイルを閉じる感じ
c1->Print(name + "]", "pdf");
```

PDF形式で保存する場合にかぎり、複数のキャンバスを1つのPDFに書き出すことができます。
（やったことないけれどPostScriptでもできるらしいです。PNGはできません。）

ROOT公式ユーザーズガイド “9. Graphics and the Graphical Userinterface :
The Postscript Interface” (p139)参照

```cpp
// c1->Print(name + "]", "pdf");

c2->Print(name, "pdf")
c2->Print(name + "]", "pdf")
```

最後の一文を活用して、別のTCanvasオブジェクトを追加し
て保存することもできます。

:::{note}

括弧（ ``[`` と ``(`` ）の違いについて

| 種類 | 説明 |
|---|---|
| ``[`` | この時点ではページを出力しない |
| ``(`` | この時点でページを出力する（空白のページができる？） |

:::
