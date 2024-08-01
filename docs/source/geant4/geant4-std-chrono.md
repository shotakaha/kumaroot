# 時間操作したい（``std::chrono``）

```cpp
#include <chrono>
```

``chrono``はC++11以降で使えるようになった時間操作クラスです。

## 現在時刻したい（``std::chrono::system_clock``）

```cpp
#include <chrono>  // std::chrono::system_clock
#include <ctime>   // std::time_t, std::tm, localtime_r
#include <fstream>  // std::fstream
#include <iomanip>  // std::put_time
#include <sstream>  // std::stringstream

namespace {
    // 無名の名前空間に入れて、スコープを小さくしておく
    // @code
    // G4String file_name = GetFileName();
    // G4cout << "Filename: " << file_name << G4endl;
    // @code

    G4String GetFileName()
    {
        // 現在のシステム時刻を取得
        auto now = std::chrono::system_clock::now();
        // time_t型に変換
        std::time_t now_t = std::chrono::system_clock::to_time_t(now);
        // tm構造体に変換
        std::tm now_tm;
        localtime_r(&now_t, &now_tm);

        // 時刻をフォーマット: yyyy-mm-ddTHHhMMmSSs
        std:stringstream ymd;
        ymd << std::put_time(&now_tm, "%Y-%m-%dT%Hh%Mm%Ss");

        // ファイル名を生成
        std::stringstream file_name;
        file_name << ymd.str() << ".csv";
    };
};  // namespace
```

現在時刻を取得して、ファイル名を生成してみました。
思った以上に手間がかかるので関数にしておくとよいと思います。

```{note}

C++20から[std::format](https://cpprefjp.github.io/reference/chrono/format.html)というモジュールが使えるようです。
Geant4がC++20に対応したら試してみるといいかもしれません。

```

## リファレンス

- [std::chrono](https://cpprefjp.github.io/reference/chrono.html)
