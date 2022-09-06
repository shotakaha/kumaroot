==================================================
use-packageの設定
==================================================

パッケージ管理ツール（:file:`package.el`）を強化するパッケージです。
`use-package <github_>`_ の使い方の一番下に書いてある通りに設定しておきます。

.. code-block:: elisp

   (eval-when-compile (require 'use-package))
   (require 'diminish)    ;; if you use :diminish
   (require 'bind-key)    ;; if you use any :bind variant
   (setq use-package-verbose t)
   (setq use-package-minimum-reported-time 0.001)

使い方に関しては、下に挙げたウェブサイトを見たほうがとよいと思います。
ただ、日本語のブログは内容が古くなっているので、概要把握にとどめ、
詳細な設定項目は本家サイトで確認するのがよいでしょう。


- `use-package - GitHub <github_>`_
- `use-packageで可読性の高いinit.elを書く - Qiita <qiita_>`_
- `use-package - るびきち日刊Emacs <rubikitch_>`_

.. _github: https://github.com/jwiegley/use-package
.. _qiita: https://qiita.com/kai2nenobu/items/5dfae3767514584f5220
.. _rubikitch: http://emacs.rubikitch.com/use-package-2/
