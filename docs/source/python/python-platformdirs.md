# 定番ディレクトリしたい（``platformdirs``）

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

## ユーザーデータしたい（``user_data_dir``）

```python
platformdirs.user_data_dir("パッケージ名")
# '~/Library/Application Support/パッケージ名'

platformdirs.user_data_path("パッケージ名")
# PosixPath('~/Library/Application Support/パッケージ名')
```

## キャッシュデータしたい（``user_cache_dir``）

```python
platformdirs.user_cache_dir("パッケージ名")
# '~/Library/Caches/パッケージ名'

platformdirs.user_cache_path("パッケージ名")
# PosixPath('~/Library/Caches/パッケージ名')
```

## ログしたい（``user_log_dir``）

```python
platformdirs.user_log_dir("パッケージ名")
# '~/Library/Logs/パッケージ名'

platformdirs.user_log_path("パッケージ名")
# PosixPath('~/Library/Logs/パッケージ名')
```

## リファレンス

- [platformdirs - GitHub](https://github.com/platformdirs/platformdirs)
- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
