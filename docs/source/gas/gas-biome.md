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

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "scripts": {
        "format:check": "biome format .",
        "format:write": "biome format --write .",
        "lint:check": "biome lint .",
        "lint:fix": "biome lint --fix .",
        "...": "..."
    }
}
```

```console
$ npm run format:write
$ npm run lint:check
```

`check`系（変更しない）と`write`/`fix`系（変更する）を分けておくと、
CIでは`check`系を、ローカルでは`write`/`fix`系を使う、という使い分けがしやすくなります。

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
$ biome lint --fix
```

`biome lint`でリンターできます。
`--fix`オプションで、自動修正できる箇所を修正します。

:::{hint}

`biome check`を使うと、フォーマット・リント・import整理（後述の`assist`）を
まとめて1コマンドで実行できます。
CIでチェックだけしたい場合は`biome ci`が便利です。

:::

## 設定したい（`biome.json`）

```console
$ biome init
// -> biome.json
```

`biome init`コマンドで設定ファイル（`biome.json`）を生成できます。
ゼロコンフィグ（＝設定ファイルなし）で使い始められますが、
きちんとしたプロジェクトの場合は、設定を追加しておくとよいです。

```json
{
  "$schema": "https://biomejs.dev/schemas/2.5.8/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "includes": [
      "**/*.js",
      "**/*.ts",
      "!**/node_modules/",
      "!**/dist/",
      "!**/docs/",
      "!**/coverage/"
    ],
    "ignoreUnknown": true
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2
  },
  "assist": {
    "actions": {
      "source": {
        "organizeImports": "on"
      }
    }
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

`files.includes`に、対象とするファイルのパターンと、
除外したいパターン（`!`で始まる否定パターン）をまとめて指定します。
Biome 2系では、`files.include`と`files.ignore`のような分離した書き方は廃止され、
このように1つの配列にまとめる形式に統一されました。

`assist.actions.source.organizeImports`で、`import`文の並び替えを有効化できます。
（Biome 1系にあった`organizeImports.enabled`は2系で廃止され、`assist`配下に統合されています。）

:::{caution}

Biomeは1系から2系への移行でいくつかの設定項目が変わっています。
古いバージョン向けの設定例をそのまま使うと、`Found an unknown key`のようなエラーになることがあります。
`biome migrate`コマンドで、古い設定ファイルを現在のバージョン向けに自動変換できます。

:::

## リファレンス

- [Biome](https://biomejs.dev/)
- [Configuration](https://biomejs.dev/reference/configuration/)
