ROOT tutorial 編
================

この章では、主にROOTに付属しているtutorialを使用して、使い方を簡単に紹介します。
前節の最後にも書きましたが、手元にコピーを作っておきましょう。

.. code:: bash

    $ cp -r /opt/local/libexec/root6/share/doc/root/tutorials ~/TEST/root6/

とりあえずROOT6のtutorialを使います。
気が向いたらROOT5との比較もしようかと思います。

とりあえず起動
--------------

.. code:: bash

    $ cd ~/TEST/root6/tutorials/
    $ root

    root[0]

コマンドラインで ``root`` と入力すると、ROOTが起動します。
この状態だと、対話的にROOTを操作することができます。

とりあえず終了
--------------

.. code:: bash

    root [0] .q

ROOTセッション内で ``.q`` を入力すると、ROOTが終了します。
それで終了しない場合は、``.qqq・・・`` の様に ``q`` をたくさんにします。

rootlogon.Cとrootlogoff.C
~~~~~~~~~~~~~~~~~~~~~~~~~

さて、tutorials をコピーしたディレクトリでROOTを起動／終了すると、
以下の様なメッセージが表示されたはずです。

.. code:: bash

    Welcome to the ROOT tutorials

    Type ".x demos.C" to get a toolbar from which to execute the demos

    Type ".x demoshelp.C" to see the help window

    ==> Many tutorials use the file hsimple.root produced by hsimple.C
    ==> It is recommended to execute hsimple.C before any other script

    root [0]

.. code:: bash

    Taking a break from ROOT? Hope to see you back!

これは、同じディレクトリに、 ``rooglogon.C`` と ``rootlogoff.C`` があるからです。
この２つのファイルを用意しておくことで、ROOT起動時および終了時の動作を設定することができます。

個人的には、数ヶ月ぶりに触るプログラムなんてほとんど忘れてしまっているので、
``rootlogon.C`` に手順を書いて残したりしています。


ROOT起動時に読み込まれるファイルの順番
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ROOT起動時に以下の順番でファイルが読み込まれます。

#. system.rootrc
#. ~/.rootrc
#. ./rootlogon.C

個人的な全体設定は ``~/.rootrc`` へ、
そのプログラムだけの設定は ``./rootlogon.C`` に書いておけばよいです。



demos.Cを実行してみる
---------------------

さて、ROOTを起動して表示されたメッセージにしたがって、 ``demos.C`` を実行してみましょう。
ROOT内で実行する場合は、 ``.x ファイル名`` と入力します。
ファイル名の部分は ``TAB補完`` ができます。
これをbashで実行する場合は以下のようにします。

.. code:: bash

    $ root demos.C

さてさて、実行すると図\ fig:demos\ のようなツールバーが出てきます。

.. figure:: ./fig/demos.png
   :alt: demos

   ``demos.C`` を実行した時に出てくるツールバー的なもの

一番上にある ``Help Demos`` をクリックすると、
図\ fig:helpdemos\ のようなキャンバスが表示されます。

.. figure:: ./fig/helpdemos.png
   :alt: helpdemos

   Help Demos を実行すると出てくるキャンバス
とりあえずこの通りにボタンを押してみましょう。

hsimple.Cを実行してみる
-----------------------

#+begin\ :sub:`src` sh $ root hsimple.C

#+end\ :sub:`src`

前節のようにボタンを押して実行するか、上の行の様にコマンドラインか
ら「hsimple.C」を走らせると、キャンバスが表示され、ヒストグラムが成
長していきます。それと同時に、「hsimple.root」というROOTファイルが
作成されます。

「hsimple.C」を開いて、上から順番に何をしているのかを確認してみましょ
う。

インクルードファイル
~~~~~~~~~~~~~~~~~~~~

とりあえず無視してOKです。コンパイルする場合は必要ですが、マクロで
動かす場合は書かなくてもよいです。

::

    #include <TFile.h>
    #include <TNtuple.h>
    #include <TH2.h>
    #include <TProfile.h>
    #include <TCanvas.h>
    #include <TFrame.h>
    #include <TROOT.h>
    #include <TSystem.h>
    #include <TRandom3.h>
    #include <TBenchmark.h>
    #include <TInterpreter.h>

関数の定義
~~~~~~~~~~

マクロの場合ファイル名と関数名は一緒にします。
戻り型はなんでもOKです。引数を指定することもできます。

::

    TFile *hsimple(Int_t get=0)

コメントの挿入
~~~~~~~~~~~~~~

コメントはC++の作法で挿入できます

