# ROOTのユーザー設定をしたい（`.rootrc`）

```console
# system.rootrc のパスを確認
$ root-config --prefix
/opt/homebrew/Cellar/root/6.36.04_1

# デフォルト設定ファイルをホームディレクトリにコピー
$ cp $(root-config --prefix)/etc/root/system.rootrc ~/.rootrc

# エディタで編集
$ nano ~/.rootrc
```

`.rootrc`ファイルでROOTのユーザーグローバル設定ができます。
ホームディレクトリに配置されたファイルは、ROOTの起動時に自動的に読み込まれます。

## .rootrc 設定ファイルを理解したい

`.rootrc`はROOTのグローバル設定ファイルです。

### 設定ファイルの場所

| ファイル | 説明 | 優先度 |
|---------|------|-------|
| `~/.rootrc` | ユーザー設定（ホームディレクトリ） | 最優先 |
| `$ROOTSYS/etc/root/system.rootrc` | システム共通設定 | 次点 |
| `/etc/root/system.rootrc` | システム全体設定 | 最後 |

後から読み込まれたファイルが同じ設定キーを含む場合、その値で上書きされます。

### 設定ファイルの探し方

```console
# ROOTをインストールしたパスを確認
$ root-config --prefix
/opt/homebrew/Cellar/root/6.36.04_1

# system.rootrc の場所を検索
$ find $(root-config --prefix) -name "system.rootrc"
/opt/homebrew/Cellar/root/6.36.04_1/etc/root/system.rootrc
```

## .rootrc を設定したい

### ファイルのセットアップ

```console
# デフォルト設定をコピー
$ cp $(root-config --prefix)/etc/root/system.rootrc ~/.rootrc

# 所有者と権限を確認
$ ls -la ~/.rootrc
-rw-r--r-- 1 user user 12345 Nov 14 10:30 /home/user/.rootrc
```

既存の`system.rootrc`をコピーしてから編集するのが推奨です。
すべてのデフォルト設定を確認できます。

### 基本的な設定例

```bash
# キャンバスのデフォルトスタイル
Canvas.Style Modern

# 保存形式のデフォルト
Canvas.SaveAsDefaultType pdf

# ヒストグラムのビニング（1次元）
Hist.Binning.1D.x 100

# ヒストグラムのビニング（2次元）
Hist.Binning.2D.x 40
Hist.Binning.2D.y 40

# ヒストグラムの精度
Hist.Precision.1D float
Hist.Precision.2D float

# ROOT対話モードの履歴
Rint.History $(HOME)/.root_hist

# ROOT対話モードのウェルカムメッセージ
Rint.WelcomeLite no
```

## 実用的な設定例

### 論文作成用

```bash
# グラフィックススタイル
Canvas.Style Plain

# 保存形式
Canvas.SaveAsDefaultType pdf

# ヒストグラム設定
Hist.Binning.1D.x 100
Hist.Binning.2D.x 50
Hist.Binning.2D.y 50
Hist.Precision.1D double
Hist.Precision.2D double

# 統計情報の表示
Stat 111110
Fit 1111
```

論文投稿用には高精度の設定が推奨されます。

### プレゼンテーション用

```bash
# グラフィックススタイル（見やすい）
Canvas.Style Modern

# 大きめのデフォルトキャンバス
Canvas.DefW 1000
Canvas.DefH 750

# 保存形式
Canvas.SaveAsDefaultType png

# ヒストグラム設定
Hist.Binning.1D.x 100
Hist.Binning.2D.x 40
Hist.Binning.2D.y 40
Hist.Precision.1D float
Hist.Precision.2D float

# 統計情報非表示
Stat 0
```

スクリーン表示用には見やすさを重視した設定です。

### データ分析用

```bash
# グラフィックススタイル
Canvas.Style Plain

# キャンバスサイズ
Canvas.DefW 800
Canvas.DefH 600

# 高精度ヒストグラム
Hist.Binning.1D.x 200
Hist.Binning.2D.x 100
Hist.Binning.2D.y 100
Hist.Binning.3D.x 50
Hist.Binning.3D.y 50
Hist.Binning.3D.z 50
Hist.Precision.1D double
Hist.Precision.2D double
Hist.Precision.3D double

# 詳細な統計情報
Stat 1111111
Fit 1111111
```

詳細な解析用には高精度ビニングが有効です。

### 対話型使用

```bash
# グラフィックススタイル
Canvas.Style Modern

# 履歴ファイル
Rint.History $(HOME)/.root_hist

# ウェルカムメッセージ
Rint.WelcomeLite no

# コマンドラインエディタ
Rint.Editor nano

# プロンプト
Rint.Prompt "root [%d] "
```

ROOT対話モードでの快適性を向上させます。

## よく使う設定オプション

### Canvas（キャンバス）設定

