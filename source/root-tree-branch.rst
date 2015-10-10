======================================================================
テキストファイルをTTreeに変換したい（２）: （ ``TTree::Branch`` ）
======================================================================

.. code:: cpp

    tree->Branch("run", &run, "run/I")

.. code:: cpp

   TBranch* Branch(const char* name,
                   Long_t address,
                   const char* leaflist,
                   Int_t bufsize = 32000)

.. list-table::
   :header-rows: 1

   * - 変数
     - 説明
   * - ``name``
     - ブランチ名
   * - ``address``
     - 変数のアドレス
   * - ``leaflist``
     - 変数の型

``name`` にはブランチ名として使う文字列を指定する。
用意した変数名とのひも付けは、次の ``address`` で行います。

``address`` には変数のアドレスを指定します。
変数は事前に宣言をしておかないと怒られます。
変数が実体の場合は :kbd:`&` を先頭につけて、配列の場合はそのまま（ ``array`` ）
もしくは配列の最初のアドレス（ ``&array[0]`` ）を指定します。

``leaflist`` は ``変数／型`` で指定します。
``int型`` は ``i`` 、 ``float型`` 、 ``double型`` は ``F`` など。



サンプルコード
==================================================

よくある方法なので、ググればいっぱい見つかります。

.. code:: cpp

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

前述したReadFile を使った方法と比べると、コードの行数がぐーんと多
いことが分かります。（ReadFileの場合、肝となる部分はたったの一行で
す）。

行数が増えた分、汎用性が高くなっています。
こちらの方法だと、ブランチに「配列」を設定することも可能です。


ブランチに配列を使いたい
==================================================

TTree::Branch を理解していれば簡単です。

.. code:: cpp

    int val1[100];
    TTree *tree = new TTree("tree", "tree using array");
    tree->Branch("val1", val1, "val1[100]/I");

第２引数には「変数のアドレス」を指定します。 val1 は
配列の先頭アドレスを指しているので、＆をつける必要はありません。
第３引数には、配列の長さをベタ書きします。


ブランチに文字列を使いたい
==================================================

配列を使うことができるので、文字列のブランチを作ることもできます。

.. code:: cpp

    char hoge[32];
    tree->Branch("moji", hoge", "moji[32]/C")
    sprintf(hoge, "hogehogefugafuga")
    tree->Fill();

ブランチに可変長配列を使いたい
==================================================

少し手間を加えると可変長配列も扱えます。

#. 配列の大きさ fN を定義する
#. 配列 val を定義する
#. fN のブランチを作る
#. val のブランチを作る

.. code:: cpp

    Int_t fN;                                 // (1) 設定したい配列の大きさ
    Int_t val[max];                           // (2) val[max]: maxはfNよりも大きな数
    tree->Branch("nch", &fN, "nch/I");        // (3) まずfNをブランチにセットする；fNだと何の変数か分かりづらいので、nch（全チャンネル数の意）に変更した点に注意
    tree->Branch("val", val, "val[nch]/I");   // (4) 次にval[fN]をセットする；maxでも、fNでもなくなく、nchにする点に注意

    // (4)を以下のようにすると、"Illegal leaf ..." と怒られる
    tree->Branch("val", val, "val[fN]/I");    // fNには、ブランチ名を入れる必要があるらしい（

ブランチに可変長文字列を使いたい
==================================================

.. code:: cpp

    #include <string.h>    // strlen()を使うために必要

    const Int_t NMAX_MOJI = 100;
    char hoge[NMAX_MOJI];
    Int_t nmoji;
    tree->Branch("nmoji", &nmoji, "nmoji/I");
    tree->Branch("moji", hoge, "hoge[nmoji]/C");

    sprintf(hoge, "hoge-hoge-fuga-ga");
    nmoji = strlen(hoge)
    tree->Fill()

ブランチにstd::vector を使いたい
==================================================

.. code:: cpp

    #include <vector>

    std::vector<Double_t> vec;
    TTree *tree = new TTree("tree", "tree using vector");
    tree->Branch("vec", &vec);

<vector>をincludeする :: namespaceを定義しない場合は、”std::vector<型 >
変数名”と宣言すること。当たり前のことだけど、結構忘れてしまう。
ROOT(CINT)を起動させると、“vector<型> 変数名”で使えてしまうため、
よく忘れる…orz vector型の変数は実体であるため、第２引数は先頭に
“&“が必要arrayと同じようにすると怒られるROOTが空気を読んでくれるた
め、第３引数はなくてよいみたいまぁでも一番最後のブランチにするのが
無難かも
