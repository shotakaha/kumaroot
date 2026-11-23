# 出力したい（`G4ios.hh`）

```cpp
#include "G4ios.hh"  // G4cout などの宣言

G4cout << "Hello Geant4" << G4endl;  // 出力: Hello Geant4
```

`G4cout`は`std::cout`の代わりに使う出力ストリームです。
`G4endl`は`std::endl`と同じで、改行して出力を確定させます。
`globals.hh`が`G4ios.hh`を読み込むため、通常は`#include`を書かなくても使えます。

## 標準出力したい（`G4cout` / `G4endl`）

```cpp
G4cout << " The run consists of " << nofEvents << " events" << G4endl;
G4cout << " Cumulated energy: " << G4BestUnit(edep, "Energy") << G4endl;
// 出力: The run consists of 1000 events
// 出力: Cumulated energy: 3.2 MeV
```

単位付きの値は、[G4BestUnit](./geant4-units.md)で表示すると読みやすくなります。
文字列の扱いは[G4String](./geant4-string.md)のページも参照してください。

アプリケーションの出力には、`std::cout`ではなく`G4cout`を使います。
`G4cout`の出力はQtの画面にも表示されますが、`std::cout`はターミナルにしか出ません。
マルチスレッドでは、`G4cout`に`G4WT0 > `のような接頭辞が付きます。
フラッシュには`std::flush`を使います（`G4flush`はありません）。

## 標準エラー出力したい（`G4cerr` / `G4endl`）

```cpp
G4cerr << "World volume of box not found." << G4endl;
// 出力: World volume of box not found.
```

警告やエラーのメッセージは、`G4cerr`に書きます。
処理を止める必要がある問題は、`G4cerr`ではなく`G4Exception`を使います。

## デバッグ用出力したい（`G4debug` / `G4endl`）

```cpp
G4debug << "Track ID: " << track->GetTrackID() << G4endl;
```

`G4debug`は、デバッグ用のメッセージを書くためのストリームです。
`G4cout`と同じ仕組みで出力先に渡されます。

## マルチスレッドの出力を制御したい（`/control/cout/*`）

マルチスレッドで実行すると、ワーカースレッドの出力が大量に表示されることがあります。
次のコマンドで表示やファイルへの出力を制御できます。
マクロに書くか、UIセッションで入力します。

```text
/control/cout/prefixString W
/control/cout/ignoreThreadsExcept 0
/control/cout/setCoutFile worker.txt
```

| コマンド | 引数 | 働き |
|---|---|---|
| `/control/cout/setCoutFile` | `fileName`、`append` | `G4cout`の出力を、スレッドごとのファイルに書く。`**Screen**`で画面に戻す |
| `/control/cout/setCerrFile` | `fileName`、`append` | `G4cerr`の出力を、スレッドごとのファイルに書く |
| `/control/cout/useBuffer` | `flag` | 出力をバッファに溜めて、実行の最後にまとめて表示する |
| `/control/cout/prefixString` | `prefix`（既定は`G4WT`） | 各スレッドの出力に付く接頭辞を変える |
| `/control/cout/ignoreThreadsExcept` | `threadID`（既定は0） | 指定したスレッド以外の`G4cout`を表示しない。`-1`で解除する |
| `/control/cout/ignoreInitializationCout` | `IgnoreInit`（既定は`true`） | 初期化中のスレッドの`G4cout`を表示しない |

`ignoreThreadsExcept`は、画面に直接出力する場合にだけ効きます。

## リファレンス

- [Geant4 User's Guide: Main program（G4cout、G4cerr、G4debug）](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html#g4cout-g4cerr-and-g4debug)
