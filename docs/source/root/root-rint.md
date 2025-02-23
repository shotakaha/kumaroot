# 起動したい（``$ root``）

```console
$ root
   ------------------------------------------------------------------
  | Welcome to ROOT 6.32.02                        https://root.cern |
  | (c) 1995-2024, The ROOT Team; conception: R. Brun, F. Rademakers |
  | Built for macosxarm64 on Jun 18 2024, 03:44:55                   |
  | From heads/master@tags/v6-32-02                                  |
  | With Apple clang version 15.0.0 (clang-1500.3.9.4)               |
  | Try '.help'/'.?', '.demo', '.license', '.credits', '.quit'/'.q'  |
   ------------------------------------------------------------------

// 正規分布のヒストグラムを作成
root [0] TH1F *h = new TH1F("h", "histogram", 100, -5, 5);
root [1] for (int i = 0; i < 10000; i++) {
root (cont'ed, cancel with .@) [2] h->Fill(gRandom->Gaus(0, 1));
root (cont'ed, cancel with .@) [3] }
root [4] h->Draw();
Info in <TCanvas::MakeDefCanvas>:  created default TCanvas with name c1
root [5]
```

`root`コマンドでROOTの対話型シェル（Rint）を起動できます。
C++はコンパイルが必要な言語ですが、
RintのおかげてPythonのようにスクリプト言語のように使うことができます。
Rintの中では`TAB`を使ってクラス名やメソッド名が補完できます。

ROOT5以前は、バックエンドに`CINT`が使われていましたが、
ROOT6から`Cling`に変更されました。
`Cling`ではエラーメッセージの表示なども丁寧になっています。

## 起動時の設定したい（``rootlogon.C``）

```cpp
{
    gStyle->SetStyle("Plain");
    gStyle->SetHistLineWidth(2);
    // gStyle->SetHistLineStyle(0);
    // gStyle->SetHistLineColor(1);
    // gStyle->SetHistFillStyle(0);
    // gStyle->SetHistFillColor(1);
    gStyle->SetNdivisions(20510);  // 100分割

    printf("\nWelcome to プロジェクト名\n\n");
    printf("\nまずこれをして\n\n");
    printf("\nつぎにこれをしてください\n\n");
}
```

``rootlogon.C``に、のROOTシェル起動時の設定を保存できます。
プロジェクトごとに設定できます。
起動後になにをしたらいいのか、ヘルプ代わりのメッセージを表示させると便利です。
