# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # バージョン情報したい
#
# - ``platform``
# - ``sys``
# - ``os``

import platform
import sys
import os

# ## OS情報
#
# - `uname`コマンドの内容を取得できる
#   - ``os.uname``と``platform.uname``がある
#   - ``platform.uname``を使えばよさそう

os.uname()

platform.uname()

# - プラットフォーム名（OS名）を取得できる
#   - ``sys.platform``と``platform.system``がある
#   - ``platform.system``を使えばよさそう
# - macOSの場合`Darwin`になる   

sys.platform

platform.system()

# - ホスト名を確認できる

platform.node()

# - リリース番号を確認できる

platform.release()

# - OS情報の詳細を確認できる

platform.version()

# ## アーキテクチャー

platform.platform()

platform.mac_ver()

platform.machine()

platform.processor()

platform.architecture()

os.cpu_count()

# ## Python情報

# - 実行時のPythonパスを確認できる
#   - ``sys``しかない

sys.executable

platform.sys.executable

sys.implementation

sys.version

platform.python_version()

platform.python_version_tuple()

platform.python_build()

platform.python_branch()

platform.python_compiler()

platform.python_implementation()

platform.python_revision()
