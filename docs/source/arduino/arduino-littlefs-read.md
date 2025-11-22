# ファイルを読み込みたい（`LittleFS.read`）

```c
File file = LittleFS.open(path, FILE_READ)
while (file.available()) {
    Serial.print(file.read());
}
Serial.println();
file.close();
```

## read_fileしたい

```c
#include <LittleFS.h>

void read_file(const char *path) {
    File file = LittleFS.open(path, FILE_READ);
    if (!file) {
        Serial.println("Failed to open file for reading");
        return;
    }

    Serial.println("File contents:");
    while (file.available()) {
        Serial.write(file.read());
    }
    Serial.println();
    file.close();
}

void setup() {
    LittleFS.begin();
    read_file("/config.txt");
}

void loop() {}
```
