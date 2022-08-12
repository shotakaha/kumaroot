==================================================
Altairの使い方
==================================================

``Pandas`` で作成したデータフレームを描画する方法は、
Matplotlib、Seaborn、Plotlyなど色々ある。Altairもそのひとつ。


事前準備
==================================================

- ``altair`` パッケージをインストールする
- ``selenium`` パッケージをインストールする
- ``Chrome`` ブラウザをインストールする
- ``chromedriver`` をインストールする


.. code-block:: bash

    $ pip3 install -U altair
    $ pip3 install -U selenium
    $ brew install --cask google-chrome
    $ brew install --cask chromedriver


データの加工
==================================================

データを加工する方法は2通りある。
1つは ``pandas`` で加工する方法、もう1つは ``altair`` で描画する際に加工する方法である。
基本は前者の ``pandas`` を使うことをおすすめする。


基本コマンド
==================================================


.. code-block:: python

    import altair as alt

    alt.Chart(data).mark_*().encode()


.. toctree::

    altair-histogram
