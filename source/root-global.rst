================================================================================
全体設定編（ ``gROOT`` , ``gStyle`` , ``gSystem`` ）
================================================================================


.. toctree::
   :maxdepth: 1

   root-global-rootrc
   root-global-setstyle
   root-global-setoptstat
   root-global-setoptfit





ヒストグラムの線の太さを一括で変更したい（ ``gStyle->SetHistLineWidth`` ）
================================================================================

ヒストグラムの外枠線の太さは、一括で設定しておくことができます。デ
フォルトだと少し細い気がするので、太くしておくとよいと思います。た
だし、たくさんのヒストグラムを描く際は、見えにくくなってしまうので
細くします。その辺りは臨機応変にお願いします。

.. code:: cpp

    gStyle->SetHistLineWidth(2)



デフォルトの色を変更したい（ ``gROOT->GetColor->SetRGB`` ）
================================================================================

.. code:: cpp

    gROOT->GetColor(3)->SetRGB(0., 0.7, 0.); // Green  (0, 1, 0)->(0, 0.7, 0)
    gROOT->GetColor(5)->SetRGB(1., 0.5, 0.); // Yellow (1, 1, 0)->(1, 0.5, 0)
    gROOT->GetColor(7)->SetRGB(0.6, 0.3, 0.6); // Cyan (0, 1, 1)->(0.6, 0.3, 0.6)

デフォルトは
（1:黒, 2:赤, 3:黄, 4:青, 5:黄緑, 6:マゼンダ, 7:シアン）なのですが、
この中で、
（3:黄, 5:黄緑, 7:シアン）は明るすぎてとても見えづらいので、
もう少し見やすい色に変更します。

上２つは奥村さんのページのコピペ、最後のはシアンを紫っぽい色に変更しました。

RGBの度合いは自分の好みで選んでください。
手順としては、RGBの値を検索（Wikipedia使用すると良い）->
その値を256（ほんとは255かも？）で割るだけです。

おまけとして、ROOT公式ブログの
「 `虹色カラーマップを使うこと <http://root.cern.ch/drupal/content/rainbow-color-map>`__ 」
の記事もリンクしておきます。


横軸に時間を使いたい（ ``SetTimeFormat`` , ``SetTimeDisplay`` ）
======================================================================

.. code:: cpp

    gStyle->SetTimeOffset(-788918400);    // set diff. btw Unix and ROOT epoch
    graph->GetXaxis()->SetTimeDisplay(1);
    graph->GetXaxis()->SetTimeFormat("%Y\/%m\/%d");
    graph->GetXaxis()->SetTimeOffset(0, "gmt");    // set GMT+0

Unixのepoch time は1970年01月01日00時00分00秒から始まるのに対し、
ROOTのepoch time は1995年01月01日00時00分00秒から始まるので、
その差をオフセットとして設定する必要がある。

Unix epoch と ROOTepochの差を計算する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

簡単な計算なので確かめてみる

.. code:: bash

        25[years] * 365[days/year * 24[hours/day] * 60[minutes/hour] * 60[seconds/minute]
        + 6[days] * 24[hours/day] * 60[minutes/hour] * 60[seconds/minutes]    // 6 leap year in 25 years
        = 788918400[seconds]


GMT+0に設定する
~~~~~~~~~~~~~~~

.. code:: cpp

        graph->GetXaxis()->SetTimeOffset(0, "gmt");

理由は忘れてしまったが、上の設定をしないと軸の時間がずれてしまってたはず。
epochの時間ではなく、作成したグラフ／ヒストグラムの軸に対して設定する



月日と時刻を2段にして表示したい
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: cpp

        graph->GetXaxis()->SetTimeFormat("#splitline{/%m\/%d}{%H:%M}");

時間に対する安定性を示したい場合などに使える。



キャンバスに補助線を描きたい（ ``gStyle->SetPadGridX`` ）
================================================================================

.. code:: cpp

       gStyle->SetPadGridX(1)    // X-axis grid
       gStyle->SetPadGridY(1)    // Y-axis grid


グラフの軸を一括してログ表示にする（ ``gStyle->SetOptLogx`` ）
================================================================================

.. code:: cpp

       gStyle->SetOptLogx(1)    // X-axis
       gStyle->SetOptLogy(1)    // Y-axis



軸の目盛り間隔を変更したい（ ``gStyle->SetNdivisions`` ）
================================================================================

.. code:: cpp

       gStyle->SetNdivisions(TTSSPP)


.. list-table::
   :widths: 1 9
   :header-rows: 0

   * - PP
     - 軸全体の分割数
   * - SS
     - PP分割された目盛り１つ分の分割数
   * - TT
     - SS分割された目盛り１つ分の分割数


デフォルトは510になっている。
PP=10、SS=05、TT=00なので、軸を10分割してその１目盛りを5分割、
ということで全体で50目盛りになる。

全体を100目盛りにするには、20510にすればよい。
（10分割、その１目盛りを5分割、さらにその1目盛りを2分割 ＝100目盛り）
