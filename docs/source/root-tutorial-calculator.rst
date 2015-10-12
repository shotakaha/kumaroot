==================================================
ROOT電卓
==================================================

CINTは電卓代わりに使うこともできます（ :numref:`fig-root-calc` ）。
四則演算の記号 :kbd:`+`, :kbd:`-`, :kbd:`*`, :kbd:`/`, :kbd:`%` はそのまま使えます。
べき乗や累乗根などはROOTの ``TMathクラス`` を使います。
``TMathクラス`` には円周率 :math:`\pi` （ ``TMath::Pi()`` ）や自然定数 :math:`e` （ ``TMath::E()`` ）のような定数も入っています。

.. _fig-root-calc:
.. figure:: ./root-tutorial/root-calc.png
   :align: center

   CINTを電卓代わりに使ってみる
