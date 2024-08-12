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
```

ターミナルで``root``と入力して、ROOTシェル（`RINT`）を起動します。

:::{note}

ROOT5のインタプリターは``CINT``でした。
ROOT6で``Cling``が採用され、エラーメッセージ表示なども丁寧になりました。

:::

## 起動時の設定したい（``rootlogon.C``）

```cpp
{
    gStyle->SetStyle("Plain");

    printf("\nWelcome to プロジェクト名\n\n");
    printf("\nまずこれをして\n\n");
    printf("\nつぎにこれをしてください\n\n");
}
```

``rootlogon.C``に、のROOTシェル起動時の設定を保存できます。
プロジェクトごとに設定できます。
起動後になにをしたらいいのか、ヘルプ代わりのメッセージを表示させると便利です。
