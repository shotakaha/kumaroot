# フォーマッター／リンターしたい（`biome`）

```console
$ biome format --write .
$ biome lint .
```

`biome`はJS（やTS）用のフォーマッター＆リンターです。
ゼロコンフィグで利用できます。
Rust製で高速に動作します。

## インストールしたい

```console
// プロジェクトにインストール
$ npm i -D --save-exact @biomejs/biome
```

`-D`（`--save-dev`）オプションで`devDependencies`にインストールします。
`--save-exact`オプションでバージョンを固定できます。

## フォーマッターしたい（`biome format`）

```console
$ biome format .
$ biome format --write .
```

`biome format`でフォーマットが必要な箇所を検出できます。
`--write`オプションで、ファイルを変更します。

## リンターしたい（`biome lint`）

```console
$ biome lint
```

`biome lint`でリンターできます。

## 設定したい（`biome.json`）

```console
$ biome init
// -> biome.json
```

`biome init`コマンドで設定ファイル（`biome.json`）を生成できます。
ゼロコンフィグ（＝設定ファイル）で使い始められますが、
きちんとしたプロジェクトの場合は、設定を追加しておくとよいです。

```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "include": ["gaslamp/", "pilotlamp/", "scripts/", "*.js", "*.ts"],
    "ignore": ["node_modules/", "docs/", "coverage/"],
    "ignoreUnknown": true
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2
  },
  "organizeImports": {
    "enabled": true
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double"
    }
  }
}
```
