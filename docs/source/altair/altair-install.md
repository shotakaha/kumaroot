# インストール

- ``altair`` パッケージをインストールする
- ``selenium`` パッケージをインストールする
- ``Chrome`` ブラウザをインストールする
- ``chromedriver`` をインストールする

```bash
pip3 install -U altair
pip3 install -U selenium
brew install --cask google-chrome
brew install --cask chromedriver
```

公式ドキュメントを読むと``alt``としてインポートするみたいです。

```python
import altair as alt
alt.Chart(data).mark_*().encode()
```
