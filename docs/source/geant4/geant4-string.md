# 文字列操作したい（``G4String``）

```cpp
G4String material_name = "G4_AIR";
```

``G4String``はGeant4内部で使用される文字列クラスです。
``std::string``クラスを継承しています。
``std::string``や``std::string_view``型の引数の値として使えます。

また、追加機能として``G4StrUtil``という名前空間も定義されています。

## C文字列に変換したい（``c_str``）

```cpp
G4String material_name = "G4_AIR";
printf("Material Name: %s", material_name.c_str())
// Material Name: G4_AIR
```

``G4String``クラスは、内部で暗黙の型変換をしてくれるそうですが、
``%s``指定子でフォーマット指定した場合は、
C文字列への変換を明示する必要があります。

:::{note}

G4Stringのクラスリファレンスを確認すると、
``deprecated``指定されたメンバー関数が多いです。
ヘッダーファイルのコメントにも
「``std::string``と同じインタフェースを提供する」
というような方針が書いてあります。
ゆくゆくは``std::string``に置き換わるのかも？

:::

## リファレンス

- [G4String](https://geant4.kek.jp/Reference/11.2.0/classG4String.html)
- [G4StrUtil](https://geant4.kek.jp/Reference/11.2.0/namespaceG4StrUtil.html)
