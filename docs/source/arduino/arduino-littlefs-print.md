# ファイルに書き込みたい

```c
File file = LittleFS.open(path, FILE_WRITE);
file.print("message");
file.close();
```

## write_fileしたい

```c
#include <LittleFs.h>

void write_file(const char *path, const char *message) {
    File file = LittleFS.open(path, FILE_WRITE);
    if (!file) {
        Serial.println("Failed to open file for writing");
        return;
    }

    if (file.print(message)) {
        Serial.println("File written");
    } else {
        Serial.println("Write failed");
    }
    file.close();
}

void setup() {
    LittleFS.begin();
    write_file("/config.txt", "Hello, World");
}

void loop() {}
```

## append_fileしたい

```cpp
#include <LittleFS.h>

void appendFile(const char *path, const char *message) {
    File file = LittleFS.open(path, FILE_APPEND);
    if (!file) {
        Serial.println("Failed to open file for appending");
        return;
    }
    if (file.print(message)) {
        Serial.println("Message appended");
    } else {
        Serial.println("Append failed");
    }
    file.close();
}

void setup() {
    LittleFS.begin();
    appendFile("/log.txt", "New log entry\n");
}

void loop() {}
```
