==================================================
TTreeを作成したい（ ``TTree::Tree`` ）
==================================================

.. code:: cpp

    TTree *t = new TTree("t1", "TTree example");

.. code:: cpp

    TTree TTree(const char* name,
                const char* title,
                Int_t splitlevel = 99)


.. list-table::
   :header-rows: 1

   * - 変数
     - 説明
   * - ``name``
     - TTreeオブジェクトの名前
   * - ``title``
     - TTreeの説明
   * - ``splitlevel``
     - 使ったことがない


``name`` はオブジェクトの名前です。
他のオブジェクトと重複しないようにします。

``title`` はTFileを覗いた時に表示されるTTreeの説明です。
１行くらいの簡単な説明をきちんと付けておくと、あとで自分自身を救うことになると思います。

``splitlevel`` は指定したことがありません。
なのでデフォルト値で大丈夫です。
