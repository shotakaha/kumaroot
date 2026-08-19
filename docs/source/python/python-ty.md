# 型チェックしたい（`ty`）

```console
$ uv tool install ty
$ ty --version
ty 0.0.72

$ ty check ファイル名
$ ty check ディレクトリ名
```

`ty`は、Astral（`uv`や`ruff`と同じ開発元）が作っているRust製の型チェッカーです。
[mypy](./python-mypy.md)よりも高速に動作します。
[uv check](./python-uv.md)コマンドは、内部で`ty`を利用しています。

:::{note}

`ty`は開発初期のツールで、バージョン番号も`0.x`台です。
`mypy`ほど厳密な検査はまだ苦手な場合があるので、
既存プロジェクトでは`mypy`と併用しながら移行を検討するのがよさそうです。

:::

## インストールしたい（`ty`）

- `uv tool`でインストール

```console
$ uv tool install ty
```

- `uv`でプロジェクトに追加

```console
$ uv add ty --group dev
```

- `pipx`でインストール

```console
$ pipx install ty
```

## 設定したい（`[tool.ty.rules]`）

```toml
[tool.ty.rules]
unresolved-import = "error"
possibly-unresolved-reference = "warn"
```

`ty`の設定は、`pyproject.toml`の`[tool.ty.rules]`セクションで変更できます。
ルール名と、重要度（`error`・`warn`・`ignore`）を指定します。

```console
$ ty check --error possibly-unresolved-reference ファイル名
$ ty check --warn unresolved-import ファイル名
```

コマンドラインからも`--error`・`--warn`オプションでルールの重要度を一時的に上書きできます。

## ルールを確認したい（`ty explain rule`）

```console
$ ty explain rule ルールID
```

`ty explain rule`で、ルールの説明を確認できます。
引数を省略すると、すべてのルールの説明が表示されます。

## ファイルの変更を監視したい（`--watch`）

```console
$ ty check --watch
```

`--watch`（`-W`）オプションで、ファイルの変更を検知して自動的に再チェックできます。
コードを編集しながら型エラーをリアルタイムで確認したいときに便利です。

## リファレンス

- [ty](https://docs.astral.sh/ty/)
- [ty - GitHub](https://github.com/astral-sh/ty)
