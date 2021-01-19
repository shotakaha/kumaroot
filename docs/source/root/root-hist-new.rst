==================================================
１次元ヒストグラムを作成したい（ ``TH1D`` ）
==================================================

.. code:: cpp

   TString hname, htitle;
   hname.Form("hname");
   htitle.Form("title;xtitle;ytitle;");
   Double_t xmin = 0, xmax = 100;
   Int_t xbin = (Int_t)xmax - (Int_t)xmin;

   TH1D *h1 = new TH1D(hname.Data(), htitle.Data(), xbin, xmin, xmax);


ヒストグラムには **（オブジェクトの）名前** が必要です。
これは **他のどのオブジェクトとも重ならないように** します。

タイトルの文字列を **"全体のタイトル;X軸名;Y軸名"** と ";" で区切ることでX軸、Y軸を同時に設定することができます。


Fill
    ヒストグラムに値を詰めるメソッド
Draw
    ヒストグラムを描くメソッド。描画のオプションを設定できる。

.. code:: cpp

    TString hname, htitle;
    hname.Form("hname");    // <------------------------ object name of histogram
    htitle.Form("title;xtitle;ytitle;");    // <-------- title and axis name
    Double_t xmin = 0, xmax = 10;    // <--------------- left edge and right edge
    Int_t xbin = (Int_t)xmax - (Int_t)xmin;    // <----- number of bins

    TH1D *h1 = new TH1D(hname.Data(), htitle.Data(), xbin, xmin, xmax);

-  ヒストグラムに限らずROOTオブジェクトには「名前」をセットする必要がある
-  タイトル部分を「;」で区切ることで、軸名を設定することができる（"タイトル;X軸名;Y軸名前"）
-  TString::Form は printf の書式が使えるのでとても便利


==================================================
２次元ヒストグラムを作成したい（ ``TH2D`` ）
==================================================

.. code:: cpp

    TH2D TH2D(const char* name, const char* title, Int_t nbinsx, Double_t xlow, Double_t xup, Int_t nbinsy, Double_t ylow, Double_t yup)
    Int_t Fill(Double_t x, Double_t y)
    void Draw(Option_t* option = "")
