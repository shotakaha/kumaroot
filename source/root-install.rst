ROOTのインストール
==================

ROOTのインストールする方法と
ROOTのチュートリアルの存在について紹介しておきます。

オススメのインストール方法（for Mac ユーザ）
--------------------------------------------

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
そのため、進行中の実験は ``ROOT5`` 系を使っていることが多いです [1]_
むやみに最新版を使うと、実験固有のソフトウェア群が動作しないこともあります。
その場合は、素直に実験で推奨されているバージョンには従ってください。


.. [1] LHC実験の要求に応えるため（？）、３年位前から ``ROOT`` の開発が非常に活発に行われています。
       しかし、その他の実験では、安定性を求め古いバージョン使い続けていることがあります。
       あとOSが古いと最新バージョンはうまくインストールできないこともあります。


Git を使ったインストール方法
----------------------------

Linuxを使っている場合は、Gitを使うとよいでしょう。
方法は
「 `installing-root-source | ROOT公式ページ <https://root.cern.ch/drupal/content/installing-root-source>`__ 」
に載っている通りです。

STEP1
    ROOTのリポジトリをクローンします

.. code-block:: bash

    [any]  $ mkdir ~/repos/git
    [any]  $ cd ~/repos/git
    [git]  $ git clone http://root.cern.ch/git/root.git
    [git]  $ cd root

STEP2
    どんなタグがあるのかを調べて、チェックアウトします。
    ブランチ名は好きにして大丈夫です
    （今回は、タグ名と同じ名前にしています）

.. code-block:: bash

    [root] $ git tag -l
    [root] $ git checkout -b v5-34-08 v5-34-08

STEP5
    従来通りPREFIXを指定してconfigureします。
    失敗した場合に備えてログを残しておきます

.. code-block:: bash

    [root(v5-34-08)] $ ./configure --prefix=/usr/local/heplib/ROOT/v5-34-08
    [root(v5-34-08)] $ make 2>&1 | tee make.log                   ## buiding ROOT
    [root(v5-34-08)] $ make install 2>&1 | tee makeinstall.log    ## installed under $PREFIX

-  ``configure`` の内容は ``config.status`` に書き出されます。
-  ``make`` 、 ``make install`` の際、 ``PREFIX`` で指定したディレクトリによっては ``sudo`` が必要になります。
-  ログを取る場合は、 ``tee`` コマンドを使うと端末に表示しながらログファイルに保存できます。
-  ``~/.bashrc`` に環境変数の設定を書いておきます。


従来のインストール方法
~~~~~~~~~~~~~~~~~~~~~~

ググればたくさん出てきますが、一応紹介しておきます。

.. code-block:: bash

    ## STEP1 : make directory for tar.gz file and wget it
    $ cd /usr/local/heplib/tarballs
    $ wget ftp://root.cern.ch/root/root_v5.30.06.source.tar.gz    ## check URL at ROOT website

    ## STEP2 : expand tar.gz
    [ROOT] $ cd /usr/loca/heplib/ROOT
    [ROOT] $ tar zxvf ../tarballs/root_v5.30.06.source.tar.gz

    ## STEP3 : set PREFIX then configure -> make -> make install
    [ROOT] $ cd root
    [root] $ ./configure --prefix=/usr/local/heplib/ROOT/v5-30-06
    [root] $ make 2>&1 | tee make.log
    [root] $ make install 2>&1 | tee makeinstall.log


インストール方法 for Windows ユーザ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windowsはよく分かりません。ごめんなさい。たぶん
「 `downloading-root | ROOT公式ページ <https://root.cern.ch/drupal/content/downloading-root>`__ 」
から目的のバージョンを選び、バイナリを落としてくるのが一番簡単だと思います。


ROOT5 と ROOT6 を試してみたい
-----------------------------

.. code-block:: bash

    $ sudo port select root root6   ## use ROOT6
    $ sudo port select root root5   ## use ROOT5

MacPortsでROOTをインストールする利点のひとつは、
``ROOT5`` と ``ROOT6`` が簡単に切り替えられることです。

実はこの ``port select`` はROOTだけでなく、
Pythonのバージョン切り替えなどもできます。
どのパッケージが使えるかは以下のコマンドで確認できます

.. code-block:: bash

    $ port select --summary


ROOT5 と ROOT6 の違いについて
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ROOTマクロなどを実行する際に使うインタプリタが変更されたみたいです [2]_ 。
細かい違いは全く分かりませんが、文法のチェックが厳密になったみたいです。

実は ``ROOT5`` ではC言語／C++言語の文法的には間違っているマクロでも動いてくれました [3]_ 。
そのため、テストで作ったマクロで動作確認した後、
より多くのデータを解析するためにコンパイルするとエラーが多出。
そのデバッグに追われるということは日常茶飯事でした。

``ROOT6`` では、このマクロの文法チェックも厳しくなったみたいです。ひぇぇ。
でも心配しなくて大丈夫。エラーの内容を詳しく教えてくれるようになりました。
よくある行末のセミコロンのつけ忘れなども指摘してくれます。
これで場所の分からない ``segmentation fault`` に悩まされることも減るでしょう。

どんな風に厳しくなったかを実感するために、試しに
``ROOT5`` のチュートリアルを ``ROOT6`` で実行してみましょう。
``warning`` や ``error`` がたくさん表示されます。

.. code-block:: bash

    $ sudo port select root root6    # ROOT6に切り替える
    $ cd /opt/local/libexec/root5/share/doc/root/tutorials/    # ROOT5のチュートリアルに移動
    $ root    # ROOT6を起動

    ## ===  an example of warning ===
    /opt/local/libexec/root5/share/doc/root/tutorials/rootalias.C:7:13:
     warning: using the result of an assignment as a condition without
     parentheses [-Wparentheses]
          if (e = getenv("EDITOR"))
              ~~^~~~~~~~~~~~~~~~~~
    ## === an example of error ===
    /opt/local/libexec/root5/share/doc/root/tutorials/rootalias.C:39:12:
     error: cannot initialize return object of type 'char *' with an rvalue of
     type 'const char *'
        return gSystem->WorkingDirectory();
               ^~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ .q    # ROOTを終了


.. [2] CINT \\rightarrow CINT++に変更

.. [3] よく知られていると思われるのは、a.b でも a->bでも動いちゃうことでしょうか



PyROOTを使いたい
----------------

.. code-block:: bash

    $ sudo port install root5 +python27   ## when ROOT5, you need to specify +pythonXX variants
    $ sudo port install root6             ## when ROOT6, no need to specify variants

CERNには「へびつかい」が多いそうです。
``PyROOT`` というモジュールを使えば、Python上でROOTが使えます。
その場合は、MacPortsでインストールする際に ``variants`` で
``+pythonXX``を指定する必要があります。
しかも、この ``variants`` は自分の使っているPythonの
バージョンに合わせる必要があります。
ミスマッチな場合は、動作せず、クラッシュします。

``ROOT6`` の場合は ``python27`` がデフォルトでONになっています。

他にも `rootpy <http://www.rootpy.org>`__ というのもあります。
こっちのほうがPython nativeな感じです。
前に試そうとしてたのですがインストールでコケてしまいました。
動かせたら項目を作るかも。


EmacsでROOTを編集したい
-----------------------

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
------------------------

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
