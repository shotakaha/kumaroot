==================================================
use-packageの使い方
==================================================

パッケージ管理ツール（:file:`package.el`）を強化するパッケージです。


設定
==================================================

`use-package <github_>`_ の使い方の一番下に書いてある通りに設定しておきます。

.. code-block:: elisp

   (eval-when-compile (require 'use-package))
   (require 'diminish)    ;; if you use :diminish
   (require 'bind-key)    ;; if you use any :bind variant
   (setq use-package-verbose t)
   (setq use-package-minimum-reported-time 0.001)



参考サイト
==================================================

- `use-package - GitHub <github_>`_
- `use-packageで可読性の高いinit.elを書く - Qiita <qiita_>`_
- `use-package - るびきち日刊Emacs <rubikitch_>`_

.. _github: https://github.com/jwiegley/use-package
.. _qiita: http://qiita.com/kai2nenobu/items/5dfae3767514584f5220
.. _rubikitch: http://rubikitch.com/2014/09/09/use-package/
