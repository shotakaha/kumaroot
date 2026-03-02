# メモリ割り当てしたい（`G4Allocator<T>`）

```cpp
// 書式: G4ThreadLocal G4Allocator<T>* allocator;
// 例: SensorHit型のアロケーター

// include/SensorHit.hh で宣言する
extern G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator;

// src/SensorHit.cc で定義する（nullptrで実体化）
G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator = nullptr;
```

`G4Allocator<T>`はGeant4の高速メモリ管理機能です。
高頻度で生成・破棄されるオブジェクトのメモリ確保と解放の効率を最適化する
**メモリプール型のアロケーター** であり、
`G4Step`や`G4Track`の処理などGeant4内部でも利用されています。

ユーザーが明示的に利用する場面は、
前述した[ユーザー定義のヒットクラス](./geant4-sensor-hit.md)です。
対象のユーザー定義クラスで
`operator new()` と `operator delete()` をオーバーロードし、
その内部で`MallocSingle()` / `FreeSingle()` を呼び出して利用します。

:::{note}

通常の`new`および`delete`演算子は、動的にメモリを確保・解放するためオーバーヘッドが生じます。
Geant4のイベント処理では、オブジェクトを大量に生成・削除するため、このオーバーヘッドが大きくなります。
`G4Allocator`であらかじめ確保したメモリブロックを使い回すことで、このオーバーヘッドを大幅に軽減します。

:::

`G4ThreadLocal`と併用することで、`G4Allocator`をスレッドごとに分離でき、
マルチスレッド環境でも安全に利用できます。

## メモリを割り当てたい（`MallocSingle`）

```cpp
SensorHitAllocator->MallocSingle();
```

`MallocSingle`は、`G4Allocator`が管理しているメモリプールから、T型（ここでは`SensorHit`型）オブジェクト1つ分のメモリを割り当てる関数です。
これはC++標準の`malloc`に相当します。

通常は、以下のように
`new`演算子（`operator new`）をオーバーロードして使います。

```cpp
void* SensorHit::operator new(size_t)
{
    if(!SensorHitAllocator) {
        SensorHitAllocator = new G4Allocator<SensorHit>;
    }
    return (void *) SensorHitAllocator->MallocSingle();
};
```

`operator new()`は、コンストラクターが呼ばれるまえに実行される特殊関数です。
ここで`SensorHitAllocator`を初期化し、必要なメモリを確保しています。

## メモリを解放したい（`FreeSingle`）

```cpp
SensorHitAllocator->FreeSingle(型名)
```

`FreeSingle`は、`MallocSingle`で割り当てたメモリを再びメモリプールに返す関数です。
C++標準の`free`に相当します。

通常は、`new`演算子（`operator delete`）をオーバーロードして使います。

```cpp
void SensorHit::operator delete(void *hit)
{
    SensorHitAllocator->FreeSingle((SensorHit*)hit);
};
```

`operator delete()`演算子は、デストラクターの後に実行される特殊関数です。
前述の`new`演算子で割り当てたメモリを、ここでアロケーターに返却しています。

## ヘッダーファイル（`include/SensorHit.hh`）

```cpp
#include "G4VHit.hh"
#include "G4Allocator.hh"

class SensorHit : public G4VHit
{
  public:
    void* operator new(size_t);
    void operator delete(void*);
    // その他のメンバー変数や関数
};

//////////////////////////////////////////////////
// （スレッドローカルな）グローバル変数を宣言
// 1. スレッドごとにSensorHit型のメモリを管理するためのアロケータ
// 2. そのメモリ領域を SensorHitAllocator という名前で管理する
// 3. 実体の定義は .cc ファイルに記述する
extern G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator;
```

`G4Allocator`はユーザー定義のヒットクラスと同じファイルで宣言します。
`SensorHitAllocator`のようにグローバルに定義することで、
どこからでも`MallocSingl()e`、`FreeSingle()`を呼び出して効率的にメモリを管理できます。

```cpp
extern G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator;
```

Geant4はマルチスレッド環境がデフォルトになっているため、
各スレッドが独立してアロケーターを保持できるように`G4ThreadLocal`を併用します。

また、C++ではグローバル変数を複数のファイルから参照する場合、
`extern`を使って宣言する必要があります。

## ソースファイル（`src/SensorHit.cc`）

```cpp
#include "SensorHit.hh"

G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator = nullptr;

void* SensorHit::operator new(size_t)
{
    // new演算子でメモリを割り当てるとき
    // {
    //     SensorHit *hit = new SensorHit();
    // }
    // 1. SensorHitAllocatorに割り当てられたメモリのポインターを取得する
    // 2. 初期化されてない場合は、新しくG4Allocator<TrackerHit>オブジェクトを作成
    if(!SensorHitAllocator) {
        SensorHitAllocator = new G4Allocator<SensorHit>;
    }
    return (void *) SensorHitAllocator->MallocSingle();
};


//////////////////////////////////////////////////
void SensorHit::operator delete(void *hit)
{
    // delete演算子でメモリを解放するとき
    //
    // {
    //     SensorHit *hit = new SensorHit();
    //     delete hit
    // }
    //
    // 1. SensorHitAllocatorに割り当てられたメモリのポインターを解放する
    SensorHitAllocator->FreeSingle((SensorHit*)hit);
};
```

`SensorHitAllocator`は`nullptr`で初期化します。

`new`するときは、`SensorHitAllocator`がまだ確保できていない場合のみ、
`new G4Allocator<SensorHit>`でアロケーターを生成し、
`SensorHitAllocator->MallocSingle()`でメモリプールからオブジェクト1つ分の領域を確保します。

`delete`するときは、オブジェクトのメモリをOSに返却せず、
`SensorHitAllocator->FreeSingle(...)`でメモリプールに返却し、
再利用できる状態にします。

## 割り当てサイズをしりたい（``GetAllocatedSize``）

```cpp
// 割り当てられた合計サイズ
G4int size = SensorHitAllocator->GetAllocatedSize();

// 現在のページのサイズ
G4int page_size = SensorHitAllocator->GetPageSize();

// 割り当てられたページ数
G4int n_pages = SensorHitAllocator->GetNoPages();
```

``GetAllocatedSize``で、割り当てられたメモリの合計サイズを確認できます。

## リファレンス

- [G4Allocator](https://geant4.kek.jp/Reference/11.2.0/classG4Allocator.html)
