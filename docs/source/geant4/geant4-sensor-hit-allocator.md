# メモリを割り当てたい（``G4Allocator``）

```cpp
#include "G4VHit.hh"
#include "G4Allocator.hh"

class TrackerHit : public G4VHit
{
    inline void* operator new(size_t);
    inline void operator delete(void*);
};

//////////////////////////////////////////////////
// （スレッドローカルな）グローバル変数を定義
extern G4ThreadLocal G4Allocator<TrackerHit>* TrackerHitAllocator;

//////////////////////////////////////////////////
inline void* TrackerHit::operator new(size_t)
{
    // new演算子でメモリを割り当てるとき
    // {
    //     TrackerHit *hit = new TrackerHit();
    // }
    // 1. TrackerHitAllocatorに割り当てられたメモリのポインターを取得する
    // 2. 初期化されてない場合は、新しくG4Allocator<TrackerHit>オブジェクトを作成
    if(!TrackerHitAllocator) {
        TrackerHitAllocator = new G4Allocator<TrackerHit>;
    }
    return (void *) TrackerHitAllocator->MallocSingle();
};

//////////////////////////////////////////////////
inline void TrackerHit::operator delete(void *hit)
{
    // delete演算子でメモリを解放するとき
    //
    // {
    //     TrackerHit *hit = new TrackerHit();
    //     delete hit
    // }
    //
    // 1. TrackerHitAllocatorに割り当てられたメモリのポインターを解放する
    TrackerHitAllocator->FreeSingle((TrackerHit*)hit);
};
```

``G4Allocator``は、ヒープ領域に高速にメモリを割り当ててくれるGeant4のクラスです。
このクラスは必須ではありませんが、C++のメモリ管理に詳しくない場合は使うことがオススメされています。
自作したヒットクラスの中で、``new``演算子と``delete``演算子をインライン関数でオーバーロードして、
``G4Allocator``を使うようにカスタマイズしています。
