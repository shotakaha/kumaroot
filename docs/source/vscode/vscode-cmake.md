# CMakeしたい

1. [CMake](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)
2. [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

## ユーザー設定

```json
{
    "cmake.configureOnOpen": false,
    "cmake.options.statusBarVisibility": "visible",
    "cmake.showOptionsMovedNotification": false,
    "cmake.useCMakePresets": "never",
    "cmake.pinnedCommands": [
        "workbench.action.tasks.configureTaskRunner",
        "workbench.action.tasks.runTask"
    ],
}
```

## ワークスペース設定

```json
{
    "cmake.generator": "Unix Makefiles",
    "cmake.sourceDirectory": "${workspaceFolder}/source用ディレクトリ",
    "cmake.buildDirectory": "${workspaceFolder}/build用ディレクトリ",
    "cmake.installPrefix": "${workspaceFolder}"
}
```

CMakeを走らせるときの設定は、ワークスペースごとに設定するとよいです。
上記サンプルは``Makefile``を使ってビルドする場合の設定です。
