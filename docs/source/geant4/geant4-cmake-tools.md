# CMake Toolsしたい

```json
// .vscode/settings.json
{
    "cmake.generator": "Unix Makefiles",
    "cmake.sourceDirectory": "${workspaceFolder}/B2a",
    "cmake.buildDirectory": "${workspaceFolder}/build",
    "cmake.installPrefix": "${workspaceFolder}"
}
```

エディターが``VS Code``の場合、``CMake Tools``プラグインを設定する快適になります。
一度CMakeしたconfigureファイルの設定から、必要なライブラリを読み込み、コード補完を提案してくれるようになります。

Geant4のクラス名とメソッド名は、長いものが多いため、
補完機能を使うことでタイプミスを減らすことができます。

## リファレンス

- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
