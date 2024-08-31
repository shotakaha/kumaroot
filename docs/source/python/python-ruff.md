# フォーマッター／リンターしたい（``ruff``）

```console
$ pipx install ruff
```

Rustで書かれたPython用のリンター&フォーマッタです。
これまで``black``、``isort``、``flake8``を組み合わせてできたことを``ruff``に集約できます。
設定を``pyproject.toml``に記述できるため、既存のPythonプロジェクトにも導入しやすいと思います。

:::{note}

Pythonのリンター＆フォーマッタの変遷は闇が深そうです。
時代とともにベストプラクティスが移り変わっている感じで、
これを使っておけばOKみたいな標準的なモジュールが存在しません。

数年前に「設定不要のフォーマッタ」を謳った``black``が登場しました。
インストールしてそのまま使えるため、逆に導入しやすいと感じました。

リンターは``flake8``を使ってみようと思ったのですが、たしか``pyproject.toml``に対応しておらず断念。
型チェッカーに``mypy``を使ってみようと思ったのですが、そもそも型アノテーションをうまく設定できておらず、こちらも断念しました。

``ruff``の基本コマンドは簡単なので、今度こそ身につけられるのではと期待しています。

:::

## リンターしたい（``ruff check``）

```console
$ ruff check
$ ruff check --fix
$ ruff check --show-fixes
$ ruff check ファイル名
$ ruff check ファイル名 --select カテゴリ記号
```

``check``コマンドでリンターを実行します。
引数にファイル名を指定したり、確認したいディレクトリで``ruff check .``を指定したりできます。
``--select``オプションを使って、チェックしたいカテゴリーやエラー番号などを指定できます。

修正箇所はターミナルに出力されます。
ファイル内容は変更されないので、とりあえず``--select ALL``でチェックして、
どのリンターを有効にするといいか検討してみるといいと思います。

```console
$ ruff check . --select ALL
```

## フォーマッタしたい（``ruff format``）

```console
$ ruff format
$ ruff format --check
$ ruff format --diff
$ ruff format ファイル名
```

``format``コマンドでフォーマッターとして利用できます。
引数にファイル名を指定したり、確認したいディレクトリで``ruff format .``を指定して実行します。

## ルールを確認したい（``ruff rule``）

```console
$ ruff rule ルールID
```



``select``や``ignore``で設定できるカテゴリ記号は[公式ドキュメントの「ルール」](https://docs.astral.sh/ruff/rules/)に書いてあります。
どんなものがあるかなと思って書き写してみたら、なんと58種類もありました。

1. ``E``, ``W``: ``pycodestyle``
2. ``F``: ``Pyflakes``
3. ``C90``: ``mccabe``
4. ``I``: ``isort``
5. ``N``: ``pep8-naming``
6. ``D``: ``pydocstyle``
7. ``UP``: ``pyupgrade``
8. ``YTT``: ``flake8-2020``
9. ``ANN``: ``flake8-annotations``
10. ``ASYNC``: ``flake8-async``
11. ``TRIO``: ``flake8-trio``
12. ``S``: ``flake8-bandit``
13. ``BLE``: ``flake8-blind-except``
14. ``FBT``: ``flake8-boolean-tra``
15. ``B``: ``flake8-bugbear``
16. ``A``: ``flake8-builtins``
17. ``COM``: ``flake8-commas``
18. ``CPY``: ``flake8-copyright``
19. ``C4``: ``flake8-comprehensions``
20. ``DTZ``: ``flake8-datetimez``
21. ``T10``: ``flake8-debugger``
22. ``DJ``: ``flake8-django``
23. ``EM``: ``flake8-errmsg``
24. ``EXE``: ``flake8-executable``
25. ``FA``: ``flake8-future-annotations``
26. ``ISC``: ``flake8-implicit-str-concat``
27. ``ICN``: ``flake8-import-conventions``
28. ``G``: ``flake8-logging-format``
29. ``INP``: ``flake8-no-pep420``
30. ``PIE``: ``flake8-pie``
31. ``T20``: ``flake8-print``
32. ``PYI``: ``flake8-pyi``
33. ``PT``: ``flake8-pytest-style``
34. ``Q``: ``flake8-quotes``
35. ``RSE``: ``flake8-raise``
36. ``RET``: ``flake8-return``
37. ``SLF``: ``flake8-self``
38. ``SLT``: ``flake8-slots``
39. ``SIM``: ``flake8-simplify``
40. ``TID``: ``flake8-tidy-imports``
41. ``TCH``: ``flake8-type-checking``
42. ``INT``: ``flake8-gettext``
43. ``ARG``: ``flake8-unused-arguments``
44. ``PTH``: ``flake8-use-pathlib``
45. ``TD``: ``flake8-todos``
46. ``FIX``: ``flake8-fixme``
47. ``ERA``: ``eradicate``
48. ``PD``: ``pandas-vet``
49. ``PGH``: ``pygrep-hooks``
50. ``PL``: ``pylint``
51. ``TRY``: ``tryceratops``
52. ``FLY``: ``flynt``
53. ``NPY``: NumPy-specific rules
54. ``AIR``: ``Airflow``
55. ``PERF``: ``Perflint``
56. ``FURB``: ``refurb``
57. ``LOG``: ``flake8-logging``
58. ``RUF``: Ruff-specific rules
