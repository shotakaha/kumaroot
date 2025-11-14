# Jupyter Notebookで対話的に実行したい（`--notebook`）

```console
$ root --notebook
```

`--notebook`オプションを使うことで、ROOTをJupyter Notebook環境で使用できます。
ブラウザベースのノートブック形式で、コードの実行結果や可視化を対話的に確認できます。

## Notebookの起動

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python3 --version
Python 3.14.0
(.venv) $ pip install notebook
(.venv) $ root --notebook
```

このコマンドでJupyter Notebookサーバーが起動し、デフォルトブラウザで自動的に開きます。
新しいノートブックを作成するか、既存のノートブックを開いて編集できます。

## Notebookでの基本的な使い方

### C++ コードの実行

```cpp
#include <iostream>
TH1F *h = new TH1F("h", "histogram", 100, -5, 5);
for (int i = 0; i < 10000; i++) {
    h->Fill(gRandom->Gaus(0, 1));
}
h->Draw();
```

セル内にC++コードを記述して実行します。

### Python コードの実行

```python
import ROOT

h = ROOT.TH1F("h", "histogram", 100, -5, 5)
for i in range(10000):
    h.Fill(ROOT.gRandom.Gaus(0, 1))
h.Draw()
```

PyROOTを使ってPythonでコードを記述することもできます。

## Notebookの利点

- **対話的な開発**：コードを実行しながら結果を確認できます
- **可視化の統合**：グラフやヒストグラムを直接ノートブック内に表示
- **ドキュメンテーション**：コード、出力、マークダウンテキストを同一ファイルに記録
- **再現性**：分析の過程をすべて記録し、あとで再実行可能
- **共有**：`.ipynb`ファイルを共有して、他のユーザーが再現可能

## Notebookの保存

作成したノートブックは`.ipynb`形式で保存されます。
このファイルには、コード、実行結果、マークダウンテキストがすべて含まれています。

## Rint（対話型シェル）との違い

| 項目 | Notebook | Rint |
|------|----------|------|
| インターフェイス | ブラウザベース | コマンドライン |
| ドキュメンテーション | 統合可能 | 不可 |
| 可視化の表示 | 直接表示 | 別ウィンドウ |
| 保存形式 | `.ipynb` | `.C`マクロファイル |
| 再現性 | 高い（全操作を記録） | 中程度 |

## 参考リンク

- [Jupyter Notebook公式ドキュメント](https://jupyter-notebook.readthedocs.io/)
- [PyROOT ガイド](https://root.cern/manual/python/)
- [起動したい（Rint）](./root-rint.md) - コマンドライン対話型シェル
