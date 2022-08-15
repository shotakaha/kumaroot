# データをすぐに読み込みたい（``TTree::ReadFile``）

```{code-block} cpp
---
linenos: true
emphasize-lines: 2
---
TTree *tree = new TTree("t1", "test measurement");
tree->ReadFile("入力ファイル名", "列1/I:列2/I:列3/D", ",");  // CSVを読み込んだ想定
tree->Draw("列1");  // 列1のヒストグラムを作成
```

```cpp
Long64_t ReadFile(const char* filename,
                  const char* branchDescriptor = "",
                  char delimiter = ' ')
```

``filename``
:   読み込むファイル名（テキストファイル）を指定します。
    連番ファイルを読みこむ場合は、後述する TString を使うと楽ちんです。
    ファイルの内容（=カラム名）は``branchDescriptor``で指定します。

``branchDescriptor``
:   ブランチ変数を指定します。
    複数のブランチ変数を指定する場合は``:（コロン）``で区切ってください。
    ブランチ名には型を含めることができます。
    ``Int_t型``の場合は``ブランチ名/I``、``Double_t型``の場合は``ブランチ名/D``のように書きます。
    型を省略した場合は``Float_t型``の``ブランチ名/F``になるらしいです。

``delimiter``
:   入力ファイルの区切り文字を指定します。
    デフォルトは``" "（半角スペース）``です。
    CSVファイルを読み込む場合は``","``と指定します。

## サンプルコード

ここに``100行4列``のデータのテキストファイルがあるとします。
このファイルの「行数」はイベント数に相当し、
「列数」は取得したデータの項目に相当します。

```unixconfig
# ch1,ch2,ch3,ch4,temp
100,105,104,103,20.5
101,106,103,100,20.7
...
```


```cpp
// data2tree.C
{
    // STEP1: Set input filename
    TString ifn = "inputfilename";

    // STEP2: Create TTree
    TTree *tree = new TTree("tree", "tree using ReadFile()");

    // STEP3: Read data using TTree::ReadFile(...) method
    tree->ReadFile(ifn.Data(), "row1/I:row2/I:row3/I:row4/I:row5/D", ",");

    // STEP4: Create TFile to save TTree
    TString ofn = "out.root";
    TFile *fout = new TFile(ofn, "recreate");

    // STEP5: Write TTree to TFile
    tree->Write();

    // STEP6: Close TFile
    fout->Close();

    return;
}
```


```{note}
学生実験や小さなテストベンチを使った実験の場合、
取得したデータはテキスト形式で出力するのが一番簡単な方法です。
ROOTで解析するときはTTreeになっていると楽ちんなので、
このデータをすぐに変換できるようマクロを作ることをオススメします。
```
