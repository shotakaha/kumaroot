# 対話型プロンプトしたい（`Rint`）

`Rint`はROOTの対話型プロンプトのインターフェイスを管理するクラスです。
ターミナルで`root`コマンドを実行すると、
`Rint`が起動して、C++コードを対話的に実行できるようになります。

`Rint`のバックエンドは
ROOT5までは`CINT`でしたが、
ROOT6からは`Cling`に変更されました。

## 起動したい（`$ root`）

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

`root`コマンドでROOTの対話型インタープリターを起動できます。
ROOT6から、インタープリターのバックエンドが`CINT`から`Cling`に変更されました。
`C++`はコンパイルが必要な言語ですが、
`Cling`のおかげで、Pythonなどのスクリプト言語のように、
コードを1行ずつ逐次実行できます。

## 終了したい（`.q`）

```console
$ root
// RINTが起動

root [0] .q
root [0] .qqq      # ROOTを終了
root [0] .qqqqq    # プロセスをすぐに終了
root [0] .qqqqqqq  # プロセスをアボート
```

`.q`で終了できます。
プロセスがハングしてしまった場合は、`.qqq`のように`q`の数を増やしてみるとよいです。
それでも終了できない場合は、ターミナルのタブを強制的に閉じるか、
[`kill`コマンド](../command/command-ps.md)でプロセスを終了させてください。

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