| オプション | 説明 | 例 |
|-----------|------|-----|
| `Canvas.Style` | デフォルトスタイル | Plain, Modern, ATLAS, CMS |
| `Canvas.DefW` | デフォルト幅（ピクセル） | 700 |
| `Canvas.DefH` | デフォルト高さ（ピクセル） | 500 |
| `Canvas.DefX` | デフォルトX座標 | 10 |
| `Canvas.DefY` | デフォルトY座標 | 10 |
| `Canvas.SaveAsDefaultType` | 保存形式 | pdf, png, jpg, eps |

### Hist（ヒストグラム）設定

| オプション | 説明 | 例 |
|-----------|------|-----|
| `Hist.Binning.1D.x` | 1D ビニング数 | 100 |
| `Hist.Binning.2D.x` | 2D X ビニング数 | 40 |
| `Hist.Binning.2D.y` | 2D Y ビニング数 | 40 |
| `Hist.Binning.3D.x` | 3D X ビニング数 | 20 |
| `Hist.Precision.1D` | 1D 精度 | float, double |
| `Hist.Precision.2D` | 2D 精度 | float, double |
| `Hist.Precision.3D` | 3D 精度 | float, double |

### Rint（対話モード）設定

| オプション | 説明 | 例 |
|-----------|------|-----|
| `Rint.History` | 履歴ファイル | $(HOME)/.root_hist |
| `Rint.WelcomeLite` | ウェルカムメッセージ | yes, no |
| `Rint.Editor` | コマンドラインエディター | nano, vim, emacs |
| `Rint.Prompt` | コマンドプロンプト | "root [%d] " |

## プロジェクト単位の設定（rootlogon.C）

プロジェクトごとの設定は、ディレクトリ直下の`rootlogon.C`ファイルで管理できます。

### rootlogon.C の基本例

```cpp
// ~/.rootlogon.C
// ROOTの起動時に自動実行されるスクリプト

void rootlogon() {
  // グラフィックススタイル設定
  gROOT->SetStyle("Plain");
  gROOT->ForceStyle();

  // 統計情報表示設定
  gStyle->SetOptStat(111110);
  gStyle->SetOptFit(1111);

  // グリッドライン表示
  gStyle->SetPadGridy(1);

  // ウェルカムメッセージ
  cout << "\n=== ROOT initialized ===" << endl;
  cout << "Version: " << gROOT->GetVersion() << endl;
  cout << "==========================\n" << endl;
}
```

`rootlogon.C`はROOT起動時に自動的に実行されます。

### プロジェクト固有の設定

```cpp
// プロジェクトディレクトリ直下の rootlogon.C
void rootlogon() {
  // プロジェクト共通設定
  gROOT->SetStyle("Plain");

  // 解析用ライブラリを読み込み
  gSystem->Load("./lib/MyAnalysis.so");

  // 解析マクロディレクトリをパスに追加
  gROOT->ProcessLine(".include ./include");

  // プロジェクト固有のマクロを読み込み
  gROOT->ProcessLine(".L ./macros/Utils.C");

  cout << "Project initialized" << endl;
}
```

各プロジェクトディレクトリに`rootlogon.C`を配置することで、
そのディレクトリでROOTを起動した時のみ実行されます。

## 設定ファイルの読み込み順序

ROOTの起動時に以下の順序で設定ファイルが読み込まれます：

1. **システム設定**: `$ROOTSYS/etc/root/system.rootrc`
2. **ユーザー設定**: `~/.rootrc`（この値で上書き）
3. **対話スクリプト**: `~/.rootlogon.C`（存在する場合）
4. **プロジェクト設定**: `./rootlogon.C`（存在する場合）

後から読み込まれたファイルが同じ設定キーを含む場合は、
新しい値で上書きされます。

## 注意事項

- **ファイルフォーマット**: `.rootrc`は大文字小文字を区別します

- **構文エラー**: 構文エラーがあるとROOT起動時に警告が出ます

- **環境変数**: `$(HOME)` のように `$()` 形式で環境変数を参照できます

- **コメント**: `#`で始まる行はコメント行です

- **複数行設定**: 継続する場合は行末に`\`を付けます

- **rootlogon.C の言語**: C++ 言語で記述します

- **権限**: `.rootrc`は本人のみ読み取り可能にしてください: `chmod 600 ~/.rootrc`

## トラブルシューティング

### 設定が反映されない場合

```console
# キャッシュをクリアしてから再起動
$ rm -rf ~/.root_*
$ root
```

### 設定ファイルの構文をチェック

```console
# 利用可能な全設定オプションを確認
$ root -b -q -x 'gEnv->Print(); .q'
```

### rootlogon.C が実行されない場合

```console
# ホームディレクトリの rootlogon.C が読み込まれているか確認
$ cat ~/.rootlogon.C

# または ROOT 起動時の出力を確認
$ root -v 2>&1 | grep -i logon
```

## リファレンス

- [ROOT .rootrc Documentation](https://root.cern/doc/master/classTEnv.html)
- [ROOT rootlogon.C Guide](https://root.cern/doc/master/group__RootConfig.html)
- [ROOT Configuration Guide](https://root.cern/doc/master/group__config.html)
