# 辞書型配列したい（``std::map``）

```cpp
#include "G4SystemOfUnit.hh"

#include <map>

std::map<std::string, G4int> fHitInt{};
fHitInt["run_id", fRunID];
fHitInt["event_id", fEventID];
fHitInt["track_id", fTrackID];
fHitInt["parent_id", fTrackParentID];
fHitInt["step_id", fStepID];

std::map<std::string, G4double> fHitDouble{};
fHitDouble["energy_deposit", fEnergyDeposit / MeV];
fHitDouble["step_x", fStepXYZ.getX() / mm];
fHitDouble["step_y", fStepXYZ.getY() / mm];
fHitDouble["step_z", fStepXYZ.getZ() / mm];

std::map<std::string, G4String> fHitString{};
fHitString["material_name", fMaterialName];
```

``std::map``で辞書型の配列を定義できます。
``G4VHit``（を継承してユーザが定義したクラス）のヒット情報を、
カラム名と一緒にまとめるために使うとよいと思います。

## LTSV形式したい

LTSV形式は、**Labeled Tab-Separated Value** の略で、
以下のような構造を持つ形式です。

```text
key1:value    key2:value    key3:value    ...
key1:value    key2:value    key3:value    ...
key1:value    key2:value    key3:value    ...
...
```

あまりメジャーではない形式かもしれませんが、
それぞれの値がラベル名（＝カラム名）を持つのが特徴です。
解析するときにカラム名を別途調べる必要がないため、かなり便利です。

また、データの数を追加／削除したときにも、解析ツールの修正をあまりしなくてすみます。
そもそも、データ自身がカラム名を持っているので、特定の解析ツールへの依存性がないのも利点です。


:::{note}

LTSV形式は、Apacheのログ解析の方法を調べているときに知りました。
デフォルト形式（common形式 もしくは combined形式）のApacheログをパースするのは大変です。
LTSV形式を使ったカスタムログにしておくと、

:::

```cpp
G4String ToLtsvString()
{
    std::stringstream ss;
    G4bool is_first = true;
    for (const auto& pair: fHitInt) {
        if (!is_first) {
            ss << ",";
        };
        ss << pair.first << ":" << pair.second;
        is_first = false;
    };
    for (const auto& pair: fHitInt) {
        ss << "," << pair.first << ":" << pair.second;
    };
    for (const auto& pair: fHitInt) {
        ss << "," << pair.first << ":" << pair.second;
    };
    G4String ltsv{ss.str()};
    return ltsv;
};
```

このサンプルでは、Tab-Separatedではなく、Comma-SeparatedとしたLTSV亜種を作成しています。
CSV形式にしておくと
Excelなどの表計算ソフトでファイルを開いたり、
Pythonで読み込むときの区切り文字（delimiter）もデフォルトのままでよかったり、
と便利だと思うからです。

```text
key1:value, key2:value, key3:value, ...
key1:value, key2:value, key3:value, ...
key1:value, key2:value, key3:value, ...
...
```

行頭と行末に``,``は不要なので``is_first``変数をつかって調整しています。
