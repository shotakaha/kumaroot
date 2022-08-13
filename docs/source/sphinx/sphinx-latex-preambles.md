============================================================
プリアンブルの追加（ ``latex_elements['preamble']`` ）
============================================================

上の ``latex_elements`` の中で複数のパッケージを書くと見た目がカッコ悪いので、
以下のように ``latex_elements['preamble']`` に直接追加することにしました。

.. code-block:: python

    latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
    latex_elements['preamble'] += '\\usepackage{graphics}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
    latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
    latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
    latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'

``LaTeX`` 文書の出力は以下のようになります。

.. code-block:: latex

   \usepackage{pxjahyper}
   \usepackage{graphics}
   \hypersetup{bookmarksopen=true}
   \hypersetup{bookmarksopenlevel=2}
   \hypersetup{colorlinks=true}
   \hypersetup{pdfpagemode=UseOutlines}
