# 描画したい（``G4VHit::Draw``）

```cpp
void SensorHit::Draw()
{
    G4debug << "SensorHit::Draw" << G4endl;
    auto vm = G4VVisManager::GetConcreteInstance();
    if (vm)
    {
        G4Circle circle(fXYZ);
        circle.SetScreenSize(4.);
        circle.SetFillStyle(G4Circle::filled);
        G4VisAttributes color{G4Colour::Red()};
        circle.SetVisAttributes(color);
        vm->Draw(circle);
    };
};
```

Qt画面などに描画するときの設定です。
ヒット点を赤い丸で描画するように設定しています。
