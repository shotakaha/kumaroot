======================================================================
テキストファイルをTTreeに変換したい（１）（ ``TTree::ReadFile`` ）
======================================================================

.. code-block:: cpp

    Long64_t ReadFile(const char* filename,
                      const char* branchDescriptor = "",
                      char delimiter = ' ')

.. list-table::
   :header-rows: 1

   * - 変数
     - 説明
   * - ``filename``
     - 入力ファイル名
   * - ``branchDescriptor``
     - 入力ファイルの書式指定
   * - ``delimiter``
     - こんなのあったんだ

``filename`` には読み込むファイル名を指定します。
連番ファイルを読む場合は、後述する TString を使うと楽になったりします。
ファイルの中身の書式は次の ``branchDescriptor`` で指定します。

``branchDescriptor`` はTTreeのブランチ変数になります。
複数のブランチ変数を指定する場合は、コロン（:）で区切って記述します。
``Int_t型`` の場合は ``ブランチ名/I`` 、 ``Double_t型`` の場合は ``ブランチ名/D`` といった感じで、
その変数名（＝ブランチ名）とその型を指定します。
型を省略した場合は ``Float_t型`` の ``ブランチ名/F`` になるらしいです。

学生実験や小さなテストベンチで行う実験の場合、取得したデータはとり
あえずテキストファイルで出力することになると思います。ROOTで解析す
るときはTTreeになっていると楽ちんなので、手間を掛けずにさっさと変換
してしまいましょう。


サンプルコード
==================================================

仮に、100行４列のテキストファイルがあるとします。
このファイルの「行数」はイベント数に相当し、「列数」は取得したデータの項目に相当します。

.. code:: text

    100    105    104   103
    101    106    103   100
    ...

.. code:: cpp

    {
      // STEP1: Set input filename
      TString ifn = "inputfilename";

      // STEP2: Create TTree
      TTree *tree = new TTree("tree", "tree using ReadFile()");

      // STEP3: Read data using TTree::ReadFile(...) method
      tree->ReadFile(ifn.Data(), "row1/I:row2/I:row3/I:row4/D:row5/I");

      // STEP4: Create TFile to save TTree
      TString ofn = "out.root";
      TFile *fout = new TFile(ofn, "recreate");

      // STEP5: Write TTree to TFile
      tree->Write();

      // STEP6: Close TFile
      fout->Close();

      return;
    }
