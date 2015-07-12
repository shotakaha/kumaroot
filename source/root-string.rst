TString編
=========

C/C++では文字とか文字列の扱いは面倒くさいのですが、
ROOTにはTStringという便利なクラスがあります。
使わない手はないでしょう、ということで紹介しておきます。

フォーマット文字列を作りたい
----------------------------

.. code:: cpp

    TString str;
    str.Form("Hist%d", i);

文字列を取り出す
----------------

.. code:: cpp

    str.Data();

使い方の一例
------------

複数のヒストグラムをループで生成したいときなどによく使います。

.. code:: cpp

       const Int_t nhist = 10;
       TString hname, htitle;
       for (Int_t i = 0; i < nhist; i++) {
           hname.Form("h%02d", i);
           htitle.Form("%s;%s;%s", hname.Data(), "x", "y");
           h[i] = new TH1D(hname.Data(), htitle.Data(), xbin, xmin, xmax);
       }

