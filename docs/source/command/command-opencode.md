# OpenCodeしたい（`opencode`）

```console
$ opencode
```

`opencode`はターミナル上で動作するオープンソースのAIコーディングエージェントです。
[Spec-Kit](./command-specify.md)でもサポートされています。

複数のAIモデルに対応しており、ユーザーが切り替えて利用できます。
推奨されているモデルは[Claude (Sonnet 4.5)](./command-claude.md)です。

## インストールしたい（`opencode`）

```console
$ brew install opencode
$ opencode --version
0.14.7
```

Homebrewで`opencode`をインストールできます。

## AIモデルを確認したい（`models`）

```console
$ opencode models
opencode/qwen3-coder
opencode/claude-opus-4-1
opencode/kimi-k2
opencode/claude-sonnet-4-5
opencode/gpt-5-codex
opencode/claude-3-5-haiku
opencode/glm-4.6
opencode/grok-code
opencode/code-supernova
opencode/claude-sonnet-4
opencode/gpt-5
anthropic/claude-3-5-sonnet-20241022
anthropic/claude-3-5-sonnet-20240620
anthropic/claude-3-opus-20240229
anthropic/claude-sonnet-4-5-20250929
anthropic/claude-sonnet-4-20250514
anthropic/claude-opus-4-20250514
anthropic/claude-3-5-haiku-20241022
anthropic/claude-3-haiku-20240307
anthropic/claude-3-7-sonnet-20250219
anthropic/claude-opus-4-1-20250805
anthropic/claude-3-sonnet-20240229
```
