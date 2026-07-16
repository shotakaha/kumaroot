# バージョン情報したい（`platform`）

```python
import platform

# OS情報
platform.version()

# プラットフォーム情報（OS名・バージョン・アーキテクチャなど）
platform.platform()

# Python情報
platform.sys.version
platform.sys.executable
```

`platform`モジュールで、実行環境のバージョンを確認できます。
`platform`の中で`sys`や`os`モジュールをインポートしているため、
それらのモジュールがもつメソッド／変数にもアクセスできます。

:::{caution}

`platform.sys`や`platform.os`は、`platform`モジュールが公開しているAPIではなく、
内部実装でこれらのモジュールを`import`しているために外側から見えてしまっているだけです。
将来のPythonバージョンで動作しなくなる可能性もあるので、
`sys`や`os`の情報が欲しい場合は、素直に`import sys`・`import os`するほうが安全です。

:::

よく使う関数には、以下のようなものがあります。

```python
platform.system()          # OS名（'Windows' / 'Linux' / 'Darwin' など）
platform.machine()         # マシンのアーキテクチャ（'x86_64' / 'arm64' など）
platform.python_version()  # Pythonのバージョン文字列（例: '3.12.3'）
```
