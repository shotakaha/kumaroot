# インストールしたい

```console
$ pip3 install -U altair
```

```python
import altair as alt
alt.Chart(data).mark_*().encode()
```

公式ドキュメントを読むと``alt``という略称でインポートしています。

## プロットを保存したい

```console
$ pip3 install -U selenium
$ brew install --cask google-chrome
$ brew install --cask chromedriver
```

プロットを保存するために``altair``以外のツールも必要です。
``selenium``や``Chrome`` / ``chromedriver`` は生成した画像を自動で書き出すために追加しました。
