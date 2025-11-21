# 初期化したい（`setup`）

```c
void setup() {
    // 初期化処理
    Serial.begin(115200);
    delay(500);
    Serial.println(F("Finished initialization"));
}
```

`setup`関数は、Arduinoを起動したときに一度だけ実行される特殊な関数です。
ボードの初期化やピンモードのアサインなど、初期化に必要な処理を定義します。
