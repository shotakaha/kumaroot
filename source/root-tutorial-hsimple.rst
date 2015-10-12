==================================================
hsimpleを実行（ :command:`.x hsimple.C` ）
==================================================

前ページのように ``Demos ツールバー`` の ``hsimple`` ボタンを押すか、CINTで :command:`.x hsimple.C` と入力するか、シェルのコマンドラインに :command:`root hsimple.C` を入力して ``hsimple`` を実行します。

実行すると :numref:`fig-hsimple` のように ``Dynamic Filling Example`` というタイトルのキャンバスが表示され、ヒストグラムが成長していきます
それと同時に、 ``hsimple.root`` というROOTファイルが作成されます。

.. _fig-hsimple:
.. figure:: ./root-tutorial/hsimple.png
   :align: center

   ``hsimple`` を実行した時に表示されるキャンバス


次ページからは :file:`hsimple.C` の中身を見ながら、どうやってこのヒストグラムを作成しているのかは確認していきます。


.. toctree::

   root-tutorials-hsimple-include
   root-tutorials-hsimple-macroname
   root-tutorials-hsimple-comment
   root-tutorials-hsimple-string
   root-tutorials-hsimple-openfile
   root-tutorials-hsimple-histogram
   root-tutorials-hsimple-benchmark
   root-tutorials-hsimple-canvas
   root-tutorials-hsimple-fill
   root-tutorials-hsimple-draw
   root-tutorials-hsimple-write
