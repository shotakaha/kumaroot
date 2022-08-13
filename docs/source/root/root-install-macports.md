==================================================
MacPortsを使う方法
==================================================

Macユーザの場合 ``MacPorts`` でインストールするのが楽ちんなのでオススメです。
環境変数（ ``$ROOTSYS`` 、 ``$LD_LIBRARY_PATH`` 、 ``$DYLD_LIBRARY_PATH`` など）の設定も不要です。

``MacPorts`` に登録されているポート名（パッケージ名）には ``root5`` と ``root6`` があります。
両方をインストールすることはできますが、同時に使うことはできません。
簡単に切り替える方法は後述します。

ROOT6
==================================================

:command:`variants` なしでインストールした場合です。
``python27`` はデフォルトで **ON** です。

.. code-block:: bash

   $ sudo port install root6
   $ port installed root6
   The following ports are currently installed:
     root6 @6.04.02.99_0+cocoa+gcc48+graphviz+gsl+http+minuit2+opengl+python27+roofit+soversion+ssl+tmva+xml


ROOT6 +python34
==================================================

:command:`variants` に ``python34`` を指定した場合です。
最近インストールしてみたので ``gcc5`` がデフォルトになってます。

.. code-block:: bash

   $ sudo port install root6 +python34
   $ port installed root6
   The following ports are currently installed:
     root6 @6.04.02.99_0+cocoa+gcc48+graphviz+gsl+http+minuit2+opengl+python27+roofit+soversion+ssl+tmva+xml
     root6 @6.04.02.99_0+cocoa+gcc5+graphviz+gsl+http+minuit2+opengl+python34+roofit+soversion+ssl+tmva+xml (active)


ROOT5
==================================================

:command:`variants` なしでインストールしました。
``python27`` はデフォルトで **OFF** です。
後述する ``PyROOT`` を使用する場合は **ON** にしてインストールする必要があります。

.. code-block:: bash

   $ sudo port install root5
   $ port installed root5
   The following ports are currently installed:
     root5 @5.34.34_0+cocoa+gcc48+graphviz+gsl+http+minuit2+opengl+roofit+soversion+ssl+tmva+xml (active)



.. caution::
   ``Homebrew`` や ``fink`` など、その他のパッケージ管理ツールは使ったことがないので分かりません。
   誰か情報をくださいな。

.. todo::
   - MacPortsでバージョンを固定する方法があれば書き足す
   - http://trac.macports.org/wiki/howto/InstallingOlderPort
