# ファイルを開きたい（`LittleFS.open`）

```c
File file = LittleFS.open(path, FILE_READ)
```

## 上書きしたい

```c
File file = LittleFS.open(path, FILE_WRITE)
```

## 追記したい

```c
File file = LittleFS.open(path, FILE_APPEND)
```
