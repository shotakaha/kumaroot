# 一次粒子をしりたい（``PrimaryVertex``）

```cpp
// G4Event *aEvent
G4int n_vertex = aEvent->GetNumberOfPrimaryVertex();
G4PrimaryVertex vertex = aEvent->GetPrimaryVertex(id);

// vertex操作
G4ThreeVector position = vertex->GetPosition();
G4double x0 = vertex->GetX0();
G4double y0 = vertex->GetY0();
G4double z0 = vertex->GetZ0();
G4double t0 = vertex->GetT0();
G4int n_particle = vertex->GetNumberOfParticle();
G4PrimaryParticle *particle = vertex->GetPrimary(id);
```

``GetNumberOfPrimaryVertex``で、ひとつのイベント中の一次粒子（＝入射粒子）の数を取得できます。

インデックスを指定して``PrimaryVertex``を取得できます。

:::{seealso}

- [G4PrimaryVertex](https://apc.u-paris.fr/~franco/g4doxy/html/classG4PrimaryVertex.html)
- [G4PrimaryParticle](https://apc.u-paris.fr/~franco/g4doxy/html/classG4PrimaryParticle.html)

:::
