==================================================
準備
==================================================

まず、サンプルコードの場所を確認し、いつでも使えるようにテスト用ディレクトリを作成し、コピーしておきましょう。
以下に例を示しておきますが、自分の環境に合わせて適宜変更してください。

- ROOT6

.. code-block:: bash

   $ locate tutorials | grep root6
   ## => /opt/local/libexec/root6/share/doc/root/tutorials/
   $ mkdir -p ~/TEST/root6
   $ cp -r /opt/local/libexec/root6/share/doc/root/tutorials ~/TEST/root6/


- ROOT5

.. code-block:: bash

   $ locate tutorials | grep root5
   ## => /opt/local/libexec/root5/share/doc/root/tutorials/
   $ mkdir -p ~/TEST/root5
   $ cp -r /opt/local/libexec/root5/share/doc/root/tutorials ~/TEST/root5/


- :command:`mkdir` と :command:`cp` のオプション

  - :command:`mkdir -p` とすると、その深さのディレクトリまで一気に作ってくれます。
  - :command:`cp -r` とすると、サブディレクトリをコピーできます。
    その際、コピー元（＝第１引数）の最後に :file:`/` を付けてはダメです。
    コピー先（＝第２引数）の最後には :file:`/` を付けてもよいです。


.. note::
   この文書では ROOT6のチュートリアルを使うことにします。
   以降、このディレクトリを ``$TUTORIALS`` とします。
