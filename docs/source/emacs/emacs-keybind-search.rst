==================================================
検索
==================================================

.. list-table:: 検索
   :header-rows: 1
   :stub-columns: 1

   * - 操作内容
     - Emacs
     - Vim
   * - 前方検索
     - :kbd:`C-s`
     - :kbd:`/文字` , :kbd:`n` , :kbd:`C-i`
   * - 後方検索
     - :kbd:`C-r`
     - :kbd:`?文字` , :kbd:`N` , :kbd:`C-o`
   * - マーカーのセット
     - :kbd:`C-@`
     - :kbd:`v`
   * - 現在行の最初の文字を置換（old -> new）
     - :kbd:`M-%`
     - :kbd:`:s/old/new`
   * - 現在行のすべての文字を置換（old -> new）
     -
     - :kbd:`:s/old/new/g`
   * - ファイル全体のすべての文字を、確認しながら置換
     -
     - :kbd:`:%s/old/new/gc`


-  Emacsの場合、
   `cmigemo <https://github.com/koron/cmigemo>`__ と
   `migemoパッケージ <https://github.com/emacs-jp/migemo>`__
   を導入するとローマ字で日本語検索が可能になります。
-  インストールと設定の詳細は
   `るびきち「日刊Emacs」 <http://emacs.rubikitch.com/migemo/>`__
   を参考にするとよいと思います。
