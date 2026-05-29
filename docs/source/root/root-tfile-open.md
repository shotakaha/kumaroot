# ファイルを開きたい（`TFile::Open`）

```cpp
TFile *file = TFile::Open("source.root");
if (!file || file->IsZombie()) {
    std::cerr << "Error opening file: source.root" << std::endl;
    return;
}
```

`TFile::Open`はファイルを開くための静的メソッドです。
第一引数（`name`）にはファイル名を指定します。
第二引数（`option`）にはファイルを開くモードを指定します。
デフォルトは読み取り専用モード（`read`）です。

ファイルが存在しない場合`nullptr`となるため`!file`でエラーを検出できます。
また、ファイルが正常に開けなかった場合は`IsZombie()`が`true`になるため、こちらでもエラーを検出できます。

## ファイルを作成したい（`recreate`）

```cpp
TFile* file = TFile::Open("output.root", "recreate");
if (!file || file->IsZombie()) {
    std::cerr << "Error creating file: output.root" << std::endl;
    return;
}
```

ファイルを作成する場合は、第二引数に`recreate`（もしくは`RECREATE`）を指定します。
同名のファイルが存在する場合は上書きします。

## ファイルを上書きしたくない（`new` / `create`）

```cpp
TFile *f = TFile::Open("output.root", "create");
if (!f || f->IsZombie()) {
    std::cerr << "Error: File already exists. Use 'recreate' mode to overwrite." << std::endl;
    return;
}
```

`create`もしくは`new`モードを指定してファイルを作成できます。
同名のファイルが存在する場合はエラーになります。

## ファイルを追記したい（`update`）

```cpp
TFile* f = TFile::Open("output.root", "update");
if (!f || f->IsZombie()) {
    std::cerr << "Error opening file for update: output.root" << std::endl;
    return;
}
```

`update`モードを指定してファイルを開くと、既存のファイルに追記できます。
ファイルが存在しない場合は新規作成します。

## 上書き確認したい（`TFile::Open` / `std::filesystem`）

```cpp
#include <TFile.h>
#include <filesystem>
#include <iostream>

std::string filename = "output.root";
if (std::filesystem::exists(filename)) {
    std::cout << "File " << filename << " already exists. Do you want to overwrite it? (y/n): ";
    char response;
    std::cin >> response;
    if (response != 'y' && response != 'Y') {
        std::cerr << "Aborted." << std::endl;
        return;
    }
}

TFile* f = TFile::Open(filename.c_str(), "recreate");
```

ファイルを作成するときに、同名のファイルが存在した場合にユーザーに上書き確認するサンプルです。
C++17以降の`std::filesystem`を使用して、ファイルの存在を確認しています。
ユーザーが上書きを拒否した場合は、処理を中断します。

:::{note}
`FileStat_t`と`TSystem::GetPathInfo`を使ってファイルの存在を確認する方法もありますが、C++17以降は`std::filesystem`を使う方が簡単なようです。
:::
