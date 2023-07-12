# インストールしたい

```console
$ pip3 install -U altair
```

```python
import altair as alt
alt.Chart(data).mark_*().encode()
```

公式ドキュメントを読むと``alt``という略称でインポートしています。

:::{note}

2023/05/10にAltair v5がリリースされ、新しい書式設定用のメソッドが追加されました。
どれでもいいのでギャラリーにある[サンプル](https://altair-viz.github.io/gallery/histogram_heatmap.html)を確認すれば、どういう機能が追加されたのか一目瞭然です。

:::

## プロットを保存したい（``vl-convert-python``）

```console
$ pip3 install vl-convert-python
```

Altair v5では``vl-convert``だけでPNGとSVGが保存できるようになりました。
ただし、[Saving Altair Charts: PNG, SVG and PDF format](https://altair-viz.github.io/user_guide/saving_charts.html#png-svg-and-pdf-format)を読むとPDFはNGのようです。

変更点の詳細は[リリースノート](https://github.com/altair-viz/altair/releases/tag/v5.0.0)を参照してください。

:::{note}

これまでAltairを使った個人プロジェクトが多数あるのですが、移行するのに手間がかかりそうなので、もうしばらくはv4で様子見します。

新しく作成するプロジェクトはv5を使いはじめてみました。
依存パッケージが減り、導入が簡単になりよき✨

:::

## プロットを保存したい（``altair_saver``）

```console
$ pip3 install altair_saver
$ pip3 install selenium==4.2.0
$ brew install --cask google-chrome
$ brew install --cask chromedriver
```

Altair v4では、プロットを保存するために``altair``以外の外部ツールが必要です。
``selenium``や``Chrome`` / ``chromedriver`` は生成した画像を自動で書き出すために追加しました。
``altair_saver``の[イシュー（altair_saver#104）](https://github.com/altair-viz/altair_saver/issues/104)があるので、``selenium``は4.2.0を指定する必要があります。

``chromedriver``をはじめて起動するときは、macOSのセキュリティ確認にひっかかります。
{guilabel}`設定` → {guilabel}`Security & Privacy` → {guilabel}`General`タブを確認し、許可してください。

:::{note}

`altair_saver`は（まだ）v5非対応です。

:::
