# 複雑な構造のデータを読み込みたい（ ``TTree::Branch`` ）

.. code:: cpp

    tree->Branch("run", &run, "run/I")

```cpp
TBranch* Branch(const char* name,
                Long_t address,
                const char* leaflist,
                Int_t bufsize = 32000)
```

``name``
:   ブランチ名を指定します。
    変数名とのひも付けは次の``address``で行います。

``address``
:   変数のアドレスを指定します。
    変数は事前に宣言をしておきます。
    変数が実体の場合は{kbd}`&`が先頭に必要です。
    配列の場合はそのまま（``array``）もしくは配列の最初のアドレス（``&array[0]``）を指定します。

``leaflist``
:   変数の型を指定します。
    ``変数/型``という形式で記述し、``int型``は``i``、``float型`` / ``double型``は``F``など。

## サンプルコード


```cpp
// data2tree.C
{
    // STEP1: データファイルを読み込む
    TString ifn = "inputfilename"
    ifstream fin;
    fin.open(ifn);

    // STEP2: データを格納するための変数を定義する
    int val1, val2, val3, val4;

    // STEP3: TTreeを作成する
    TTree *tree = new TTree("name", "title);

    // STEP4: TTree::Branch(...)を使って、各変数のブランチを作成する
    tree->Branch("val1", &val1, "val1/I");
    tree->Branch("val2", &val2, "val2/I");
    tree->Branch("val3", &val3, "val3/I");
    tree->Branch("val4", &val4, "val4/I");

    // STEP5: cppでファイルを読み込むときの常套手段
    while (fin >> val1 >> val2 >> val3 >> val4) {
        // STEP6: データのエントリの区切りで必ずTTree::Fill()する
        tree->Fill();
    }

    // STEP7: 作成したTTreeを保存するためのTFileを作成する
    TString ofn = "outputfilename";
    TFile *fout = new TFile(ofn, "recreate");

    // STEP8: TFileにTTreeを書き込む
    tree->Write();  //

    // STEP9: TFileを閉じる
    // プログラム（やマクロ）終了時に勝手に閉じてくれるらしいが一応
    fout->Close();

    return;
}
```


[TTree::ReadFileを使った方法](root-ttree-readfile.md)と比べると、
コードの行数がぐーんと多くなりました。

行数が増えた分（？）、汎用性は高くなっています。
この方法だと、ブランチに**配列**を設定ができます。

## ブランチに配列を使いたい

```{code-block} cpp
---
linenos: true
emphasize-lines: 3
---
Int_t val1[100];
TTree *tree = new TTree("tree", "tree using array");
tree->Branch("val1", val1, "val1[100]/I");
```

第1引数はブランチの名前なので、任意の文字列を指定します。
第2引数には**変数のアドレス**が必要とされています。
配列の変数名は、その先頭アドレスを返すので、そのまま``val1``と書けばよいです。
第3引数では、変数名に配列の長さをベタ書きします。


## ブランチに可変長配列を使いたい

少し手間を加えると可変長配列も扱えます。

1. 配列の大きさ fN を定義する
1. 配列 val を定義する
1. fN のブランチを作る
1. val のブランチを作る

```cpp
Int_t fN;                                 // (1) 設定したい配列の大きさ
Int_t val[max];                           // (2) val[max]: maxはfNよりも大きな数
tree->Branch("nch", &fN, "nch/I");        // (3) まずfNをブランチにセットする；fNだと何の変数か分かりづらいので、nch（全チャンネル数の意）に変更した点に注意
tree->Branch("val", val, "val[nch]/I");   // (4) 次にval[fN]をセットする；maxでも、fNでもなくなく、nchにする点に注意

// (4)を以下のようにすると、"Illegal leaf ..." と怒られる
tree->Branch("val", val, "val[fN]/I");    // fNには、ブランチ名を入れる必要があるらしい（
```


### 可変長文字列を使いたい

```cpp
#include <string.h>    // strlen()を使うために必要

const Int_t NMAX_MOJI = 100;
char hoge[NMAX_MOJI];
Int_t nmoji;
tree->Branch("nmoji", &nmoji, "nmoji/I");
tree->Branch("moji", hoge, "hoge[nmoji]/C");

sprintf(hoge, "hoge-hoge-fuga-ga");
nmoji = strlen(hoge)
tree->Fill()
```

### ``std::vector``を使いたい

```cpp
#include <vector>

std::vector<Double_t> vec;
TTree *tree = new TTree("tree", "tree using vector");
tree->Branch("vec", &vec);
```

``<vector>``をincludeする。
namespaceを定義しない場合は``std::vector<型> 変数名``と宣言すること。
当たり前のことだけど、結構忘れてしまう。
ROOT(CINT)を起動させると``vector<型> 変数名``で使えてしまうため、よく忘れる…orz。
``vector型``の変数は実体であるため、第2引数は先頭に{kbd}`&`が必要。
``array``と同じようにすると怒られる。
ROOTが空気を読んでくれるため、第3引数はなくてよいみたい。
まぁでも一番最後のブランチにするのが無難かもしれない。
