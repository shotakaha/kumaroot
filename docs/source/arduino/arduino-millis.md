# ミリ秒したい（`millis`）

```cpp
millis()
```

`millis()`で、起動してから現在までの経過時間をミリ秒で取得できます。

:::{note}

`millis()`は32ビットなので、約50日でオーバーフローします。
長期測定の場合は対応が必要です。

:::

## 起動時間したい

```cpp
unsigned long g_started;

void setup() {
    Serial.begin(115200);

    // 初期化処理いろいろ

    // 起動時刻を取得
    g_started = millis();
}

void loop() {
    unsigned long uptime = millis() - g_start;
    Serial.print("Uptime (ms): ");
    Serial.println(uptime);

    delay(1000);    // 1秒ごとに表示
}
```

`setup()`で基準となる時刻を取得しておくことで、
`loop()`内のタイムスタンプとして利用できます。

## オーバーフロー処理したい

```cpp
#include <Arduino.h>

uint32_t _previous_millis = 0;  前回の millis を保存
uint64_t _uptime64 = 0;

void uptime_start() {
    _previous_millis = millis();
    _uptime64 = 0;
}

uint64_t get_uptime() {
    uint32_t current = millis();

    // オーバーフロー検出
    if (current < _previous_millis) {
        _uptime64 += (uint64_t)0xFFFFFFFFUL + 1;
    }

    _uptime64 += (uint64_t)(current - _previous_millis);
    _previous_millis = current;

    return _uptime64;
}
```

オーバーフローすると`millis()`は0に戻ります。
そのとき`current`は`_previous_millis`より小さくなるため
`current < _previous_millis`で検出できます。

オーバーフローを検出したら、桁が繰り上がったことを記録しておくようにします。
32bitでオーバーフローするので`0xFFFFFFFFUL + 1`で1桁繰り上げできます。

`current - _previous_millis`はオーバーフローしてからの時刻差（マイナスの値）です。
`_uptime64`に加算することで、現在の経過時間が計算できます。

```cpp
void setup() {
    Serial.begin(115200);
    uptime_start();
}

void loop() {
    uint64_t uptime = get_uptime();
    Serial.print("Uptime (ms): ");
    Serial.println(uptime);

    // delay(1000)
}
```
