==================================================
TTreeを作成したい（ ``TTree::Tree`` ）
==================================================

.. code:: cpp

    TTree *t = new TTree("t1", "TTree example");

.. code:: cpp

    TTree TTree(const char* name, const char* title, Int_t splitlevel = 99)


.. list-table::
   :header-rows: 1

   * - 変数
     - 説明
   * - name
     - TTreeオブジェクトの名前
   * - title
     - TTreeの説明
   * - splitlevel
     - 使ったことがない

第１引数（ ``name`` ）はTTreeオブジェクトの名前

name
    TTreeオブジェクトの名前。他のオブジェクトと重複しないようにする
title
    TTreeの説明。TFileに保存したときに表示される
splitlevel
    使ったことがない

    「name」はオブジェクトの名前です。他のオブジェクトと重複しないよう
    にしましょう。「title」はTFileを覗いた時に表示されるTTreeの説明です。
    １行くらいの簡単な説明をきちんと付けておくとあとで自分自身を救うこ
    とになると思います。「splitlevel」は指定したことがありません。デフォ
    ルト値で大丈夫です。
