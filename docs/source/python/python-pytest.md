# ユニットテストしたい（`pytest`）

```console
$ pytest --version
pytest 9.1.1

$ pytest
$ pytest --verbose
$ pytest ファイル名
```

`pytest`はPythonのユニットテスト群をまとめて実行できるツールです。
プロジェクトのルートディレクトリで実行すればテストをまとめて実行できます。
``--verbose``オプションで、それぞれのテストごとに結果を表示できます。

## インストールしたい（`pytest`）

- `pip`でインストール

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install pytest
$ pip install pytest-mock  # モックを使ったユニットテスト
$ pip install pytest-cov   # カバレッジの計測
$ pip install pytest-html  # テスト結果をHTMLファイルに出力
```

- `pipx`でインストール

```console
$ pipx install pytest
$ pipx install pytest-mock
$ pipx install pytest-cov
$ pipx install pytest-html
```

- `uv tool`でインストール

```console
$ uv tool install pytest
$ uv tool install pytest-mock
$ uv tool install pytest-cov
$ uv tool install pytest-html
```

- `poetry`でインストール

```console
$ poetry add pytest --group test
$ poetry add pytest-mock --group test
$ poetry add pytest-cov --group test
$ poetry add pytest-html --group test
```

- `uv`でインストール

```console
$ uv add pytest --group test
$ uv add pytest-mock --group test
$ uv add pytest-cov --group test
$ uv add pytest-html --group test
```

`pipx`や`uv tool`を使ってシステム（の仮想環境）にインストールできます。
`poetry`や`uv`で管理している場合は`--group test`に分類するとよいと思います。

テスト結果をHTMLファイルに出力する場合は`pytest-html`が必要です。

[unittest.mock](./python-unittest-mock.md)を使う場合は、
`pytest-mock`もインストールしておくとよいです。
カバレッジを計測した場合は`pytest-cov`が必要です。

## マーカーしたい（`-m`）

```console
$ pytest テストのパス -m "xxx"

$ pytest テストのパス -m "slow"
$ pytest テストのパス -m "local"
```

`-m "マーカー名"`で`@pytest.mark.xxx`のデコレーターでマークしたテストだけを実行できます。

```console
$ pytest --markers

// @pytest.mark.filterwarnings(warning)
// @pytest.mark.skip(reason=None)
// @pytest.mark.skipif(condition, ..., *, reason=...)
// @pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict)
// @pytest.mark.parametrize(argnames, argvalues)
// @pytest.mark.usefixtures(fixturename1, fixturename2, ...)
```

`--markers`オプションでマーカー名を確認できます。
いくつかのマーカーはpytestにプリセットがあります。
プロジェクト固有のマーカーは`pyproject.toml`で定義できます。

```toml
[tool.pytest.ini_options]
minversion = "8.0"
testpaths = ["tests"]
markers = [
    "local: tests that should only run locally",
    "slow: tests that take more than 1 second to run"
]
addopts = [
    "-m", "not local",
]
filterwarnings = [
    "error",
    "ignore::DeprecationWarning",
]
```

`minversion`で、このプロジェクトが要求する`pytest`の最低バージョンを指定できます。
`testpaths`で、引数なしで`pytest`を実行したときに検索するディレクトリを指定できます。
`filterwarnings`で、警告（`Warning`）の扱いを設定できます。
上記の例では、想定外の警告は`error`として失敗させつつ、`DeprecationWarning`だけは無視しています。

マーカー名に`not`をつけることで除外できます。
このサンプルでは、時間のかかるテストなどに`@pytest.mark.local`とマークし、デフォルトでスキップするようにしています。

## テスト名で絞り込みたい（`-k`）

```console
$ pytest -k "download"
$ pytest -k "download and not slow"
```

`-k "式"`で、テスト関数名やクラス名の一部にマッチするテストだけを実行できます。
`and`・`or`・`not`を組み合わせた式も使えます。
`-m`（マーカー）と違い、事前にマークしておく必要がないため、手早く絞り込みたいときに便利です。

## 失敗したら止めたい（`-x` / `--maxfail`）

```console
$ pytest -x
$ pytest --maxfail=3
```

`-x`（`--exitfirst`）で、最初に失敗したテストの時点で実行を打ち切れます。
`--maxfail=数`で、指定した数だけ失敗した時点で打ち切れます。
テストが大量にある場合、全部の結果を待たずに早めに気づけるので便利です。

## 前回失敗したテストだけ実行したい（`--lf` / `--ff`）

```console
# 前回失敗したテストだけ再実行
$ pytest --lf

