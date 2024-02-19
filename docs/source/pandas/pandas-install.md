# インストールしたい（``pandas``）

```console
$ pip3 install pandas
```

## 科学計算パッケージ

```bash
$ pip3 install numpy
$ pip3 install scipy
```

データ分析するときに、[NumPy](https://numpy.org/)や[SciPy](https://scipy.org/)といった科学計算パッケージでできることもあるので、必要になったらインストールしてください。

## 可視化したい（``matplotlib``）

```console
$ pip3 install matplotlib
$ pip3 install japanize-matplotlib
```

データを可視化するパッケージもいろいろありますが
一番メジャーなものは[matplotlib](https://matplotlib.org/stable/)だと思います。
``pandas``から直接使えるラッパーみたいなメソッドもあるので、まず使ってみるとよいです。

## 可視化したい（``altair``）

```console
$ pip3 install altair
```

作成した図をインタラクティブに操作したい場合は、
JavaScriptをベースにした描画ツールがオススメです。
僕は[Altair](https://altair-viz.github.io/)を好んで使っています。

## 機械学習したい（``scikit-learn``）

```console
$ pip3 install scikit-learn
```

機械学習したいひとは、よく使われる[scikit-learn](https://scikit-learn.org/stable/)パッケージをインストールするとよいでしょう。
