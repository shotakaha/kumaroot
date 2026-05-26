# 起動したい（`$ root`）

```console
$ root
   ------------------------------------------------------------------
  | Welcome to ROOT 6.40.00                        https://root.cern |
  | (c) 1995-2025, The ROOT Team; conception: R. Brun, F. Rademakers |
  | Built for macosxarm64 on May 20 2026, 03:46:43                   |
  | From tags/6-40-00@6-40-00                                        |
  | With Apple clang version 17.0.0 (clang-1700.6.4.2) std201703     |
  | Try '.help'/'.?', '.demo', '.license', '.credits', '.quit'/'.q'  |
   ------------------------------------------------------------------

root [0]
```

`root`コマンドでROOTの対話型シェル（Rint）を起動できます。
C++はコンパイルが必要な言語ですが、
RintのおかげてPythonのようにスクリプト言語のように使うことができます。
Rintの中では`TAB`を使ってクラス名やメソッド名が補完できます。

ROOT6から、バックエンドのインタプリターが`CINT`から`Cling`に変更されました。
詳しくは[Clingについて知りたい](./root-cling.md)と[CINTについて知りたい](./root-cint.md)を参照してください。

```{toctree}
---
maxdepth: 1
---
root-rint-quit
root-rint-macro
root-rint-calculator
root-notebook
```

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
