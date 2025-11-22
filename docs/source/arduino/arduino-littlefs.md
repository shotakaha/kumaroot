# LittleFSしたい

```c
#include <LittleFS.h>
```

LittleFSはマイコンのフラッシュ領域にファイルを保存できるライブラリです。

ESP32などのマイコンには、揮発性メモリ（DRAM）と不揮発性メモリ（フラッシュ）の領域があります。

**揮発性メモリ**は電源が落ちると消去される領域です。
プログラム実行時の変数や一時データを保存するのに使われます。
**不揮発性メモリ**は電源が落ちても保存される領域です。
プログラムやファイルなどの永続データを保存するのに使われます。

LittleFSはフラッシュ領域をファイルシステムとして分割し、通常のファイル操作（読み書き、削除など）を可能にします。

:::{warning}

フラッシュ領域には書き込み回数の制限（一般に約10万～100万回）があります。

:::

## ESP32で初期化したい

```cpp
#include <LittleFS.h>

void setup() {
    Serial.begin(115200);

    if (!LittleFS.begin()) {
        Serial.println("LittleFS Mount Failed");
        return;
    }
    Serial.println("LittleFS Mounted Successfully");
}

void loop() {
    // Your code here
}
```

ESP32のArduino Core2.0以降では、LittleFSが標準で含まれています。

## ESP8266で初期化したい

```cpp
#include "LittleFS.h"

void setup() {
    Serial.begin(115200);

    if (!LittleFS.begin()) {
        Serial.println("LittleFS mount failed");
        return;
    }
    Serial.println("LittleFS mounted successfully");
}

void loop() {
    // Your code here
}
```

ESP8266のArduinoコアには、LittleFSがビルトインされています。

## ファイルの管理

### ファイルを削除したい

```cpp
void setup() {
    LittleFS.begin();

    if (LittleFS.remove("/old_config.txt")) {
        Serial.println("File deleted");
    } else {
        Serial.println("Delete failed");
    }
}

void loop() {}
```

### ファイルが存在するか確認したい

```cpp
void setup() {
    LittleFS.begin();

    if (LittleFS.exists("/config.txt")) {
        Serial.println("File exists");
    } else {
        Serial.println("File does not exist");
    }
}

void loop() {}
```

### ファイル名を変更したい

```cpp
void setup() {
    LittleFS.begin();
    LittleFS.rename("/old.txt", "/new.txt");
}

void loop() {}
```

## ディレクトリの操作

### ディレクトリの中身を一覧表示したい

```cpp
#include <LittleFS.h>

void listDir(const char *dirname, uint8_t levels) {
    File root = LittleFS.open(dirname);
    if (!root || !root.isDirectory()) {
        Serial.println("Failed to open directory");
        return;
    }

    File file = root.openNextFile();
    while (file) {
        if (file.isDirectory()) {
            Serial.print("DIR : ");
            Serial.println(file.name());
            if (levels) {
                listDir(file.path(), levels - 1);
            }
        } else {
            Serial.print("FILE: ");
            Serial.print(file.name());
            Serial.print(" SIZE: ");
            Serial.println(file.size());
        }
        file = root.openNextFile();
    }
}

void setup() {
    LittleFS.begin();
    listDir("/", 1);
}

void loop() {}
```

### ディレクトリを作成したい

```cpp
void setup() {
    LittleFS.begin();
    LittleFS.mkdir("/data");
}

void loop() {}
```

### ディレクトリを削除したい

```cpp
void setup() {
    LittleFS.begin();
    LittleFS.rmdir("/data");
}

void loop() {}
```

## フラッシュメモリの情報

### 容量情報を確認したい

```cpp
// ESP32
void setup() {
    LittleFS.begin();
    Serial.printf("Total: %u bytes\n", LittleFS.totalBytes());
    Serial.printf("Used: %u bytes\n", LittleFS.usedBytes());
}

void loop() {}
```

## ファイルをアップロードしたい

Arduino IDEを使ってパソコン上のファイルをマイコンのフラッシュメモリにアップロードするには、LittleFSアップローダーを使用します。

### 準備手順

1. **LittleFSアップローダーをインストール**
   - Arduino IDE 2.x：プラグイン機能から「LittleFS Upload」をインストール

2. **スケッチのフォルダーに`data`フォルダーを作成**
   - Sketch > Show Sketch Folder でスケッチフォルダーを開く
   - `data`というフォルダーを作成
   - ここにアップロードしたいファイル（HTMLファイルなど）を配置

3. **シリアルモニターを閉じる**（重要）

4. **アップローダーを実行**
   - Ctrl+Shift+P（Mac: Cmd+Shift+P）でコマンドパレットを開き、「Upload LittleFS」を実行

### アップロード後の確認

```cpp
#include <LittleFS.h>

void listDir(const char *dirname, uint8_t levels) {
    File root = LittleFS.open(dirname);
    if (!root || !root.isDirectory()) return;

    File file = root.openNextFile();
    while (file) {
        Serial.print("FILE: ");
        Serial.println(file.name());
        file = root.openNextFile();
    }
}

void setup() {
    Serial.begin(115200);
    LittleFS.begin();
    listDir("/", 1);
}

void loop() {}
```

## ファイルモード

ファイルを開く際に、以下のモードを指定できます：

| モード | 説明 |
|--------|------|
| `FILE_READ` | 読み込みのみ |
| `FILE_WRITE` | 上書き（既存ファイルは削除） |
| `FILE_APPEND` | 追記 |

## 関連メソッド

| メソッド | 説明 |
|----------|------|
| `file.available()` | 読み込み可能なバイト数 |
| `file.read()` | 1バイト読み込む |
| `file.write()` | データを書き込む |
| `file.print()` | テキストを書き込む |
| `file.println()` | テキストを改行付きで書き込む |
| `file.seek(offset, mode)` | ファイルポジションを移動 |
| `file.size()` | ファイルサイズ（バイト） |
| `file.name()` | ファイル名 |
| `file.close()` | ファイルを閉じる |
| `file.isDirectory()` | ディレクトリかどうか判定 |
