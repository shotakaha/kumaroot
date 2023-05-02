# インストールしたい

```console
$ pip3 install -U altair
$ pip3 install -U selenium
$ brew install --cask google-chrome
$ brew install --cask chromedriver
```

``altair``本体以外にもいろいろ追加しています。
``selenium``や``Chrome`` / ``chromedriver`` は生成した画像を自動で書き出すために追加しました。

公式ドキュメントを読むと``alt``という略称でインポートしています。

```python
import altair as alt
alt.Chart(data).mark_*().encode()
```
