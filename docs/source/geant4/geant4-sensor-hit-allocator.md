# メモリ割り当てしたい（``G4Allocator``）

```cpp
#include "G4VHit.hh"
#include "G4Allocator.hh"

class SensorHit : public G4VHit
{
    inline void* operator new(size_t);
    inline void operator delete(void*);
};

//////////////////////////////////////////////////
// （スレッドローカルな）グローバル変数を定義
// 1. スレッドごとにSensorHit型に必要なメモリを確保する
// 2. そのメモリ領域を SensorHitAllocator と名付ける
extern G4ThreadLocal G4Allocator<SensorHit>* SensorHitAllocator;

//////////////////////////////////////////////////
inline void* SensorHit::operator new(size_t)
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
inline void SensorHit::operator delete(void *hit)
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

``G4Allocator``は、ヒープ領域に高速にメモリを割り当ててくれるGeant4のクラスです。
このクラスは必須ではありませんが、C++のメモリ管理に詳しくない場合は使うことがオススメされています。
自作したヒットクラスの中で、``new``演算子と``delete``演算子をインライン関数でオーバーロードして、
``G4Allocator``を使うようにカスタマイズしています。
