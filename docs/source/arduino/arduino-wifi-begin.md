# Wi-Fi接続したい

```c
#include <WiFi.h>

const char* ssid = "EXISTING_SSID_NAME";
const char* password = "EXISTING_WIFI_PASSWORD";
WiFi.begin(ssid, password);
```

`WiFi.begin`関数で既存のWi-Fi機器に接続できます。
`setup()`関数に記述します。

## リトライ処理したい

```c
#include <WiFi.h>

const char* ssid = "SET_SSID_NAME";
const char* password = "SET_PASSWORD";

void wifi_init_sta() {
    // ステーションモード
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password)

    Serial.println("Connecting to WiFi...");

    // 接続するまでのリトライ処理
    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < 20) {
        delay(500);
        Serial.print(".");
        attempts++;
    }

    if (WiFi.status() == WL_CONNECTED) {
        Serial.println();
        Serial.println("WiFi connected!");
        Serial.print("IP address: ");
        Serial.println(WiFi.localIP());
    } else {
        Serial.println();
        Serial.println("Failed to connect to WiFi");
    }
}

void setup() {

    Serial.begin(115200);
    delay(1000);
    Serial.println();

    wifi_init_sta();
}

void loop() {};
```

WiFi接続に失敗することもあるはずなので、リトライ処理を追加したサンプルです。

最初に`WiFi.mode(WIFI_STA)`でステーションモードを明示的に設定しています。
基本は接続の状態が成功（`WL_CONNECTED`）になるまで`while`ループします。
ただし、接続に失敗し続けた時の無限ループを防止するため、リトライする回数に上限（ここでは20回）を設けています。

## ステーション接続に切り替えたい

```c
void wifi_switch_sta() {
    // Disconnect ALL connections
    WiFi.disconnect(true);
    delay(100);

    wifi_init_sta();
}

void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println();
    wifi_init_sta();
}

void loop() {

    // "switch sta"コマンドでAP -> STAに切り替え
    if (Serial.available()) {
        String cmd = Serial.readStringUntil('\n');
        if (cmd == "switch sta") {
            wifi_switch_sta();
        }
    }
}
```

ループ処理の途中で、APモードからSTA（ステーション）モードに切り替えるサンプルです。

ここでは`switch sta`コマンドを受け取ったときに`wifi_switch_sta`が実行されます。
内部では`wifi_init_sta`を再利用しています。
