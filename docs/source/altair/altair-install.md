# インストールしたい

``Altair``本体と、図を保存するためのパッケージをインストールします。
``v5``と``v4``で必要¯パッケージが異なります。
詳しくは[Saving Altair Charts: PNG, SVG and PDF format](https://altair-viz.github.io/user_guide/saving_charts.html#png-svg-and-pdf-format)を参照してください。

## v5をインストールしたい

```console
$ pip3 install -U altair
$ pip3 install -U vl-convert
```

``v5``では図を保存するためのパッケージ依存が少なくなり``vl-convert``だけでOKになりました。
ただし、PNGとSVGだけに対応しており、PDFでは保存できません。

## v4をインストールしたい

```console
$ pip3 install -U altair
$ pip3 install altair_saver
$ pip3 install selenium==4.2.0
$ brew install --cask google-chrome
$ brew install --cask chromedriver
```

``v4``では図を保存するためのパッケージ依存が複雑です。
まず``altair_saver``と``selenium``が必要です。
``altair_saver``には[イシュー（altair_saver#104）](https://github.com/altair-viz/altair_saver/issues/104)があるので、``selenium``は4.2.0を指定する必要があります。

また`altair_saver`は（まだ）``v5``非対応です。
すでにAltairを使った個人プロジェクトがあるのですが、移行するのに手間がかかりそうなので、もうしばらくはv4で様子を見ようと思っています。

さらに``Chrome``ブラウザと``chromedriver``が必要です。
これはChromeをヘッドレスモードで動かして画像やPDFとして保存しているためだと思います。
``chromedriver``をはじめて起動するときは、macOSのセキュリティ確認にひっかかります。
{guilabel}`設定` → {guilabel}`Security & Privacy` → {guilabel}`General`タブを確認し、許可してください。
