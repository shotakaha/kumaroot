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

ユーザーが定義した[SensorHitクラス](./geant4-sensor-hit.md)の中で、
1. ``G4Allocator``の定義
2. ``new``演算子の再定義
3. ``delete``演算子の再定
のメモリ割り当てに関係する箇所を抜粋しました。

``G4Allocator``クラスはGeant4に用意されている高速なメモリアロケーターです。
C++のメモリ管理に詳しくないひとは、とりあえず使っておけばよいと思います。

``G4ThreadLocal``はGeant4に用意されたスレッドローカル処理の関数です。
マルチスレッド処理に詳しくないひとは、とりあえず使っておけばよいと思います。

``new``演算子は、コンストラクターの前に実行される特殊関数です。
ここで``SensorHitAllocatorを使って、``SensorHit``クラスに必要なメモリ領域を割り当てています。

``delete``演算子は、デストラクターの後に実行される特殊関数です。
前述した``new``演算子で割り当てたメモリ領域を解放します。
