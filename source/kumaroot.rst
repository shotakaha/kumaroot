Emacs + Prelude
~~~~~~~~~~~~~~~

Emacsの設定を一からするのってめんどくさいですよね。
そんな場合はとりあえずググってみましょう。いろんな人が、いろんな形で公開しています。

Preludeもその１つで、GitHubで公開されています。いろいろあって違い
がよく分からなかったので、名前がかっこいいなーと思ってこれに決めま
した。ほんとそれだけです。

複数のマシンで同じEmacs設定を使いたい場合は、Preludeを自分のGitHub
にForkして、Cloneするとよいと思います。

LaTeX
-----

ほとんどの人は修論の時にLaTeXをがしがし使うことになると思います。そ
の時に「インストールできないー」などと焦っていては時既に時間切れ
 [12]_なので、簡単 にまとめておきます。

MacTeXを使おう
~~~~~~~~~~~~~~

MacOSXでLaTeXを使う場合は、これで決まりです。
TeX環境の本体であるTeXLiveと一緒に、TeX編集の統合環境である
TeXShop [13]_やTeXworks、TeX関連のパッケージ管理ツールであ るTeX Live
Utility [14]_、文献管理のBibDesk、
スペルチェックのExcalibur、そして、Keynoteに数式を貼り付けるのに必
要なLaTeXiT [15]_もついてきます。

日本語とLaTeX
^^^^^^^^^^^^^

日本語はマルチバイトコードであるため、LaTeXでコンパイルするのが難
しかったみたいです。それに対処する歴史的な紆余曲折から日本語版
LaTeXにはさまざまな派生品が存在します。この歴史の詳細に関しては、
三重大学の奥村さんのウェブサイトをはじめ、ググってみるとよいでしょ う。

つい最近までは「Mac LaTeX インストール」などでググると、なんだか
まとまりのない情報で溢れていました。しかし、現在はそれらを取りま
とめようということで開発が進んでいるようで、これからはTeXLive一択
で良いみたいです。

TeXLiveはMacPortsからインストールすることもできますが、うまく設定
できた試しがありません。なので、\ `MacTeX公式ページ <https://tug.org/mactex/>`__
に置いてある
MacTeXパッケージをダウンロード [16]_するのが一番簡単で良いと思います。

ptex2pdf を使おう
~~~~~~~~~~~~~~~~~

日本語のLaTeX文書をコンパイルするにはpLaTeXコマンドを使います。コ
ンパイルが成功するとdviファイルが作成されるので、dvipdfmxコマンド
を使ってPDFファイルに変換します。

これをまとめてやってくれるのがptex2pdfコマンドで、（おそらく）
MacTeXをインストールすると勝手についてきます。ただのシェルスクリプ
トなので、気になる人は中を見てみるとよいでしょう。

YaTeXを使おう
~~~~~~~~~~~~~

MacTeXをインストールするとTeXShop.appがついてきます。
すぐに使えるので、時間に余裕がないときはこちらを使うと良いでしょう。

設定に時間を割けるようであれば、Emacs+YaTeXをおすすめします。YaTeX
の設定や操作コマンドを覚えるための時間は必要ですが、ある程度慣れて
しまえば編集作業が格段に捗るはずです。

http://ichiro-maruta.blogspot.jp/2013/03/latex.html
http://qiita.com/zr_tex8r/items/5413a29d5276acac3771

pdfLaTeX
~~~~~~~~

jsarticleドキュメントクラス
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#+begin\ :sub:`src` latex \\documentclass[dvipdfmx,12pt]{jsarticle}

#+end\ :sub:`src`

日本語のLaTeX文書にはjsarticleドキュメントクラスを使います。
ドライバはdvipdfmxを使います。

graphicxパッケージ
~~~~~~~~~~~~~~~~~~

#+begin\ :sub:`src` latex \\usepackage[hiresbb]{graphicx}

#+end\ :sub:`src`

画像を扱う場合はgraphicxパッケージを使います。
ドライバはdvipdfmxを使います。ドキュメントクラス指定時に宣言していてれば、ここで指定する必要はありません。
画像のバウンディングボックスに「HiResBoundingBox」を使う場合は、hiresbbオプションを付けておきます。

hyperrefパッケージ
~~~~~~~~~~~~~~~~~~

LaTeX文書内にハイパーリンクを置く場合には、hyperrefパッケージを使うとよい。
しかし、日本語のドキュメントクラスを使うとページから文章がはみ出たり、目次のしおりが文字化けしたりするので、以下のように対処する必要がある。

PXjahyperパッケージも読み込む
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#+begin\ :sub:`src` latex \\usepackage{pxjahyper}

