# アクリルを作りたい

```cpp
G4NistManager *nist = G4NistManager::Instance();
G4Material *Acrylic = nist->FindOrBuildMaterial("G4_PLEXIGLASS");
```

``G4_PLEXIGLASS``でアクリル材（アクリル樹脂）を生成できます。

:::{note}

アクリル樹脂で作ったガラスのことを「プレキシガラス」（商標名）と呼ぶそうです。
この呼び方を知らなかったのでデータシートから検索できず、自分で作るしかないと思っていました。
構成する元素も密度も同じなので、代用してOKと思います。

:::

## カスタムしたい

```cpp
G4NistManager *nist = G4NistManager::Instance();
G4Element H = nist->FindOrBuildElement("G4_H");
G4Element C = nist->FindOrBuildElement("G4_C");
G4Element O = nist->FindOrBuildElement("G4_O");

G4Material *Acrylic = new G4Material("Acrylic", density=1.19*g/cm3, nelements=3);
Acrylic->AddElement(C, 5);
Acrylic->AddElement(H, 8);
Acrylic->AddElement(O, 2);
```

構成する元素の情報はNISTデータを参照しています。

:::{note}

``G4Element``オブジェクトを取得する場合は``FindOrBuildElement``を使います。

:::
