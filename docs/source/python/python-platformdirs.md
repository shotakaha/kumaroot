# 定番ディレクトリしたい（`platformdirs`）

```python
import platformdirs
platformdirs.user_data_dir("パッケージ名")
platformdirs.user_cache_dir("パッケージ名")
platformdirs.user_log_dir("パッケージ名", ensure_exists=True)
```

各種データを保存するディレクトリ名はOSによって異なります。
``platformdirs``を使うと定番パスを取得できます。
また、``ensure_exists``オプションを使うと、パスが存在しない場合に作成できます。

以下は``macOS``で確認しました。

:::{note}

`_dir`で終わる関数（`user_data_dir`など）は文字列（`str`）を返し、
`_path`で終わる関数（`user_data_path`など）は``pathlib.Path``オブジェクトを返します。
``pathlib``で後続の処理をしたい場合は`_path`系を使うと便利です。

:::

## ユーザーデータしたい（``user_data_dir``）

```python
platformdirs.user_data_dir("パッケージ名")
# '~/Library/Application Support/パッケージ名'

platformdirs.user_data_path("パッケージ名")
# PosixPath('~/Library/Application Support/パッケージ名')
```

:::{note}

Windowsでは、第二引数``appauthor``で発行元（会社名など）を指定できます
（``platformdirs.user_data_dir("パッケージ名", "発行元")``）。
macOS／Linuxではパスに反映されませんが、Windowsではパスの一部として使われます。

:::

## キャッシュデータしたい（``user_cache_dir``）

```python
platformdirs.user_cache_dir("パッケージ名")
# '~/Library/Caches/パッケージ名'

platformdirs.user_cache_path("パッケージ名")
# PosixPath('~/Library/Caches/パッケージ名')
```

## 設定ファイルしたい（``user_config_dir``）

```python
platformdirs.user_config_dir("パッケージ名")
# '~/Library/Application Support/パッケージ名'

platformdirs.user_config_path("パッケージ名")
# PosixPath('~/Library/Application Support/パッケージ名')
```

アプリケーションの設定ファイルを保存する場所です。
macOSでは`user_data_dir`と同じパスになりますが、
LinuxやWindowsでは異なるパスになります。

## ログしたい（``user_log_dir``）

```python
platformdirs.user_log_dir("パッケージ名")
# '~/Library/Logs/パッケージ名'

platformdirs.user_log_path("パッケージ名")
# PosixPath('~/Library/Logs/パッケージ名')
```

アプリケーションのログは、カレントディレクトリではなく、
ユーザーやシステムが探しやすい適切な場所に保存するのがよいとされています。

## リファレンス

- [platformdirs - GitHub](https://github.com/platformdirs/platformdirs)
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
