# データ送信したい（`Serial.print` / `Serial.println`）

```c
void loop() {

    int uptime = get_uptime();
    int duration = get_duration();

    Serial.print(uptime);
    Serial.print(" ");
    Serial.print(duration);
    Serial.println();
}
```

`Serial.print()` でデータを送信し、`Serial.println()` で改行を付けます。

## 複数のデータを送信したい

```c
void loop() {
    int temp = 25;
    int humidity = 60;

    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.print(", Humidity: ");
    Serial.println(humidity);
}
```

## 浮動小数点数を送信したい

```c
void loop() {
    float voltage = 3.14159;

    Serial.print("Voltage: ");
    Serial.println(voltage);
}
```

## メモリを節約したい（Fマクロ）

```c
void loop() {
    // F()マクロを使わない場合
    Serial.println("Temperature: 25C");

    // F()マクロを使う場合（推奨）
    Serial.println(F("Temperature: 25C"));
}
```

文字列リテラルを`F()`マクロで囲むとメモリを節約できます。
通常はSRAMを利用しますが、Fマクロはフラッシュメモリを使用します。
メモリ限定の環境ではオススメです。

## CSV形式で送信したい

```c
void send_csv(int data[], int size) {
    for (int i = 0; i < size; i++) {
        Serial.print(data[i]);
        if (i < size - 1) {
            Serial.print(",");
        }
    }
    Serial.println();
}
```
