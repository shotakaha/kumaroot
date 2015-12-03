==================================================
TCanvas編
==================================================

色見本を見たい
==================================================

ROOTのプロンプト内で下のように入力すれば、簡単に確認できる。

.. code:: cpp

    root> TCanvas c
    root> c.DrawColorTable()

グラフの軸をログ表示にしたい
==================================================

.. code:: cpp

    TCanvas *c1;
    c1->SetLogy();


キャンバスを分割している場合
--------------------------------------------------


まず、分割したいキャンバスに移動する

.. code:: cpp

    c1->cd(2)->SetLogy();
    h1->Draw();

gPadは current canvas へのポインタなので、下のようにも書くことができる。

.. code:: cpp

    c1->cd(2);
    gPad->SetLogy();


複数のキャンバスをPDFに保存したい
==================================================

PDF形式で保存する場合のみ、複数のキャンバスを1つのPDFに書き出すことができる。
やったことないけれどPostScriptでもできるらしい。PNGはできない。

ROOT公式ユーザーズガイド “9. Graphics and the Graphical Userinterface :
The Postscript Interface” (p139)参照

.. code:: cpp

    TString name;
    name.Form("canv.pdf");
    TCanvas *c1 = new TCanvas(name.Data(), name.Data(), 1000, 500);

    c1->Print(name + "[", "pdf");    // ここで"canv.pdf"を開く感じ

    for (Int_t ihist = 0; ihist < Nhists; ihist++) {
        hist[ihist]->Draw();
        c1->Print(name, "pdf")       // ここで、キャンバスを保存する
    }
    c1->Print(name + "]", "pdf");    // ここで"canv.pdf"を閉じる感じ

最後の一文を以下のように変更すれば、別のTCanvasオブジェクトを追加し
て保存することができる。

.. code:: cpp

    c2->Print(name, "pdf")
    c2->Print(name + "]", "pdf")



括弧（ ``[`` と ``(`` ）の違いについて
--------------------------------------------------


``[``
    この時点ではページを出力しない
``(``
    この時点でページを出力する（空白のページができる？）
