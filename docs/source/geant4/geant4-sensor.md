# 有感検出器したい

有感検出器（Sensitive Detector）は、シミュレーションの結果を取得するための仕組みです。
Geant4の出力を得るために、ユーザーが体得する必要があるクラスです。

以下では、あらゆる情報を得られる理想的な検出器を想定して、
検出器本体を``Sensor``クラス、
ヒットひとつの情報を``SensorHit``クラス、
検出器の中のすべてのヒットを格納する領域を``SensorHitsCollection``型、
という名前にして、Sensitive Detectorを作る過程を分割して整理しました。

```{toctree}
geant4-sensor-sensitivedetector
geant4-sensor-hit
geant4-sensor-hit-hitscollection
geant4-sensor-hit-allocator
geant4-sensor-hit-draw
geant4-sensor-hit-print
geant4-sensor-sdmanager
geant4-sensor-hit-hitsmap
geant4-sensor-hit-hcofthisevent
```
