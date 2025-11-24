# バッファリングしたい

```c
#include <Arduino.h>

QueueHandle_t xQueue;
xQueue = xQueueCreate(
    10,    // キューの要素数
    sizeof(int)    // 1要素のサイズ
)
```

`FreeRTOS Queue`ライブラリで、FIFOバッファーを利用できます。
このライブラリはArduinoライブラリ（`Arduino.h`）に含まれているため、
追加のインクルードは不要です。

## キューを作成したい（`xQueueCreate`）

```c
static QueueHandle_t xQueue;

void setup() {
    xQueue = xQueueCreate(10, sieof(int));
}
```

`QueueHandle_t`でQueueオブジェクトのポインターを作成し、`xQueueCreate`でキュー用の配列をメモリ上に確保します。

`QueueHandle_t`は
キューを操作するためのハンドルです。
キュー用メモリは、一度だけ作って使い回すのが基本なので、
`static`（または`static`グローバル）に定義して、`setup`関数で初期化するの標準的な設計です。

:::{note}

`xQueueCreate`は内部で`malloc`して動的にメモリを確保します。
メモリ制限がシビアで、完全にユーザー制御したい場合は
`xQueueCreateStatic`を使います。

:::

## キューから受け取りたい（`xQueueReceive`）

```c
int rx;
(xQueueReceive(xQueue, &rx, portMAX_DELAY)
```

`xQueueReceive`関数でキューからデータを受け取ることができます。
キューは基本的にFIFOバッファーとなっているため、
バッファーの先頭のデータが取り出されます。

```c
void loop() {
    int rx;

    // キューにデータがあれば1つ取り出す
    // 非ブロッキング処理： 即時取り出しを指定。空ならばスキップ
    if (xQueueReceive(xQueue, &rx, 0) == pdPASS) {
        // キューから取り出したデータを処理
        Serial.println(rx);
    }

    //
    doMainStuff();
}
```

## キューに送りたい（`xQueueSend`）

```c
int value = 123;
xQueueSend(xQueue, &value, portMAX_DELAY);
```

`xQueueSend`関数でキューにデータを追加できます。
キューは基本的にFIFOバッファーとなっているため、
バッファーの末尾にデータが追加されます。

バッファーが一杯のときの対応は[どう設定するか調べる]

## 割り込みしたい（`xQueueSendFromISR`）

```c
xQueueSendFromISR(xQueue, &value);
```

`xQueueSendFromISR`関数で、割り込み（ISR）からキューにデータを追加できます。

## 命名規則

FreeRTOSのライブラリは、名前の先頭に
`x` / `v` / `ux` / `pv` などのプリフィクスが付いた
FreeRTOS固有の形式
（型プリフィクス付きの`PascalCase`）
です。

| prefix | 戻り値の型 | 例 |
|---|---|---|
| `x` | `BaseType_t` | `xQueueSend` |
| `v` | `void` | `vTaskDelay` |
| `ux` | `unsigned BaseType_t` | `uxQueueMessagesWaiting` |
| `pv` | `void*` | `pvPortMalloc` |
| `pc` | `char*` | `pcTaskGetName` |
| `pd` | `bool` | `pdTRUE` / `pdFALSE` |
