============================================================
ドキュメントクラスオプションの設定（ ``latex_elements`` ）
============================================================

ドキュメントクラス（ ``\documentclass`` ）のオプションを設定する部分です。
プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけして、中身はあとで書くことにします。


.. code-block:: python

    latex_elements = {
        'papersize' = 'a4paper',
        'pointsize' = '12pt',
        'preamble': '',    # あとで追加するので定義だけしておく
        'figure_align': 'htbp',
    #   'fontpkg': '\\usepackage{times}',
    }


``LaTeX`` 文書の出力は以下のようになります。

.. code-block:: latex

   \documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}
