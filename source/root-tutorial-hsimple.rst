==================================================
hsimple.Cを実行してみる（ ``$ root hsimple.C`` ）
==================================================

前項のようにボタンを押して実行するか、
コマンドラインで ``$ root hsimple.C`` を実行します。
すると、キャンバスが表示され、ヒストグラムが成長していきます（ :numref:`fig-hsimple` ）。
それと同時に、 ``hsimple.root`` というROOTファイルが作成されます。

.. _fig-hsimple:

.. figure:: ./root-tutorial/hsimple.png

   ``hsimple`` を実行した時に表示されるキャンバス


それでは ``hsimple.C`` を開いて、
上から順番に何をしているのかを確認してみましょう。


インクルードファイル（ ``#include`` ）
--------------------------------------------------

``#include`` で始まるのはインクルードファイルです。
コンパイルする場合は必須ですが、マクロで動かす場合は書かなくてもよいです。
なので今は無視します。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 1-11
   :lineno-start: 1


関数の定義
--------------------------------------------------

マクロの場合ファイル名と関数名は一緒にします。
戻り型はなんでもOKです。引数を指定することもできます。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 13
   :lineno-start: 13


コメントの挿入（ ``//`` ）
--------------------------------------------------

コメントはC++の作法で挿入できます。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 14-25
   :lineno-start: 14


ファイル名の宣言（ ``TString`` ）
--------------------------------------------------

TStringクラスという文字列クラスを使っています。
普通のC/C++の関数を使うよりはるかに楽なので、積極的に使うと良いと思います。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 27-51
   :lineno-start: 27


ROOTファイルを開く（ ``TFile`` ）
--------------------------------------------------

``TFile`` クラスを使います。
直前の ``if`` 文の中ではファイルの存在を確認しています。
ファイルがある場合は、 ``TFile::Open`` メソッドでファイルを開いています。
ない場合は、 ``TFile::TFile`` コンストラクタで
新しい ``TFileオブジェクト`` を作成しています。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 31,37,42,52-53



ヒストグラムを作成する
--------------------------------------------------

``TH1`` クラス、 ``TH2`` クラスなどを使います。
ここでは ``TProfile`` クラスや ``TNtuple`` クラスも使われています。


.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 55-60
   :lineno-start: 55


プロセス時間の測定開始・表示（ ``gBenchmark`` ）
--------------------------------------------------

このマクロを実行すると、ターミナル上にプロセス時間が表示されます。
この部分から測定を開始しています。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 62,92


キャンバスの作成（ ``TCanvas`` ）
--------------------------------------------------

グラフを描く領域をキャンバスと呼びます。
``TCanvas`` クラスを使います。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 64-69
   :lineno-start: 64



ヒストグラムに値を詰める（ ``Fill`` ）
--------------------------------------------------

このマクロでは、ヒストグラムにランダムな値を詰め込んでいます。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 72-83
   :lineno-start: 72


キャンバスに描画する（ ``Draw`` ）
--------------------------------------------------

TH1::Draw()メソッドで描画します。

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 84-91
   :lineno-start: 84



ROOTファイルに保存する（ ``Write`` ）
--------------------------------------------------

.. literalinclude:: ./tutorials/root6/hsimple.C
   :language: cpp
   :lines: 94-103
   :lineno-start: 94
