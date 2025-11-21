# ループ処理したい（`loop`）

```c
void loop() {

    // センサー値の読み込み
    int value = analogRead(A0);

    // 条件処理
    if (value > 512) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }

    // 一定時間待機
    delay(100);
}
```

`loop`関数は、Arduinoを初期化したあとに繰り返し実行される特殊な関数です。
ボードを使って実現したいメインの処理はすべてこの`loop`関数の中に定義します。

ArduinoではC言語の関数が利用できます。
ループ内の処理を関数化／モジュール化して整理できます。

:::{tip}

Arduinoの開発環境にArduino IDEとPlatformIOがあります。

複数ファイルに分けてモジュール化したい場合は、[PlatformIO](./arduino-platformio.md) の利用をオススメします。

Arduino IDEではスケッチファイルが1つのディレクトリで管理されるため、大規模なプロジェクトではPlatformIOの方が構造的に整理しやすいです。

:::