#+end\ :sub:`src`

PXjahyperパッケージを読み込んでおけば、万事解決するみたい。
それでも解決しない場合は、以下のように個別に対処する。

ページサイズ対策
^^^^^^^^^^^^^^^^

#+begin\ :sub:`src` latex \\hypersetup{setpagesize=false}

#+end\ :sub:`src`

しおりの文字化け対策
^^^^^^^^^^^^^^^^^^^^

#+begin\ :sub:`src` latex \\usepackage{atbegshi}
\\AtBeginShipoutFirst{\\special{pdf:tounicode EUC-UCS2}}
\\AtBeginShipoutFirst{\\special{pdf:tounicode 90ms-RKSJ-UCS2}}

#+end\ :sub:`src`

何をしてくのか全く分かっていないけれど、両方書いておけばいい。
それでだめな場合は片方にする。

KiNOKO
------

CAMACやVMEでデータ収集を行うためのドライバをインストールします。
詳細に関しては「\ `KiNOKOプロジェクト <http://www.awa.tohoku.ac.jp/~sanshiro/kinoko/index.html>`__\ 」を参照してください。

.. code:: bash

    $ cd ~/Downloads/
    $ wget http://www.awa.tohoku.ac.jp/~sanshiro/kinoko-download/files/kinoko-2014-01-29.tar.gz
    $ tar zxvf kinoko-2014-01-29.tar.gz /usr/local/heplib/

僕の場合、ダウンロードしたファイルはとりあえず ~/Downloads
に保存することにしています。 また、高エネルギー物理関連のプログラムは
*usr/local/heplib* 以下にインストールすることにしています。

CAMACドライバのインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~

VMEドライバのインストール
~~~~~~~~~~~~~~~~~~~~~~~~~

Geant4
------

.. [1]
   Vimも基本操作はできるようにし といた方がよいと思っています

.. [2]
   MacのCocoaアプリもEmacsキーバインドで使え るのも大きな理由だったかも

.. [3]
   Wordやメモ帳

.. [4]
   決して安くはない

.. [5]
   Emacsの場合、\ `jawordパッケージ <https://github.com/zk-phi/jaword>`__
   を導入すると日本語の単語移動が賢くなります

.. [6]
   Emacsの場合、\ `jawordパッケージ <https://github.com/zk-phi/jaword>`__
   を導入すると日本語の単語移動が賢くなります

.. [7]
   Emacsの場合、\ `cmigemo <https://github.com/koron/cmigemo>`__ と
   `migemoパッケージ <https://github.com/emacs-jp/migemo>`__
   を導入するとローマ字で日本語検索が可能になります。インストールと設定の詳細は
   `るびきち「日刊Emacs」 <http://rubikitch.com/2014/08/20/migemo/>`__
   を参考にするとよいと思います

.. [8]
   Emacsの場合、\ `cmigemo <https://github.com/koron/cmigemo>`__ と
   `migemoパッケージ <https://github.com/emacs-jp/migemo>`__
   を導入するとローマ字で日本語検索が可能になります。インストールと設定の詳細は
   `るびきち「日刊Emacs」 <http://rubikitch.com/2014/08/20/migemo/>`__
   を参考にするとよいと思います

.. [9]
   元々はHelpですが、置き換えています

.. [10]
   元々はHelpですが、置き換えています

.. [11]
   Org-modeから LaTeXにエクスポート \\rightarrow
   YaTeX環境でコンパイルしています。
   すべての作業がEmacs内でできるので大変便利です

.. [12]
   ピンと来ない人は「ブロント語」でググってください

.. [13]
   修論の頃はお世話になりました。現在はYaTeXに移行したの
   で全く使っていません

.. [14]
   コマンドラインからtlmgrとして使えます。パッ
   ケージのインストールがとても楽ちん。ただし、TeXLiveのバージョンが上
   がるたびに動かなくなるのでちょっとめんどくさい

.. [15]
   これが一番重宝してます

.. [16]
   フルパッケージは2GBちょいあるの
   で、ダウンロードに少し時間がかかります。細い回線で行うのはオススメ
   しません

.. |CapsLock \\rightarrow Controlに変更| image:: ./fig/mac-keyboard04.png
.. |スポットライト検索のショートカットキーを変更する前。デフォルトは「Control + Space」| image:: ./fig/mac-keyboard01.png
.. |スポットライト検索のショートカットキーを「Option + Command + Space」に変更。重複するキーがあるため黄色い警告がでている| image:: ./fig/mac-keyboard02.png
.. |「Select next source in input menu」なんてショートカットキーはこれまで使ったことない。なので無効にしても問題ない| image:: ./fig/mac-keyboard03.png
