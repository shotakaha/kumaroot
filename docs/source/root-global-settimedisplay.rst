================================================================================
横軸に時間を使いたい（ ``SetTimeFormat`` , ``SetTimeDisplay`` ）
================================================================================

.. code:: cpp

    gStyle->SetTimeOffset(-788918400);    // set diff. btw Unix and ROOT epoch
    graph->GetXaxis()->SetTimeDisplay(1);
    graph->GetXaxis()->SetTimeFormat("%Y\/%m\/%d");
    graph->GetXaxis()->SetTimeOffset(0, "gmt");    // set GMT+0

Unixのepoch time は1970年01月01日00時00分00秒から始まるのに対し、
ROOTのepoch time は1995年01月01日00時00分00秒から始まるので、
その差をオフセットとして設定する必要がある。

Unix epoch と ROOTepochの差を計算する
==================================================

簡単な計算なので確かめてみる

.. code:: bash

        25[years] * 365[days/year * 24[hours/day] * 60[minutes/hour] * 60[seconds/minute]
        + 6[days] * 24[hours/day] * 60[minutes/hour] * 60[seconds/minutes]    // 6 leap year in 25 years
        = 788918400[seconds]


GMT+0に設定する
==================================================

.. code:: cpp

        graph->GetXaxis()->SetTimeOffset(0, "gmt");

理由は忘れてしまったが、上の設定をしないと軸の時間がずれてしまってたはず。
epochの時間ではなく、作成したグラフ／ヒストグラムの軸に対して設定する



月日と時刻を2段にして表示したい
==================================================

.. code:: cpp

        graph->GetXaxis()->SetTimeFormat("#splitline{/%m\/%d}{%H:%M}");

時間に対する安定性を示したい場合などに使える。
