# 文字列操作したい（`G4String`）

```cpp
G4String material_name = "G4_AIR";
```

`G4String`は、Geant4で使用される文字列クラスです。
C++標準の`std::string`を継承しており、
`std::string`型や`std::string_view`型の引数としてもそのまま利用できます。

また、文字列操作用の補助機能として
`G4StrUtil`という名前空間ベースのユーティリティ関数群も提供されています。
v11.0以降では、`G4String`の旧来のメンバー関数を使用せず、`G4StrUtil`の関数を使用することが推奨されています。

:::{note}

[G4Stringのクラスリファレンス](https://geant4.kek.jp/Reference/11.2.0/classG4String.html)を確認すると、
ほとんどのメンバー関数が
`[Deprecated function]`とマークされています。

これからGeant4アプリケーションを新規開発する場合は、
`std::string`を利用するのがよいかもしれません。

:::

## C文字列に変換したい（``c_str``）

```cpp
G4String material_name = "G4_AIR";
printf("Material Name: %s", material_name.c_str())
// Material Name: G4_AIR
```

`G4String`は、内部的に`std::string`として扱えるよう暗黙の型変換が定義されています。
C言語形式の`%s`指定子でフォーマット指定する場合は、
`c_str()`で明示的にC文字列へ変換する必要があります。



## リファレンス

- [G4String](https://geant4.kek.jp/Reference/11.2.0/classG4String.html)
- [G4StrUtil](https://geant4.kek.jp/Reference/11.2.0/namespaceG4StrUtil.html)
