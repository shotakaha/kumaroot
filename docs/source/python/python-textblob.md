# 感情分析したい（``textblob``）

```console
$ pip3 install textblob
$ python -m textblob.download_corpora
```

事前準備として、パッケージのインストールに加えて、感情分析に必要な学習データセット（＝コーパス）のダウンロードが必要です。
このパッケージは[NLTK（National Language Toolkit）](https://www.nltk.org/)を利用しています。
ホームディレクトリ直下に{file}`~/nltk_data/`が作成され、そこに必要はデータがサブディレクトリごとにダウンロードされます。

```python
from textblob import TextBlob
blob = TextBlob("分析したい文字列")
blob.sentiment.polarity
blob.sentiment.subjectivity
```

``textblob``パッケージを使って、文章の感情を評価できます。
感情分析は「極性（``polarity``）」と「主観性（``subjectivity``）」の軸があります。
極性は``-1.0 - 1.0``、主観性は``0.0 - 1.0``の範囲のfloat値で返ってきます。

## データフレームを一括で分析したい

```python
import pandas as pd
import numpy as np
from textblob import TextBlob


def sentiment_polarity(text: str):
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except TyperError as e:
        # print(e)
        return np.nan

def sentiment_subjectivity(text: str):
    try:
        blob = TextBlob(text)
        return blob.sentiment.subjectivity
    except TyperError as e:
        # print(e)
        return np.nan

# data: pd.DataFrame
data["text_polarity"] = data["text"].apply(sentiment_polarity)
data["text_subjectivity"] = data["text"].apply(sentiment_subjectivity)
```

Googleフォームで実施したアンケートの回答を``pandas.DataFrame``で処理したときに、自由記述の回答に対して実際に感情分析したときのソースです。
``pandas.DataFrame.apply``を使って、自由記述のカラムに対して極性と主観性をそれぞれ計算するようにしています。

回答が空欄だった場合は元データが``NaN``になっているため、``TextBlob``オブジェクトを作成する際に``TypeError``になってしまいます。
そのため``try...except``して``numpy.nan``を返すようにしています（``pandas.NA``でもいいのかもしれない）。

## 自動翻訳したい

```python
blob = TextBlob("翻訳したい文字列")
blob.translate(from_lang="en", to="ja")
```

元の言語（``from_lang``）と翻訳先の言語（``to``）を指定するだけで、自動翻訳できます。
英語の回答を理解するには十分な手助けになりました。
