# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# ---
# title: ヒストグラムしたい（pd.DataFrame.plot）
# subject: pandasの使い方
# keywords: [python, pandas]
# authors:
#   - Shota Takahashi
# exports:
#   - format: pdf
# ---

# +
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
# -

# # 年齢の度数分布表を
#
# 18 - 60歳の100人を対象に実施したアンケートの、年齢分布を作成したいと思います。
# まず、``random.randint``を使って、アンケート結果をエミュレートします。

ages = [random.randint(18, 60) for i in range(100)]
data = pd.DataFrame({"age": ages})
data

# ``pandas.DataFrame.hist``もしくは``pandas.DataFrame.plot.hist``でヒストグラムを作成します。
# 階級（ビン）のサイズは、``bins``オプションで変更できます。

bins = range(0, 100, 5)
data.plot.hist(
    bins=bins,
    title="アンケート回答者の年齢分布",
    xlabel="年代",
    ylabel="回答数",
    legend=None,
)

# それぞれの階級の度数を確認したい場合は、``pandas.cut``と``pandas.value_counts``を組み合わせて使います。

# +
bins = range(0, 100, 10)
# listを渡すと、Categorical型で返ってくる
# c = pd.cut(ages, bins=bins)

# pd.Seriesを渡すと、pd.Seriesで返ってくる
# c = pd.cut(data["age"], bins=bins)
c = (
    data["age"]
    .value_counts(bins=bins)
    .reset_index()
    .rename(columns={"index": "rank", "count": "freq"})
)
c
# -

np.histogram(data["age"])
