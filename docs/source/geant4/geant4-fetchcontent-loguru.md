# ロガーしたい（``loguru::loguru``）

```cpp
#include <loguru::loguru>

// ロガーの初期化
loguru::init(argc, argv);

// ファイルの設定
loguru::add_file("everything.log", loguru::Append, loguru::Verbosity_MAX);

// ログ表示
LOG_F(DEBUG, "Debug")
LOG_F(INFO, "Info")
LOG_F(WARNING, "Warning")
LOG_F(ERROR, "Error")
```

Geant4を実行すると大量のデフォルト出力に埋もれてしまうことがあります。
必要なログ情報は見た目をわかりやすくして出力してあると便利です。

## CMakeLists.txtの編集

```cmake
# FetchContentモジュールを読み込む
include(FetchContent)

# Loguruを取得
FetchContent_Declare(
    LoguruGitRepo
    GIT_REPOSITORY "https://github.com/emilk/loguru"
    GIT_TAG        "master"
)
set(LOGURU_WITH_STREAMS TRUE)
FetchContent_MakeAvailable(LoguruGitRepo)

# Loguruをリンク
target_link_libraries(実行ファイル名 ${Geant4_LIBRARIES} loguru::loguru)
```

[loguruのCMake Example](https://github.com/emilk/loguru/blob/master/loguru_cmake_example/CMakeLists.txt)を参考にCMakeLists.txtを編集します。
いくつかの方法がありますが、FetchContentモジュールを使うのが簡単だと思いました。

## ソースコードの編集

```cpp
// //////////////////////////////////////////////////
// メインのファイル.cc
// //////////////////////////////////////////////////
#include <loguru::loguru>

int main(int argc, char **argv)
{
    // main関数（メインファイル）の先頭で初期化する
    // 一度だけでよい（はず）
    loguru::init(argc, argv);
    LOG_F(INFO, "Setup loguru");
}
```

```cpp
// //////////////////////////////////////////////////
// 他のファイル.cc
// //////////////////////////////////////////////////
#include <loguru::loguru>

コンストラクター
{
    // 必要なところでロガーを使うだけ
    LOG_F(INFO, "コンストラクター")
}
```

``#include <loguru::loguru>``でロガーが利用できるようになります。
メインファイルの先頭でロガーを初期化（）``loguru::init``します。
他のファイルでは初期化せずともログ出力できるようになります。
ログ出力は``printf``形式で指定できます。

## リファレンス

- [emilk/loguru - GitHub](https://github.com/emilk/loguru)
- [loguru - emilk.github.io](https://emilk.github.io/loguru/index.html)
