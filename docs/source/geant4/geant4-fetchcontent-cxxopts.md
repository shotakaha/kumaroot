# オプション解析したい（``cxxopts``）

```cpp
#include <cxxopts.hpp>

// Optionsオブジェクト
cxxopts::Options option(
    "プログラム名",
    "プログラムの一行説明"
    );

// オプションを追加
options.add_options()
  ("d,debug", "Enable debugging")
  ("i,integer", "整数", cxxopts::value<int>())
  ("f,file", "ファイル名", cxxopts::value<std::string>())
  ("v,verbose", "verbosity", cxxopts::value<bool>()->default_value("false"))
;

// main関数の引数をパースして解析
auto result = options.parse(argc, argv);
```

main関数のオプション解析に``cxxopts``を使うことにしました。

``cxxopts::Options``オブジェクトを作成し、
``add_options``でオプションを追加します。

## リファレンス

- [jarro2783/cxxopts - GitHub](https://github.com/jarro2783/cxxopts)
