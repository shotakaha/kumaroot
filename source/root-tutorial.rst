==================================================
チュートリアル編
==================================================

ここではROOTに付属しているサンプルコードの使い方を簡単に紹介します。
使い方をウェブで検索してもよく分からない場合は、このサンプルコードを動かしながら中身をいじくってみるのが一番です。

まず、サンプルコードの場所を確認しておきましょう。

.. code-block:: bash

   $ locate tutorials | grep root5
   ## => /opt/local/libexec/root5/share/doc/root/tutorials/
   $ locate tutorials | grep root6
   ## => /opt/local/libexec/root6/share/doc/root/tutorials/


とりあえず、いつでも使えるようにテスト用ディレクトリを作成しコピーしておきましょう。
以下に一例を示しましたが、自分の環境に合わせて適宜変更してください。

.. code-block:: bash

    $ cp -r /opt/local/libexec/root5/share/doc/root/tutorials ~/TEST/root5/
    $ cp -r /opt/local/libexec/root6/share/doc/root/tutorials ~/TEST/root6/

:command:`cp` コマンドを使う際には :command:`-r` オプションを付けることでサブディレクトリもコピーできます。
その際、コピー元（＝第１引数）の最後に :file:`/` を付けてはダメです。
コピー先（＝第２引数）の最後には :file:`/` を付けてもよいです。


この文書では ROOT6のチュートリアルを使うことにします。
以降、このディレクトリを ``$TUTORIALS`` とします。

.. todo::

   気が向いたらROOT5と比較しようかと思います。

.. toctree::

   root-tutorial-start
   root-tutorial-quit
   root-tutorial-logon-logoff
   root-tutorial-demos
   root-tutorial-hsimple
