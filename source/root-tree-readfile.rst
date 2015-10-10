======================================================================
テキストファイルをTTreeに変換したい（１）（ ``TTree::ReadFile`` ）
======================================================================

.. code-block:: cpp

    Long64_t ReadFile(const char* filename, const char* branchDescriptor = "", char delimiter = ' ')

filename
    入力ファイル名
branchDescriptor
    入力ファイルの構造指定。「:」で区切る
delimiter
    こんなのあったんだ

学生実験や小さなテストベンチで行う実験の場合、取得したデータはとり
あえずテキストファイルで出力することになると思います。ROOTで解析す
るときはTTreeになっていると楽ちんなので、手間を掛けずにさっさと変換
してしまいましょう。

入力ファイルの構造は「branchDescriptor」で、TTreeに教えてあげます。

第１引数
    入力ファイル名
第２引数
    branch descriptor。TTreeのブランチ変数になります。複
    数のブランチ変数を指定する場合は、コロン（:）で区切っ
    て記述します。Int\ :sub:`t型の場合は`\ 「ブランチ名/I」、
    Double\ :sub:`t型の場合は`\ 「ブランチ名/D」といった感じで、そ
    の変数名（＝ブランチ名）とその型を指定できます。型を
    省略した場合はFloat\ :sub:`t型の`\ 「ブランチ名/F」になるみた
    いです。

サンプルコード
^^^^^^^^^^^^^^

仮に、100行４列のテキストファイルがあるとします。
このファイルの「行数」はイベント数に相当し、「列数」は取得したデータの項目に相当します。

.. code:: example

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
