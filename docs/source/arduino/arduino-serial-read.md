# データを受信したい（`Serial.read`）

```c
while (Serial.available()) {
    char c = Serial.read();
    Serial.print(c);
}
```

`Serial.read`関数で、シリアルデータを受信できます。
`Serial.available`関数を使ったデータ確認と組み合わせて、1文字（1バイト）ずつ連続的に読み出すのが一般的です。

## 行単位で受信したい（`Serial.readStringUntil`）

```c
String line = Serial.readStringUntil('\n');
Serial.println("Received: " + line);
```

`readStringUntil`で、指定した改行文字まで受信できます。
行単位で読み込みたい場合は`"\n"`とします。

## 固定長で受信したい（`Serial.readBytesUntil`)

```c
int buffer_size = 64;
byte buffer[buffer_size];

// 読み出しのタイムアウト設定
Serial.setTimeout(500);

// データ受信
size_t bytes_read = Serial.readBytesUntil('\n', buffer, buffer_size - 1);

// データサイズがバッファーサイズより大きかった場合の処理
if (bytes_read == (buffer_size - 1)) {
    while (Serial.available()) {
        Serial.read();
    }
    Serial.println("Overflowed: Cleared remaining data.");
}

// データサイズが0だった場合（なにもしない）
if (bytes_read == 0) {
    Serial.println("Empty data.")
}

// trailing spaceの処理
while (bytes_read > 0 &&
        (buffer[bytes_read - 1] == '\r' ||
        buffer[bytes_read - 1] == ' ' ||
        buffer[bytes_read - 1] == '\t')
    ) {
        bytes_read--;
    }

```

`readBytesUntil`で固定長で受信できます。
メモリを節約したい場合に使用します。

## リファレンス

- [Serial.read](https://docs.arduino.cc/language-reference/en/functions/communication/serial/read/)
- [Serial.readBytes](https://docs.arduino.cc/language-reference/en/functions/communication/serial/readBytes/)
- [Serial.readBytesUntil](https://docs.arduino.cc/language-reference/en/functions/communication/serial/readBytesUntil/)
- [Serial.readString](https://docs.arduino.cc/language-reference/en/functions/communication/serial/readString/)
- [Serial.readStringUntil](https://docs.arduino.cc/language-reference/en/functions/communication/serial/readStringUntil/)
- [Serial.setTimeout](https://docs.arduino.cc/language-reference/en/functions/communication/serial/setTimeout/)
