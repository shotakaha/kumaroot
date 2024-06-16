# マクロしたい（``/control/execute``）

[前のページ](./geant4-command.md)で紹介したコマンド操作を、
ひとつファイルにまとめてマクロを作成できます。

```cfg
/control/execute ファイル名.mac
```

Geant4では、慣習的にマクロの拡張子を``.mac``としているようですが、
テキストファイルであればなんでもOKです。

## 起動時にマクロしたい（``G4UIManager``）

```cpp
int main(int argc, char** argv)
{
    // 第一引数がマクロの場合
    G4String fileName = argv[1];
    G4String command = "/control/execute ";
    G4UImanager* um = G4UImanager::GetUIpointer();
    um->ApplyCommand(command+fileName);
}
```

``main()``関数で``G4UImanager``を設定すると
アプリケーション起動時に、マクロを読み込むことができます。
