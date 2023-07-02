# インストールしたい

```console
$ pip3 install -U altair
```

```python
import altair as alt
alt.Chart(data).mark_*().encode()
```

公式ドキュメントを読むと``alt``という略称でインポートしています。

## プロットを保存したい（``altair_saver``）

```console
$ pip3 install altair_saver
$ pip3 install selenium==4.2.0
$ brew install --cask google-chrome
$ brew install --cask chromedriver
```

プロットを保存するために``altair``以外のツールも必要です。
``selenium``や``Chrome`` / ``chromedriver`` は生成した画像を自動で書き出すために追加しました。
``altair_saver``の[イシュー（altair_saver#104）](https://github.com/altair-viz/altair_saver/issues/104)があるので、``selenium``は4.2.0を指定する必要があります。

``chromedriver``をはじめて起動するときは、macOSのセキュリティ確認にひっかかります。
{guilabel}`設定` → {guilabel}`Security & Privacy` → {guilabel}`General`タブを確認し、許可してください。

:::{note}

2023/05/10にAltair v5がリリースされました。
[リリースノート](https://github.com/altair-viz/altair/releases/tag/v5.0.0)を確認すると、プロット保存周りも大きく変更されたようです。

> `vl-convert` is now used as the default backend for saving Altair charts as svg and png files, which simplifies saving chart as it does not require external dependencies like `altair_saver` does (#2701).
> Currently, `altair_saver` does not support Altair 5 and it is recommended to switch to `vl-convert`.
> See PNG, SVG, and PDF format for more details.

上記のとおり、v5ではプロットを保存するパッケージが`vl-convert`に変わったようです。
`altair_saver`は（まだ）v5非対応なので`vl-convert`への移行が必要です。

ただし、[Saving Altair Charts: PNG, SVG and PDF format](https://altair-viz.github.io/user_guide/saving_charts.html#png-svg-and-pdf-format)を読むと、`vl-convert`で保存できるのはPNGとSVGだけで、PDFはNGのようです。
Altairを使った個人プロジェクトがあるのですが、移行するのに手間がかかりそうなので、もうしばらくはv4で様子を見ようと思っています。

:::
