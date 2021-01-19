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

   root-tutorial-hsimple-include
   root-tutorial-hsimple-macroname
   root-tutorial-hsimple-comment
   root-tutorial-hsimple-string
   root-tutorial-hsimple-openfile
   root-tutorial-hsimple-histogram
   root-tutorial-hsimple-benchmark
   root-tutorial-hsimple-canvas
   root-tutorial-hsimple-fill
   root-tutorial-hsimple-draw
   root-tutorial-hsimple-write