::

    {
    //  This program creates :
    //    - a one dimensional histogram
    //    - a two dimensional histogram
    //    - a profile histogram
    //    - a memory-resident ntuple
    //
    //  These objects are filled with some random numbers and saved on a file.
    //  If get=1 the macro returns a pointer to the TFile of "hsimple.root"
    //          if this file exists, otherwise it is created.
    //  The file "hsimple.root" is created in $ROOTSYS/tutorials if the caller has
    //  write access to this directory, otherwise the file is created in $PWD

ファイル名の宣言
~~~~~~~~~~~~~~~~

TStringクラスという文字列クラスを使っています。
普通のC/C++の関数を使うよりはるかに楽なので、積極的に使うと良いと思います。

::

       TString filename = "hsimple.root";
       TString dir = gSystem->UnixPathName(__FILE__);
       dir.ReplaceAll("hsimple.C","");
       dir.ReplaceAll("/./","/");
       TFile *hfile = 0;
       if (get) {
          // if the argument get =1 return the file "hsimple.root"
          // if the file does not exist, it is created
          TString fullPath = dir+"hsimple.root";
          if (!gSystem->AccessPathName(fullPath,kFileExists)) {
             hfile = TFile::Open(fullPath); //in $ROOTSYS/tutorials
             if (hfile) return hfile;
          }
          //otherwise try $PWD/hsimple.root
          if (!gSystem->AccessPathName("hsimple.root",kFileExists)) {
             hfile = TFile::Open("hsimple.root"); //in current dir
             if (hfile) return hfile;
          }
       }
       //no hsimple.root file found. Must generate it !
       //generate hsimple.root in current directory if we have write access
       if (gSystem->AccessPathName(".",kWritePermission)) {
          printf("you must run the script in a directory with write access\n");
          return 0;
       }

ROOTファイルを開く
~~~~~~~~~~~~~~~~~~

TFileクラスを使います。直前のif文の中ではファイルの存在を確認して
います。ファイルがある場合は、TFile::Openメソッドでファイルを開い
ています。ない場合は、TFile::TFileコンストラクタで新しいTFileオブ
ジェクトを作成しています。

::

       TFile *hfile = 0;

       hfile = TFile::Open(fullPath); //in $ROOTSYS/tutorials
       hfile = TFile::Open("hsimple.root"); //in current dir

       hfile = (TFile*)gROOT->FindObject(filename); if (hfile) hfile->Close();
       hfile = new TFile(filename,"RECREATE","Demo ROOT file with histograms");

ヒストグラムを作成する
~~~~~~~~~~~~~~~~~~~~~~

TH1クラス、TH2クラスなどを使います。
ここでは、TProfileクラスやTNtupleクラスも使われています。

::

       // Create some histograms, a profile histogram and an ntuple
       TH1F *hpx = new TH1F("hpx","This is the px distribution",100,-4,4);
       hpx->SetFillColor(48);
       TH2F *hpxpy = new TH2F("hpxpy","py vs px",40,-4,4,40,-4,4);
       TProfile *hprof = new TProfile("hprof","Profile of pz versus px",100,-4,4,0,20);
       TNtuple *ntuple = new TNtuple("ntuple","Demo ntuple","px:py:pz:random:i");

プロセス時間の測定開始
~~~~~~~~~~~~~~~~~~~~~~

このマクロを実行すると、ターミナル上にプロセス時間が表示されます。
この部分から測定を開始しています。

::

       gBenchmark->Start("hsimple");

キャンバスの作成
~~~~~~~~~~~~~~~~

グラフを描く領域をキャンバスと呼びます。TCanvasクラスを使います。

::

       // Create a new canvas.
       TCanvas *c1 = new TCanvas("c1","Dynamic Filling Example",200,10,700,500);
       c1->SetFillColor(42);
       c1->GetFrame()->SetFillColor(21);
       c1->GetFrame()->SetBorderSize(6);
       c1->GetFrame()->SetBorderMode(-1);

ヒストグラムに値を詰める
~~~~~~~~~~~~~~~~~~~~~~~~

このマクロでは、ヒストグラムにランダムな値を詰め込んでいます。

::

       // Fill histograms randomly
       TRandom3 random;
       Float_t px, py, pz;
       const Int_t kUPDATE = 1000;
       for (Int_t i = 0; i < 25000; i++) {
          random.Rannor(px,py);
          pz = px*px + py*py;
          Float_t rnd = random.Rndm(1);
          hpx->Fill(px);
          hpxpy->Fill(px,py);
          hprof->Fill(px,pz);
          ntuple->Fill(px,py,pz,rnd,i);

キャンバスに描画する
~~~~~~~~~~~~~~~~~~~~

TH1::Draw()メソッドで描画します。

::

          if (i && (i%kUPDATE) == 0) {
             if (i == kUPDATE) hpx->Draw();
             c1->Modified();
             c1->Update();
             if (gSystem->ProcessEvents())
                break;
          }
       }

プロセス時間の表示
~~~~~~~~~~~~~~~~~~

::

       gBenchmark->Show("hsimple");

ROOTファイルに保存する
~~~~~~~~~~~~~~~~~~~~~~

::

       // Save all objects in this file
       hpx->SetFillColor(0);
       hfile->Write();
       hpx->SetFillColor(48);
       c1->Modified();
       return hfile;

    // Note that the file is automatically close when application terminates
    // or when the file destructor is called.
    }
