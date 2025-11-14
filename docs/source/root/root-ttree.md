# TTreeしたい（`new TTree`）

```cpp
#include <TTree.h>

// TTree::TTree(name, title)
TTree *tree = new TTree("mytree", "example tree");
```

`new TTree`でTTreeオブジェクトを作成します。

古いドキュメントやサンプルでは`TNtuple`が紹介されていることがありますが、現在は`TTree`を使用すればOKです。
`TTree`は`TNtuple`の機能を包含しており、より柔軟で強力です。

```python
from ROOT import TTree

# Pythonでの作成
tree = TTree("mytree", "example tree")
```

## コンストラクターのシグネチャ

```cpp
TTree(
    const char *name,
    const char *title,
    Int_t splitlevel = 99
)
```

### 引数の説明

**name** - TTreeの名前

- ROOTファイル内で一意の名前を指定します
- 他のTTreeと重複しないようにします
- ファイルから読み込むときに指定する名前です

**title** - TTreeの説明

- データの簡潔な説明を設定します
- ROOTファイルを開いたときに表示されます
- 空文字列でも構いませんが、簡単な説明があると便利です

**splitlevel** -（通常は指定不要）

- デフォルト値: 99
- ブランチ内でオブジェクトを分割するレベルを指定
- ほとんどの場合、デフォルト値で問題ありません

## リファレンス

- [ROOT TTree Documentation](https://root.cern.ch/doc/master/classTTree.html)
