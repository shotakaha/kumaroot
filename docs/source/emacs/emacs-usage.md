```{eval-rst}
.. index::
    pair: Emacs; usage
```

# Emacsの使い方

Emacsは1970年代に誕生し、半世紀近くに渡って使われ続けているテキストエディターです。
初期状態ではシンプルな構成となっており、必ずしも使いやすいとは言えませんが、
Emacs Lisp（Elisp）によって無限にカスタマイズできます。

その結果、テキスト編集だけでなく、メールやカレンダー、タスク管理などにも利用でき、
統合開発環境（IDE）を含む作業環境そのものをEmacs上に構築することも可能です。
この拡張性の高さこそが、長年にわたって多くのユーザーに支持されてきた理由のひとつです。

僕が本格的にEmacsを使いはじめたのは2009年ころです。
Emacs23でパッケージ管理システム（[package.el](./emacs-package.md)）が導入され、
[use-package](./emacs-use-package.md)も登場し、
パッケージの追加と設定がぐっと便利になったタイミングでした。

るびきちさんの本を読みながら設定を真似し、
[Prelude](./emacs-prelude.md)もこの頃から使いはじめました。
Elispを使った簡単なカスタマイズにどハマりし、ありとあらゆることをEmacsに集約できないかと、
設定に四苦八苦した思い出もあります
（結局、メール設定でUTF-8/ShiftJIS周りのなにかを解決する方法がわからず断念）。

エディターは、プログラミングや文書作成などの編集作業に欠かせないツールです。
デスクワークの多くの時間を、エディターとともに過ごしているといっても過言ではありません。
自分に合ったエディターを選ぶことで、日々の編集作業はより快適で、効率的で、そして楽しいものになります。

Emacsは「カスタマイズ性」に優れた、とても育て甲斐のあるエディターです。
使い込むほどに自分の手に馴染み、作業環境そのものを形作っていくことができます。
このドキュメントでは、その一助となることを目指して
Emacsの簡単な使い方と、日常的に役立つ便利なパッケージを紹介していきます。

:::{note}

パソコンを買い替えるたびにイチから設定するめんどくさくなり
（設定の見直しも兼ねていて、それはそれで楽しい作業ではあるのですが）、
2020年くらいから[VS Code](../vscode/vscode-usage.md)をメインで使うようになりました。

ただ、Emacs操作体系が身体に深く染み付いているため、
キーバインドには[Awesome Emacs Keymap](https://marketplace.visualstudio.com/items?itemName=tuttieee.emacs-mcx)を導入し、
Git操作には[Edamagit](https://marketplace.visualstudio.com/items?itemName=kahole.magit)を利用しています。
また、全体の操作体系として[VSpaceCode](https://marketplace.visualstudio.com/items?itemName=VSpaceCode.vspacecode)を採用することで、
`Emacs`と`vim`のいいとこどりな環境を構築しています。

`Emacs` vs `vim`はエディター界隈の宗教戦争と揶揄されますが、
`vim`のモード切り替えと、片手でスクロール操作できるのはすばらしいと思います。

:::

:::{note}

Emacsのバッファー／ミニバッファーや[dired](./emacs-dired.md)のような操作体験が、
VS Codeではなかなか得られず、2026年にひさびさにEmacsに戻ってきました。

この数年でまさに隔世の感がありました。
以前は「手間暇かけて使えるようにするエディター」という印象でしたが、
現在では標準機能や周辺パッケージが大きく進化し、かなり使い勝手が向上しているように感じます。

昔の設定を見直し、ChatGPTなども活用しながら、
モダンなEmacs環境の構築を目指して、ドキュメント更新をリブートしてみようと思います。

:::

```{toctree}
---
maxdepth: 1
---
emacs-install
emacs-init
emacs-keyboard
emacs-keybind
emacs-twitter
emacs-word
```

## 基本設定したい

```{toctree}
---
maxdepth: 1
---
emacs-builtins
emacs-font
emacs-frame
```

## 標準パッケージしたい

```{toctree}
---
maxdepth: 1
---
emacs-package
emacs-dired
emacs-org
emacs-eshell
emacs-icomplete
emacs-ido
emacs-ivy
emacs-eval
emacs-modeline
emacs-doom-modeline
emacs-flymake
```

To be added

- emacs-show-paren-mode
- emacs-column-number-mode
- emacs-save-place-mode
- emacs-delete-selection-mode
- emacs-recentf-mode
- emacs-savef-mode
- emacs-auto-revert-mode
- emacs-project

## 拡張パッケージしたい

```{toctree}
---
maxdepth: 1
---
emacs-use-package
emacs-which-key
emacs-vertico
emacs-magit
emacs-yatex
emacs-vterm
emacs-corfu
emacs-orderless
emacs-anything
emacs-guru
emacs-evil
emacs-marginalia
emacs-consult
```

To be Added

- emacs-embark
- emacs-savehist
- emacs-projectile
- emacs-cape
- emacs-flycheck
- emacs-eglot

## フレームワークしたい

```{toctree}
---
maxdepth: 1
---
emacs-prelude
emacs-spacemacs
emacs-doom
```

## リファレンス

- [Emacs for MacOS X](https://emacsformacosx.com)
- [るびきち「日刊Emacs」](http://rubikitch.com)
- [Prelude](https://prelude.emacsredux.com/en/latest/)
- [Org-mode for Emacs](https://orgmode.org/)
- [野鳥（YaTeX : Yet Another TeX for Emacs）](https://www.yatex.org/)
- [Magit! A Git Porcelain inside Emacs](https://magit.vc/)