# 前回失敗したテストを先に、残りもすべて実行
$ pytest --ff
```

`--lf`（`--last-failed`）で、前回失敗したテストだけを再実行できます。
`--ff`（`--failed-first`）で、前回失敗したテストを先頭に並べつつ、すべてのテストを実行できます。
修正がうまくいったかをすぐに確認したいときに便利です。

## 並列実行したい（`pytest-xdist`）

```console
$ uv add pytest-xdist --group test
```

```console
$ pytest -n auto
$ pytest -n 4
```

`pytest-xdist`をインストールすると、`-n`オプションでテストを並列実行できるようになります。
`-n auto`でCPUコア数に応じて自動的に並列数を決定します。
テストの数が増えてきて実行時間が気になってきたら、導入を検討するとよいです。

## 詳細表示したい（`--verbose`）

```console
$ pytest テストのパス --verbose
```

`--verbose`オプションで、ファイル内のテスト関数を表示できます。

## トレースバックを表示したい（`--tb`）

```console
$ pytest テストのパス --tb=short    # 簡潔
$ pytest テストのパス --tb=long     # 詳細
$ pytest テストのパス --tb=none     # 非表示
```

`--tb`オプションで、トレースバックの表示形式を変更できます。

## 実行時間を確認したい（`--durations`）

```console
$ pytest テストのパス --verbose --durations=0
$ pytest テストのパス --verbose --durations=10  # TOP10件
```

`--durations`オプションで、各テストの実行時間を表示できます。


## テスト用ディレクトリ（`tests`）

```console
tests/
├── conftest.py
├── __init__.py
├── test_モジュール1.py
├── test_モジュール2.py
```

ユニットテスト用のファイルは、`tests`ディレクトリの中に作成します。
ファイル名の先頭は必ず`test_`にする必要があります。

`conftest.py`はPyTestを実行するときに読み込まれる特殊なファイルです。
どのテストでも利用するデータセットなど、再利用可能なオブジェクトは
このファイルに`fixture`として定義しておくとよいです。

## オススメのテスト構造

僕がたどりついた勝手にオススメのディレクトリ構造を紹介します。

```console
$ cd プロジェクト
$ tree
.
├── 自作パッケージ名
│   ├── __init__.py
│   ├── 自作モジュール1.py
│   ├── 自作モジュール2.py
├── tests
│   ├── conftest.py
│   ├── __init__.py
│   ├── unit/
│   │   ├── 自作モジュール名1/
│   │   │   ├── test_関数1.py    // Success / Failure / Edge
│   │   │   ├── test_関数2.py    // Success / Failure / Edge
│   │   ├── 自作モジュール2.py
│   │   │   ├── test_関数3.py
│   ├── integration/
│       ├── test_統合テスト1.py
├── poetry.toml
├── pyproject.toml
```

自作パッケージと同じ階層に`tests`ディレクトリを作成します。
その中にユニットテスト用（`unit`）と
統合テスト用（`integration`）を分けて作成します。

```console
$ uv run pytest tests/unit -v
$ uv run pytest tests/integration -v
```

ディレクトリを分けることで、
ユニットテストだけ、統合テストだけを実行できます。

:::{hint}

このディレクトリ分類は、リファクター時にとても有用だと思います。
ユニットテストだけで実行できるので、（気持ち的に）安全にリファクターを進めることができます。

:::

ユニットテストは、モジュールごとにディレクトリを作成し、
その中に関数ごとにテストファイル（`test_関数名.py`）を作成します。
テストには、成功、失敗、エッジケースに分類し、
必要なユニットテストを記述します。

:::{hint}

この分類はディレクトリの階層が深くなってしまうのがデメリットです。
ただし、テストファイルの肥大化を防ぎつつ、
網羅性を確保できるのが大きなメリットだと思います。

:::

## モックしたい

:::{note}

モック／パッチの作り方はまだわかっていないので、
ChatGPTに聞きながら書くことが多いです。

:::

```python
import pytest
from unittest.mock import patch

@patch("subprocess.run")
def test_download(mock_subprocess_run):

    """Test download method"""

    # テスト用URL
    url = TEST_SHARED_URL
    sheet = Sheet(
        url=url,
        filename="output.csv")
    sheet.download()

    mock_subprocess_run.assert_called_with(
        ["wget", "--quiet", "-O", "output.csv", sheet.export_url]
    )
```

上のサンプルは、
``sheet.download``の中で、
``subprocess.run``を使って
`wget`を呼んでいる場合のテストです。

`subprocess.run`をモックすることで、wgetを実行せずにテストできるようにしています。
テスト関数の引数名はモック名にします。
この場合は``mock_subprocess_run``でアクセスできるようになります。

wgetを実行していないため、`filename="output.csv"`に設定したファイルは作成されません。
そのため、``assert_called_with``を使って、指定した引数で関数が呼ばれたかどうかで、動作確認しています。



## ファイル書き込みをモックしたい（`pathlib.Path.write_text`）

```python
def 関数名(引数):
    p = Path("ファイル名")
    p.write_text("ファイル内容", encoding="utf-8")
```

`pathlib.Path.write_text`を使っている関数のユニットテストを作成したときのサンプルです。
関数名や引数名は適当に置き換えて読んでください。

```python
from unittest.mock import patch

@patch("pathlib.Path.write_text")
def test_関数名(mock_write):
    # test strings
    text = "ファイル内容"

    # run a function
    関数名(引数)

    # assertion
    # write_textが1回だけ呼ばれたことを確認
    mock_write.assert_called_once_with(text, encoding="utf-8")
```

`pathlib.Path.write_text`をモックします。
`write_text`は内部で`pathlib.Path.open`を使っていますが、
`mock_open`は必要ありません。

:::{note}

`open`関数を使う場合は`mock_open`が必要です。

:::

## 例外をテストしたい（`pytest.raises`）

```python
import pytest

def test_関数名():
    with pytest.raises(例外名):
        関数(...)  # <- 例外を発生させる
```

`pytest.raises`で例外をテストできます。

## 繰り返しテストしたい（`@pytest.mark.parametrize`）

```python
@pytest.mark.parametrize(
    "a, b, expected",
    [ (1, 2, 3),
      (3, 4, 5),]
)
def test_関数名(a, b, expected):
    assert 関数名(a, b) == expected
```

`@pytest.mark.parametrize`デコレータで、
異なる値で繰り返しテストできます。

## テスト用の設定したい（`@pytest.fixture`）

```python
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_data_length(sample_data):
    assert len(sample_data) == 3
```

`@pytest.fixture`でテスト用の設定値を作成できます。
