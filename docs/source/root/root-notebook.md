# Notebookしたい（`--notebook`）

```console
$ root --notebook
```

`--notebook`オプションで、ROOTをJupyter Notebook環境で使用できます。
このコマンドでJupyter Notebookサーバーが起動し、デフォルトのブラウザが自動的に開きます。

ブラウザベースでノートブックを操作し、コードの実行結果や可視化を対話的に確認できます。
ノートブックは`ipynb`形式で保存できます。
ノートブックは共同研究者に共有して、結果を再現できます。

## Notebookの準備

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 --version
Python 3.14.0
(.venv) $ pip install notebook
(.venv) $ pip install metakernel
(.venv) $ root --notebook
```

HomebrewでインストールしたROOTの場合、Jupyter Notebook周りのPythonパッケージが不足している可能性があります。
その場合は、通常のPythonと同じように仮想環境を作成し、必要なパッケージをインストールしてください。

## C++を実行したい（`ROOT C++ Kernel`）

```cpp
#include <iostream>
TH1F *h = new TH1F("h", "histogram", 100, -5, 5);
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}
h->Draw();
```

カーネル選択で「`ROOT C++`」に切り替えます。
セル内にC++/ROOTの解析コードを記述できます。

## PyROOTを実行したい（`Python3 (ipykernel) Kernel`）

```python
import ROOT

h = ROOT.TH1F("h", "histogram", 100, -5, 5)
for i in range(10000):
    h.Fill(ROOT.gRandom.Gaus(0, 1))
h.Draw()
```

カーネル選択で「`Python (ipykernel)`」に切り替えます。
PyROOTを使ってPythonで解析コードを記述できます。

## Notebookの利点

- **対話的な開発**：コードを実行しながら結果を確認できます
- **可視化の統合**：グラフやヒストグラムを直接ノートブック内に表示
- **ドキュメンテーション**：コード、出力、マークダウンテキストを同一ファイルに記録
- **再現性**：分析の過程をすべて記録し、あとで再実行可能
- **共有**：`.ipynb`ファイルを共有して、他のユーザーが再現可能

## 参考リンク

- [Jupyter Notebook公式ドキュメント](https://jupyter-notebook.readthedocs.io/)
- [PyROOT ガイド](https://root.cern/manual/python/)
- [起動したい（Rint）](./root-rint.md) - コマンドライン対話型シェル
