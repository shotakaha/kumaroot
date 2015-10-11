================================================================================
デフォルトの色を変更したい（ ``gROOT->GetColor->SetRGB`` ）
================================================================================

.. code:: cpp

   gROOT->GetColor(3)->SetRGB(0.00, 0.70, 0.00); // Bright Green -> Green
   gROOT->GetColor(5)->SetRGB(1.00, 0.50, 0.00); // Bright Yellow -> Orange
   gROOT->GetColor(7)->SetRGB(0.15, 0.29, 0.56); // Bright Cyan -> China Blue
   gROOT->GetColor(8)->SetRGB(0.22, 0.37, 0.04); // Dull Green -> Leaf Green
   gROOT->GetColor(9)->SetRGB(0.50, 0.30, 0.70); // Dull Navy -> Purple


ROOTのデフォルト配色は、蛍光が強すぎてとてもとても見えにくい色が何色かあります。
それらを、以下のようにもう少し落ち着いた色に変更します。


.. list-table::
   :header-rows: 1

   * - 番号
     - デフォルト色
     - 変更後の色
   * - 1
     - 黒
     -
   * - 2
     - 赤
     -
   * - 3
     - 緑（蛍光）
     - 緑
   * - 4
     - 青
     -
   * - 5
     - 黄（蛍光）
     - 橙
   * - 6
     - マゼンタ
     -
   * - 7
     - シアン（蛍光）
     - China Blue
   * - 8
     - Dull Green
     - Leaf Green
   * - 9
     - Dull Navy
     - Purple
   * - 10
     - 白
     - Purple



上２つは奥村さんのページのコピペ、最後のはシアンを紫っぽい色に変更しました。

RGBの度合いは自分の好みで選んでください。
手順としては、RGBの値を検索（Wikipedia使用すると良い）->
その値を256（ほんとは255かも？）で割るだけです。

.. note::

   `虹色カラーマップを使うこと - ROOT公式ブログ <http://root.cern.ch/drupal/content/rainbow-color-map>`__
