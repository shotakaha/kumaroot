# ロガーしたい（``loguru::loguru``）

```cpp
#include <loguru::loguru>

int main(int argc, char** argv)
{
  // ロガーの初期化
  loguru::init(argc, argv);

  // ファイルの設定
  loguru::add_file("everything.log", loguru::Append, loguru::Verbosity_MAX);

  // ログ表示
  LOG_F(ERROR, "Error")
  LOG_F(WARNING, "Error | Warning")
  LOG_F(INFO, "Error | Warning | Info")
  VLOG_F(0, "INFOと同じ")
  VLOG_F(1, "ERROR | WARNING | INFO | 1")
  ...
  VLOG_F(9, "MAX = すべて")
}
```

シミュレーションの進行状況は、ログファイルに出力して確認できるようにしておくとよいです。
ここでは``loguru``でログを設定／出力する方法を紹介します。

:::{hint}

なんでもかんでも``G4cout``や``G4cerr``で標準出力に表示していたら、100イベントを実行するのももっさりしていました。
ファイル出力に切り替えたら、一瞬で終わるようになりました。
ログ設定は、できるだけ早めに導入することをオススメします。

:::

## ログ出力したい（``LOG_F`` / ``VLOG_F``）

```cpp
LOG_F(ログレベル, "表示内容");
LOG_F(INFO, "RunID= %d", aRun->GetRunID());
LOG_F(INFO, "EventID= %d", aEvent->GetEventID());
LOG_F(INFO, "TrackID= %d", aTrack->GetTrackID());
LOG_F(INFO, "StepID= %d", aTrack->GetCurrentStepNumber());
VLOG_F(1, "ParentID= %d", aTrack->GetParentID());
VLOG_F(2, "PVName= %s", aTouchable->GetVolume()->GetName().c_str());
```

``LOG_F``形の関数では文字列、
``VLOG_F``形の関数では数値で、表示するときのログレベルをします。
表示内容は``printf``形式で指定きます。
``G4String``は``.c_str()``で文字列への変換が必要です。

## ログレベル

```cpp
FATAL
ERROR    // -2
WARNING  // -1
INFO     // 0
1 - 9
```

``loguru``のログレベルは（FATALを除いて）``-2 - 9``段階まで用意されています。

## 表示レベル（``loguru::g_stderr_verbosity``）

```cpp
loguru::g_stderr_verbosity = 表示レベル
loguru::g_stderr_verbosity = loguru::Verbosity_WARNING;  // WARNING（=-1）以下を表示
loguru::g_stderr_verbosity = loguru::Verbosity_INFO; // INFO（=0）以下を表示
loguru::g_stderr_verbosity = loguru::Verbosity_1;  // 1以下を表示
loguru::g_stderr_verbosity = loguru::Verbosity_2; // 2以下を表示
loguru::g_stderr_verbosity = loguru::Verbosity_MAX; // MAX（=9）以下を表示
```

``loguru::g_stderr_verbosity``で表示レベルを変更できます。
設定した表示レベル**以下**のログレベルに設定したログ表示されます。

## ファイルにログしたい（``add_file``）

```cpp
loguru::add_file("ファイル名", モード, 表示レベル);

// ファイル名: everything.log
// モード: 追記
// 表示レベル: INFO以下（=INFO / WARNING / ERROR）
loguru::add_file("everything.log", loguru::Append, loguru::Verbosity_INFO);

// ファイル名: latest.log
// モード: 上書き
// 表示レベル: MAX以下（=すべて）
loguru::add_file("latest.log", loguru::Truncate, loguru::Verbosity_MAX);
```

``loguru::add_file``でログをファイルに出力できます。
ファイルへの書き込みモードや、
書き込むログの表示レベルを設定できます。

## syslogしたい（``add_syslog``）

```cpp
loguru::add_syslog("ファイル名", 表示レベル);
```

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

    // ファイルにすべてログする
    loguru::add_file("everything.log", loguru::Truncate, loguru::Verbosity_MAX);

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
メインのファイルの先頭で
ロガーを初期化（``loguru::init``）したり、
ログファイルの設定（``loguru::add_file``）したりします。

他のファイルでは初期化せずともログ出力できるようになります。

## リファレンス

- [emilk/loguru - GitHub](https://github.com/emilk/loguru)
- [loguru - emilk.github.io](https://emilk.github.io/loguru/index.html)
