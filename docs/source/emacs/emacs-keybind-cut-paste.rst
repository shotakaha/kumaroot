==================================================
切り貼り
==================================================

.. list-table:: 切り貼り
   :header-rows: 1
   :stub-columns: 1

   * - 操作内容
     - Emacs
     - Vim
   * - カーソルの位置から行末までを切り取り
     - :kbd:`C-k`
     - :kbd:`d$`
   * - 選択範囲を切り取り
     - :kbd:`C-w`
     - :kbd:`dd` , :kbd:`d$` , :kbd:`dw` , :kbd:`d^` , :kbd:`d0`
   * - 選択範囲をコピー（yank）
     - :kbd:`M-w`
     - :kbd:`y` , :kbd:`yy` , :kbd:`yw` , :kbd:`y$` , :kbd:`y^` , :kbd:`y0`
   * - 貼り付け
     - :kbd:`C-y`
     - :kbd:`p`
