==================================================
インストール
==================================================

はじめにROOTをインストールする方法と
ROOTのチュートリアルの存在について紹介しておきます。


オススメのインストール方法（for Mac ユーザ）
==================================================

.. code-block:: bash

    $ sudo port install root5    ## for ROOT5 user
    $ sudo port install root6    ## for ROOT6 user

Macユーザは ``MacPorts`` からインストールできます。
すごく楽ちんなのでオススメです。
環境変数（ ``$ROOTSYS`` 、 ``$LD_LIBRARY_PATH`` 、 ``$DYLD_LIBRARY_PATH`` など）の設定も不要です。
``Homebrew`` や ``fink`` など、その他のパッケージ管理ツールは使ったことがないので分かりません。
誰か情報をくださいな。

``ROOT6`` は2014年頃にリリースされました。
MacPortsの場合 ``root6`` というポート名（パッケージ名）でインストールすることができます。
``ROOT5`` と一緒にインストールすることができますが、一緒には使えません。
簡単に切り替える方法は後述します。

現在は ``ROOT5`` から ``ROOT6`` へ移行する過渡期です。
そのため、進行中の実験は ``ROOT5`` 系を使っていることが多いです [#]_
むやみに最新版を使うと、実験固有のソフトウェア群が動作しないこともあります。
その場合は、素直に実験で推奨されているバージョンには従ってください。


.. [#] LHC実験が開始してから ``ROOT`` の開発が非常に活発に行われています。
       しかし、その他の実験では、安定性を求め古いバージョン使い続けていることがあります。
       あとOSが古いと最新バージョンはうまくインストールできないこともあります。


ROOT5 と ROOT6 を試してみたい
==================================================

.. code-block:: bash

    $ sudo port select root root6   ## use ROOT6
    $ sudo port select root root5   ## use ROOT5

MacPortsでROOTをインストールする利点のひとつは、
``ROOT5`` と ``ROOT6`` が簡単に切り替えられることです。

実はこの :command:`port select` はROOTだけでなく、
Pythonのバージョン切り替えなどもできます。
どのパッケージが使えるかは以下のコマンドで確認できます

.. code-block:: bash

    $ port select --summary


ROOT5 と ROOT6 の違いについて
==================================================

ROOTマクロなどを実行する際に使うインタプリタが ``CINT`` から ``CINT++`` に変更されました。
細かい違いは全く分かりませんが、文法のチェックが厳密になったみたいです。

実は ``ROOT5`` ではC言語／C++言語の文法的には間違っているマクロでも動いてくれました [#]_ 。
そのため、テストで作ったマクロで動作確認した後、
より多くのデータを解析するためにコンパイルするとエラーが多出。
そのデバッグに追われるということが多々ありました。

``ROOT6`` では、このマクロの文法チェックも厳しくなったようです。
その証拠に、試しに ``ROOT5`` のチュートリアルを ``ROOT6`` で実行してみると、
``warning`` や ``error`` がたくさん表示されます。

また、エラーの内容を詳しく教えてくれるようになっています。
やってしまいがちな行末のセミコロンのつけ忘れなども指摘してくれるので、
これで場所の分からない ``segmentation fault`` に悩まされることも減るかもしれません。

.. [#] よく知られていると思われるのは、a.b でも a->bでも動いちゃうことでしょうか


PyROOTを使いたい
==================================================

.. code-block:: bash

    $ sudo port install root5 +python27   ## when ROOT5, you need to specify +pythonXX variants
    $ sudo port install root6             ## when ROOT6, no need to specify variants


``PyROOT`` というモジュールを使えば、Python上でROOTが使えます。
その場合は、MacPortsでインストールする際に ``variants`` で
``+pythonXX`` を指定する必要があります。
しかも、この ``variants`` は自分の使っているPythonの
バージョンに合わせる必要があります。
ミスマッチな場合は、動作せず、クラッシュします。

``ROOT6`` の場合は ``python27`` がデフォルトでONになっています。

他にも `rootpy <http://www.rootpy.org>`__ というのもあります。
こっちのほうがPython nativeな感じです。
前に試そうとしてたのですがインストールでコケてしまいました。
動かせたら項目を作るかも。


EmacsでROOTを編集したい
==================================================

.. code-block:: bash

    $ locate root-help.el    # check path

これもあまり知られていないと思うのですが、
Emacs上でROOTのソースを編集するのを簡単にする
Elispパッケージが一緒にインストールされます。

locateコマンドでどこにあるか調べておきましょう。
ちなみに、僕の場合（＝MacPortsの場合）、以下にありました。

.. code-block:: bash

   ## ROOT5
   /opt/local/libexec/root5/share/emacs/site-lisp/root-help.el
   ## ROOT6
   /opt/local/libexec/root6/share/emacs/site-lisp/root-help.el

これの使い方に関しては、あとできちんと調べて書くことにします。


ROOTのtutorialを使いたい
==================================================

.. code-block:: bash

   ## ROOT5
   /opt/local/libexec/root5/share/doc/root/tutorials/
   ## ROOT6
   /opt/local/libexec/root6/share/doc/root/tutorials/

実はROOTをインストールすると、たくさんのサンプルコードもついてきま
す。使い方をウェブで検索してもよく分からない場合は、このサンプルコー
ドを動かしながら中身をいじくってみるのが一番です。

とりあえず、いつでも使えるようにテスト用ディレクトリを作成しコピー
しておきましょう。以下に一例を示しましたが、自分の環境に合わせて適
宜変更してください。

.. code-block:: bash

    $ cp -r /opt/local/libexec/root5/share/doc/root/tutorials ~/TEST/root5/
    $ cp -r /opt/local/libexec/root6/share/doc/root/tutorials ~/TEST/root6/

``cp`` コマンドを使う際には、 ``-r`` オプションを付けることでサブディレクトリもコピーできます。
その際、コピー元（＝第１引数）の最後に ``/`` を付けてはダメです。
コピー先（＝第２引数）の最後には ``/`` を付けてもよいです [4]_ 。


.. [4] この辺はよく忘れます。分からなかったら ``man cp`` などで確認しましょう。
       あと、失敗したらコピー先を削除すればいいだけなので、とりあえずやってみてもいいかも。
