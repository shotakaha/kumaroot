# JSON形式で送信したい（`ArduinoJson.serializeJson`）

```c
#include <ArduinoJson.h>

// メインループ
void loop() {

    // JSON形式のオブジェクトを静的メモリ確保
    StaticJsonDocument<200> doc;

    // データを代入
    doc["tmp"] = 25;
    doc["hmd"] = 60;

    // データを送信
    serializeJson(doc, Serial);
    Serial.println();
    // {"tmp":25,"hmd":60} + 改行
}
```

`ArduinoJson`ライブラリは、ArduinoやESP32などのマイコンでJSON形式を扱うための軽量ライブラリです。

JSON形式は人間にも機械にも読みやすい標準的なデータ形式です。
キーと値のペアでデータを整理するため、CSV形式よりも構造化されたデータを送信できます。

## JSONL形式で送信したい

```c
// JSONL形式に変換して送信する関数
void send_jsonl(StaticJsonDocument<200>& doc) {
    serializeJson(doc, Serial);
    Serial.println();
}
```

マイコンからデータを送信する場合、行末に改行を付与したJSONL（JSON Lines）形式で送信することで、複数のデータを1行ずつ効率的に処理できます。

```json
{"temperature":25,"humidity":60}
{"temperature":26,"humidity":58}
{"temperature":25,"humidity":62}
```
