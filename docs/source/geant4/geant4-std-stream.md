# ファイル操作したい（``std::fstream``）

```cpp
#include <fstream>  // std::fstream
#include <sstream>  // std::stringstream

// 連続してファイル名を生成したい場合、
// ファイル名が重複しないように工夫する
G4int run_id = "ランID";
G4int event_id = "イベントID";

// ファイル名を生成する
std::stringstream filename;
filename << "run" << std::setfill('0') << std::setw(5) << run_id;
filename << "event" << std::setfill('0') << std::setw(5) << event_id;
filename << ".csv";

// ファイルを追記モードで作成する
std::ofstream file(filename.c_str(), std::ios::app);

// ファイルが開けなかった場合の処理
if (!file.is_open())
{
    G4cerr << "Failed to open file: " << filename << G4endl;
    return;
};

// ファイルに文字列を追加する
G4cout << "File opened: " << filename << G4endl;
file << "CSV文字列1" << "\n";
file << "CSV文字列2" << "\n";
file << "CSV文字列3" << "\n";

// ファイルを閉じる
file.close();
```

``std::stringstream``で、ファイル名を作成しています。
``std::fstream``でファイル操作しています。
