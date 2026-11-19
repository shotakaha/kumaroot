# 文字列操作したい（`G4String`）

```cpp
G4String material_name = "G4_AIR";
```

`G4String`は、Geant4で文字列を扱うための型です。
C++の標準の文字列型`std::string`の機能を、そのまま持っています。
そのため、`std::string`を受け取る関数にも`G4String`をそのまま渡せます。

文字列の変換や検索には、`G4StrUtil`という機能を使います。
Geant4 11.0から使えるようになり、古いメンバー関数（例：`toLower()`）の代わりに使うことが推奨されています。

:::{note}

`G4String`の古いメンバー関数の多くは、非推奨（`deprecated`）になっています。
新しく書くときは、この後の`G4StrUtil`の関数を使いましょう。

:::

## C文字列に変換したい（`c_str`）

```cpp
G4String material_name = "G4_AIR";
printf("Material Name: %s\n", material_name.c_str());
// 出力: Material Name: G4_AIR
```

`printf`の`%s`は、C言語の文字列（`const char*`）しか受け取れません。
`c_str()`は、`G4String`の中身をC言語の文字列として取り出します。

Geant4のコードでは、`printf`よりも`G4cout`を使うことが多いです。
`G4cout`なら、`c_str()`は不要です。

```cpp
G4String material_name = "G4_AIR";
G4cout << "Material Name: " << material_name << G4endl;
// 出力: Material Name: G4_AIR
```

## 文字列を大文字にしたい（`G4StrUtil::to_upper_copy`）

```cpp
G4String name = "g4_air";
G4String upper = G4StrUtil::to_upper_copy(name);
G4cout << upper << G4endl;  // 出力: G4_AIR
```

`G4StrUtil::to_upper_copy()`は、大文字にしたコピーを返します。
元の`name`は変わりません。

## 文字列に含まれるか調べたい（`G4StrUtil::contains`）

```cpp
G4String material_name = "G4_WATER";
if (G4StrUtil::contains(material_name, "WATER")) {
  G4cout << "水を使っています" << G4endl;
}
```

`G4StrUtil::contains()`は、文字列の中に別の文字列が含まれていれば`true`を返します。

## リファレンス

- [G4String](https://geant4.kek.jp/Reference/11.4.0/classG4String.html)
- [G4StrUtil](https://geant4.kek.jp/Reference/11.4.0/namespaceG4StrUtil.html)
