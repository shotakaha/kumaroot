# CHANGELOG.md

## v2025.12.0 (2025-12-08)

### Fix

- **mkdocs-site**: add MkDocs site, markdown, and material configuration guides
- **mkdocs-usage**: add toctree for MkDocs documentation
- **mkdocs-plugins**: add built-in plugin documentation
- **mkdocs-theme**: add comprehensive theme configuration guide
- **command-usage**: add DVC documentation to toctree
- **command-dvc**: add comprehensive DVC documentation with Google Drive support

## v2025.11.12 (2025-11-26)

### Fix

- **python-poetry**: rewrite for beginners with improved structure and clarity
- **python-poetry**: rewrite for beginners with simplified structure and examples
- **python-uv**: rewrite for beginners with improved structure and clarity
- **python-hatch**: add comprehensive hatch guide for beginners
- **python-pyproject**: expand build tools evolution and add tool adoption rationale
- **python-pyproject**: update introduction and add specification evolution
- **update-changelog-workflow**: use cz executable from commitizen
- **update-changelog-workflow**: use uvx for commitizen installation
- **command-task-git**: add git management tasks documentation
- **command-task-version**: update documentation to reflect new task namespace
- **taskfile**: add git management tasks and improve comment formatting

### Refactor

- **taskfile**: reorganize dependency management tasks with namespace grouping

## v2025.11.11 (2025-11-25)

### Feat

- **arduino**: add FreeRTOS Queue documentation
- **arduino**: add Serial data reception documentation
- **arduino**: add WiFi connection documentation with mode switching
- **arduino**: add comprehensive LittleFS documentation
- **arduino**: add JSON serialization documentation with JSONL format examples
- **arduino**: add Serial.print documentation with practical examples
- **arduino**: add Arduino usage documentation with setup and loop guides
- **root-tf1-crystalball**: add Crystal Ball function fitting documentation
- **root-tf1-pol**: add polynomial fitting documentation with TGraphErrors examples
- **root-tf1-draw**: add TF1::Draw documentation
- **root-tf1-derivative**: add TF1::Derivative documentation
- **root-tf1-integral**: add TF1::Integral documentation
- **root-tf1-getchisquare**: add TF1::GetChiSquare documentation
- **root-tf1-getparameter**: add TF1::GetParameter documentation
- **root-tf1-fixparameter**: add TF1::FixParameter documentation
- **root-tf1-setparameter**: add TF1::SetParameter documentation
- **root-ttree-entry**: add TTree::GetEntry documentation

### Fix

- **arduino**: add millis timing documentation and improve loop documentation
- **arduino**: add millis timing documentation and improve loop documentation
- **arduino**: improve Queue documentation with detailed explanations
- **python-jupytext**: add format and metadata filter documentation
- **root-ttree-entry**: improve documentation clarity and organization
- **root-tf1**: reorganize TF1 documentation and update toctree
- **root-tf1-gaus**: correct Gaussian function formula
- **root-usage**: add newly reorganized ROOT documentation files to toctree
- **root-th1-draw**: restructure documentation following root-th1-fill pattern
- **root-th1-fit**: restructure documentation following root-th1-fill pattern
- **root-tf1-gaus**: restructure documentation following root-th1-fill pattern
- **root-tf1**: create comprehensive TF1 documentation with JTF style corrections
- **root-notebook,root-ttree-entries,root-usage**: update package names and references
- **root-rntuple**: restructure documentation with practical examples
- **root-ttree-write**: restructure documentation following root-th1-fill pattern
- **root-ttree-branch**: restructure documentation following root-th1-fill pattern
- **root-ttree-fill**: restructure documentation following root-th1-fill pattern
- **root-ttree-fill**: restructure documentation with purpose-driven subsections
- **root-notebook**: add TCanvas examples and clarify drawing in Jupyter
- **root-notebook**: restructure documentation with purpose-driven subsections
- **CLAUDE**: update subsection pattern documentation to purpose-driven format
- **root-ttree-draw**: reorganize documentation with purpose-driven subsections
- **root-usage**: restructure table of contents for better organization

### Refactor

- **arduino**: split LittleFS documentation into focused modules

## v2025.11.10 (2025-11-14)

Migrated project-wide build system to pyproject-based configuration and unified dependency management from Poetry to uv.

### Refactor

- **ci**: migrate remaining GitHub Actions workflows from poetry to uv
- **ci**: migrate GitHub Actions workflow from poetry to uv
- **readthedocs**: remove requirements.txt dependency
- **docs/Makefile**: migrate from poetry to uv
- **pre-commit**: remove poetry-check hook after uv migration
- **pyproject**: disable package discovery in setuptools
- **pyproject**: use setuptools as build backend
- **pyproject**: add hatchling wheel configuration
- **taskfile**: migrate commands from poetry to uv
- **pyproject**: migrate build system from poetry-core to hatchling

## v2025.11.9 (2025-11-14)

### Feat

- **root-th1-stats**: add SetStats method documentation for histogram statistics box display
- **root-th1-rms**: add GetRMS method documentation for histogram root mean square calculation
- **root-th1-mean**: add GetMean method documentation for histogram mean value calculation
- **root-th1-binerror**: add SetBinError method documentation for custom bin error assignment
- **root-th1-sumw2**: add comprehensive Sumw2 method documentation for weighted histogram error tracking
- **python-uproot**: add uproot documentation for reading ROOT files in Python

### Fix

- **root-notebook**: add virtual environment setup instructions
- **root-notebook**: enhance documentation with comprehensive notebook usage guide
- **root-usage**: update tutorial section with ROOT official resources
- **root-tutorial**: remove obsolete reStructuredText tutorial files
- **root-usage**: add Cling and CINT documentation to interactive mode section
- **root-cling, root-cint**: add C++ interpreter documentation
- **root-tcanvas**: add DrawColorTable documentation
- **root-tcanvas**: add SetLogy documentation with comparison to gStyle
- **root-tcanvas**: add Draw documentation and reorganize canvas guide
- **root-tcanvas**: add Update documentation and reorganize canvas guide
- **root-tcanvas**: create TCanvas::Print documentation
- **root**: reorganize canvas documentation structure
- **root-tcanvas**: reorganize SaveAs documentation into separate file
- **root-tcanvas**: reorganize canvas documentation
- **root-tcanvas**: add section explaining why 'new' should be used for canvas creation
- **root-tcanvas**: add note about automatic canvas generation
- **root-tcanvas**: organize and expand Canvas documentation following CLAUDE.md format
- **root-tgraph**: reorganize and split graph documentation
- **root-th2**: organize 2D histogram documentation following CLAUDE.md standards
- **root-usage**: reorganize histogram and graph documentation structure
- **root-rdataframe**: improve examples and add csv loading reference
- **root-tfile**: move method signature section to follow opening code examples
- **root-tfile**: reorganize TFile documentation with comprehensive examples
- **root-rdataframe-csv**: add comprehensive CSV loading documentation
- **root-hist**: add integral and scale documentation to index
- **root-th1-scale**: add comprehensive normalization documentation
- **root-th1-integral**: add comprehensive integral documentation
- **root-th1-mean**: reorganize documentation with comprehensive examples
- **root-hist, root-th1**: update documentation with cross-references to new statistical methods
- **CLAUDE**: establish concise ROOT method documentation style as basic reference
- **root-th1-fill**: add comprehensive Fill method documentation
- **root-th1-title**: reorganize with comprehensive style guidelines
- **root-th1**: add error management section explaining weights vs errors
- **root-th1**: add explanation of when and why to use weights in Fill method
- **root-th1**: add concise explanation for weight parameter in Fill method
- **root-th1**: add constructor signatures and detailed parameter documentation
- **root-th1**: reorganize TH1 documentation with comprehensive style guidelines
- **root-tstring**: enhance TString documentation with benefits and C++ std::string comparison
- **root-tstring**: reorganize TString documentation with style guidelines
- **root-ttree**: simplify TTree creation documentation focused on new TTree constructor
- **root-history**: organize ROOT development history from PAW through modern features including TTree as core design and RDataFrame evolution
- **root-ttree-entries**: reorganize TTree entry counting documentation with comprehensive examples and practical use cases
- **root-ttree-readfile**: reorganize text file to TTree conversion documentation with comprehensive examples and practical use cases

### Refactor

- **CHANGELOG**: split changelog by release year for better maintainability

## v2025.11.8 (2025-11-14)

### Feat

- **root-rdataframe**: split histogram visualization into separate documentation
- **root-rdataframe**: split statistics computation into separate documentation
- **root-rdataframe**: split filtering into separate documentation

### Fix

- **root-rootrc**: reorganize ROOT user configuration documentation with .rootrc and rootlogon.C examples
- **root-groot-setstyle**: reorganize graphics style documentation with style comparison table and practical examples
- **root-gstyle-font**: add warning admonition for CJK font limitations
- **root-gstyle-font**: reorganize font configuration documentation with precision and font family examples
- **root-gstyle-canvas**: reorganize canvas configuration documentation with size and position examples
- **root-gstyle-settimedisplay**: reorganize time display documentation with epoch explanation and practical examples
- **root-gstyle-setpadgrid**: reorganize grid line documentation with practical examples and customization options
- **root-gstyle-setoptlog**: reorganize logarithmic scale documentation with practical examples and use cases
- **root-gstyle-setoptstat**: reorganize statistics display documentation with comprehensive bit structure and practical examples
- **root-gstyle-setoptfit**: reorganize fit result display documentation with detailed bit structure and practical examples
- **root-gstyle-setndivisions**: reorganize axis division documentation with detailed parameter explanations and practical examples
- **root-gstyle-sethistlinewidth**: reorganize histogram styling documentation with comprehensive parameter documentation and practical examples
- **root-groot-setrgb**: reorganize and add recommended color palettes
- **root-rdataframe**: add headers, restructure, and explain TChain relationship
- **docker**: auto-format by pre-commit hooks
- **docker-example-nginx**: improve documentation for beginners and add version information
- **docker-example-httpd**: improve documentation for beginners and add version information
- **CLAUDE**: add custom versioning scheme documentation
- **CLAUDE**: improve formatting and update commit type conventions
- **CLAUDE**: add CLAUDE.md developer guidance file
- **docker**: add AlmaLinux and RockyLinux to toctree
- **docker-example-busybox**: add characteristics section
- **docker-example-raspi**: add emulation characteristics section
- **docker-example-rockylinux**: add characteristics section
- **docker-example-almalinux**: add characteristics section
- **docker-ubuntu**: add characteristics section
- **docker-example-rockylinux**: add RockyLinux container documentation
- **docker-example-almalinux**: add AlmaLinux container documentation
- **command**: add GPG encryption documentation
- **typst**: improve tyler documentation by splitting local-build and local-install sections

### Refactor

- **root-rdataframe**: rename statistics documentation and expand content
- **root**: split global configuration documentation
- **docker**: update Ubuntu version information with latest releases
- **docker-example**: reorganize example files with docker-example- prefix

## v2025.11.7 (2025-11-12)

### Feat

- **raspi-config**: create comprehensive reverse lookup reference documentation

### Fix

- **python-venv**: update tool comparison with recommendation levels
- **python-venv**: improve for beginners and add system vs venv explanation
- **python-pyserial**: add more configuration options and troubleshooting tips
- **python-pyserial**: add beginner-friendly note about serial communication options
- **python-pyserial**: fix continuous reading section syntax and improve explanation
- **python-pyserial**: remove corrupted section added by linter
- **sphinx-latex-lualatex**: add luatex packages and hyperref settings
- **python-commitizen**: reorganize for beginners with detailed bump options
- **docs/Makefile**: correct sphinx-autobuild ignore option syntax
- **docs/Makefile**: add poetry integration for sphinx-build
- **command-mkcert**: restructure with reverse lookup style and Docker integration
- **docker-wordpress-bitnami**: split Bitnami WordPress configuration into separate document
- **docker-wordpress**: add Bitnami image examples and comparison guide
- **docker-wordpress**: restructure with compose-first approach and reverse lookup style
- **docker-mariadb**: add environment variables and adminer configuration
- **docker-postgresql**: reorganize structure and add Adminer with env variables
- **docker-mariadb**: reorganize structure and add Adminer with env variables
- **docker-nginx**: reorganize structure and update to Compose format
- **raspi-date**: add NTP synchronization note and improve documentation
- **raspi-packages**: update Python environment setup to include pipx and uv
- **raspi-python**: focus on uv tool install for ruff and pre-commit
- **raspi-capslock**: restructure as reverse lookup reference with improved documentation
- **raspi-usage**: reorganize table of contents with new configuration files
- **raspi-packages**: restructure as reverse lookup reference with expanded documentation
- **raspi-ssh**: restructure to prioritize CLI setup and improve organization
- **raspi-vnc**: restructure VNC client setup and add macOS compatibility info
- **raspi-vnc**: update documentation for Raspberry Pi 4/5 with modern VNC setup

### Refactor

- **Taskfile**: simplify bump task name
- **command-usage**: reorganize items into logical categories
- **raspi**: split configuration docs into focused files

## v2025.11.6 (2025-11-09)

### Feat

- **raspi-config**: create comprehensive reverse lookup reference documentation

### Fix

- **raspi-date**: add NTP synchronization note and improve documentation
- **raspi-packages**: update Python environment setup to include pipx and uv
- **raspi-python**: focus on uv tool install for ruff and pre-commit
- **raspi-capslock**: restructure as reverse lookup reference with improved documentation
- **raspi-usage**: reorganize table of contents with new configuration files
- **raspi-packages**: restructure as reverse lookup reference with expanded documentation
- **raspi-ssh**: restructure to prioritize CLI setup and improve organization
- **raspi-vnc**: restructure VNC client setup and add macOS compatibility info
- **raspi-vnc**: update documentation for Raspberry Pi 4/5 with modern VNC setup

### Refactor

- **raspi**: split configuration docs into focused files

## v2025.11.5 (2025-11-09)

### Fix

- **docker-dockerfile-cmd**: expand documentation with comprehensive examples and best practices
- **docker-dockerfile-run**: add Python + venv environment setup example
- **docker-dockerfile-run**: expand documentation with comprehensive examples
- **docker-dockerfile-copy**: clarify .dockerignore placement in build context
- **docker-dockerfile-copy**: expand documentation with comprehensive examples and best practices
- **docker-dockerfile**: improve documentation with sample and reorganize toctree order
- **docker-dockerfile-shell**: improve documentation quality and completeness
- **docker-dockerfile-workdir**: improve documentation quality and completeness
- **docker-dockerfile-from**: improve documentation quality and completeness
- **docker-compose.md**: reorder commands by usage frequency and add introduction
- **docker-compose-run.md**: expand documentation with practical examples
- **docker-compose-ps.md**: restructure and expand documentation
- **docker-compose-ls.md**: improve documentation clarity
- **docker-compose-logs.md**: improve clarity and documentation
- **docker-compose-cp.md**: improve clarity and documentation
- **docker-compose-exec.md**: improve clarity and documentation
- **docker-compose-down.md**: improve clarity and documentation
- **docker-compose-up.md**: improve clarity and documentation
- **docker-compose-yaml.md**: improve clarity with version key note and workflow
- **docker-compose-yaml.md**: reorganize introduction for clarity

### Refactor

- **docker**: split ls and inspect commands into separate files

## v2025.11.4 (2025-11-09)

### Fix

- **pandas-usage.md**: correct toctree reference
- **conf.py**: add unicode-math package for LuaLaTeX \mathscr support

### Refactor

- **conf.py**: improve configuration organization

## v2025.11.3 (2025-11-09)

### Feat

- **Taskfile.yml**: add pre-commit task

### Fix

- **README.md**: Correct typos and URLs

### Refactor

- **README.md**: Improve virtual environment activation instructions

## v2025.11.2 (2025-11-09)

### Refactor

- **Taskfile.yml**: Rename livehtml task to docs

## v2025.11.1 (2025-11-09)

### Feat

- **Taskfile.yml**: Add incremental changelog generation task

## v2025.11.0 (2025-11-09)

### Feat

- Switch to calendar-based versioning (YYYY.MM.PATCH)
- **Taskfile.yml**: Add cz bump commands for patch and minor versions

### Fix

- **python/python-platformdirs.md**: platformdirsを追記した
- **command/command-wget.md**: wgetを追記した
- **command/command-curl.md**: curlの使い方を整理した
- **python/python-ruff.md**: ruffの設定を追記した
- **command/command-ansible.md**: ansibleを追加した
- **typst/typst-with.md**: テンプレートの使い方を追加した
- **python/python-esptool.md**: esptoolを追加した
- **python/python-pytest.md**: マーカーなどを追加した

## v2.0.0 (2025-10-26)

ひさびさにbumpしたらv2になってしまいました

### Feat

- **command/specify**: specify（スペック駆動開発）を追加した
- **numpy/numpy-ndarray.md**: NumPyを追加した
- **python/python-pyserial.md**: PySerialの使い方を追加した

### Fix

- **command/command-lmstudio.md**: LM Studioを追加した
- **command/command-ollama.md**: Ollamaを追加した
- **command/command-claude.md**: Claude Codeを追加した
- **command/command-claude.md**: vimモード切り替えを追加した
- **command/command-cmake.md**: CMakeを追加した
- **command/command-glab.md**: glabを追加した
- **command/command-screen.md**: screenを追加した
- **command/command-task.md**: タスクのサンプルを追加した
- **command/command-zed.md**: Zedを追加した
- **docker**: MariaDBの使い方を更新した
- **docker**: サブコマンドの使い方を更新した
- **gas/gas-drive.md**: DriveAppを追記した
- **gas/gas-exports.md**: エクスポートを追加した
- **gas/gas-groups.md**: グループの使い方を追記した
- **gas/gas-trigger.md**: トリガー設定を追記した
- **gas/js-biome.md**: biomeを追加した
- **gas/ts-tsc.md**: tscを追加した
- **gas/ts-typedoc.md**: TypeDocを追加した
- **geant4-sensor-allocator.md**: G4Allocatorを整理した
- **geant4/geant4-cpp-geant4.md**: Geant4のコーディング規約を整理した
- **geant4/geant4-errors.md**: エラーの対処方法を追加した
- **geant4/geant4-event.md**: イベント情報を追記した
- **geant4/geant4-geometry.md**: ジオメトリの設定を追記した
- **geant4/geant4-install-cmake.md**: インストール手順を修正した
- **geant4/geant4-install-taskfile.md**: タスクを整理した
- **geant4/geant4-install.md**: Geant4のインストール手順を改訂した
- **geant4/geant4-material-plastic-scintillator.md**: プラシンのサンプルを改良した
- **geant4/geant4-physics-opticalphysics.md**: 光学物理の設定を整理した
- **geant4/geant4-scoring-accumulable.md**: G4Accumlableを追記した
- **geant4/geant4-singleton.md**: シングルトンパターンを追加した
- **geant4/geant4-user-actioninitialization.md**: ユーザーアクションの設定を整理した
- **geant4/geant4-user-physicslist.md**: 物理モデルを整理した
- **geant4/geant4-versions.md**: バージョン情報を整理した
- **git/git-fork.md**: フォーク開発のワークフローを追記した
- **hvplot/hvplot-options.md**: hvplotのオプション設定を追記した
- **hvplot/hvplot-scatter.md**: hvplotの散布図を追記した
- **jupytext**: JupyTextを修正した
- **notebooks/python-histogram.ipynb**: Pythonでヒストグラムを作成する方法を比較した
- **numpy/numpy-arange.md**: np.arangeを追加した
- **numpy/numpy-column_stack.md**: column_stackを追加した
- **numpy/numpy-linspace.md**: np.linspaceを追加した
- **numpy/numpy-usage.md**: numpyの位置付けを追記した
- **opencode**: OpenCodeを追加した
- **pandas**: Pandasの使い方の分類を整理した
- **pandas/pandas-groupby.md**: groupbyを整理した
- **pandas/pandas-lmfit.md**: lmfitを追加した
- **pytest**: テスト用のディレクトリ構造を整理した
- **python/python-mypy.md**: mypyの使い方を追記した
- **python/python-pip.md**: パッケージ管理ツール選択フローチャートを追加した
- **python/python-pydantic.md**: 設定ファイルを管理するクラスの手順を追記した
- **python/python-pyright.md**: pyrightを追記した
- **python/python-pyserial.md**: ファイルに保存する方法を追記した
- **python/python-pyserial.md**: 複数デバイスのシリアル通信を追加した
- **python/python-pyserial.md**: 複数デバイス処理を追記した
- **python/python-pytest.md**: pytestを追記した
- **python/python-ruff.md**: ruffを追記した
- **python/python-typing.md**: typingを追記した
- **python/python-uv.md**: uvを追記した
- **python/python-venv.md**: venvを追加した
- **python/python-virtualenv.md**: virtualenvを削除した
- **raspi/raspi-python.md**: Python環境のセットアップを追加した
- **raspi/raspi-usage.md**: GoとNode環境のセットアップを追加した
- **specify**: SpecKitの使い方を追記した
- **task**: added poetry export task
- **task**: updated Taskfile
- **task**: タスク（code）を修正した
- **tyler**: Tylerの使い方を確認した
- **typst**: page設定を追記した
- **typst**: raw要素を追記した
- **typst**: showの使い方を整理した
- **typst**: stateを追加した
- **typst**: tylerの使い方を追加した
- **typst**: Typstの使い方を更新した
- **typst**: ブロック要素とインライン要素を追加した
- **typst**: 色の設定を追加した
- **typst**: 関連ツール（typstyleとtinymist）を追加した
- **typst/typst-page.md**: ページ設定を追記した
- **typst/typst-set.md**: Typstの使い方を追記した
- **wp-cli**: wp-cliを追加した

## v1.44.3 (2025-04-15)

### Fix

- **.gitignore**: ignored vscode 設定
- **.mise.toml**: miseを削除した
- **command/command-1password.md**: opコマンドを追記した
- **command/command-awk.md**: 空白とカンマ区切りできるようにした
- **command/command-jq.md**: よく使われるワンライナーを追記した
- **command/command-vim.md**: vimのキーバインドを追加した
- **docker/docker-cli.md**: 新旧コマンド対応表を追加した
- **docker/docker-compose-down.md**: upとdownを分割した
- **docker/docker-compose-exec.md**: compose execの例を追記した
- **docker/docker-compose-run.md**: compose runを追記した
- **docker/docker-compose-up-down.md**: downのオプションを追記した
- **docker/docker-compose-up.md**: stopとstartをまとめた
- **docker/docker-compose-up.md**: 設定ファイルを変更できることを追記した
- **docker/docker-compose-yaml.md**: ボリューム設定を追加した
- **docker/docker-mariadb.md**: MariaDBを整理した
- **docker/docker-texlive.md**: TeX LiveのDocker composeを追記した
- **docker/docker-usage.md**: Dockerの使い方の導入を修正した
- **docs/source/python/python-pre-commit.md**: pre-commitで設定できるフックの種類を追記した
- **gas/gas-spreadsheet-book.md**: ブック操作を追記した
- **gas/gas-spreadsheet-range.md**: range操作を追加した
- **gas/gas-spreadsheet-sheet.md**: シート操作を修正した
- **gas/gas-spreadsheet.md**: spreadsheetを修正した
- **gas/js-jest.md**: jestを追加した
- **geant4/geant4-install-brew.md**: WSL2でのインストールを追加した
- **geant4/geant4-install-download.md**: ダウンロードリンクを修正した
- **git/git-branch.md**: ブランチ名を整理した
- **git/git-config.md**: リポジトリ設定を整理した
- **git/git-ignore.md**: gitignoredを整理した
- **git/git-local.md**: 目次を整理した
- **git/git-review.md**: レビューの手順を整理した
- **git/git-setup.md**: 目次を整理した
- **git/git-worktree.md**: worktreeを追記した
- **hugo/hugo-setup.md**: 目次を整理した
- **python/python-coverage.md**: coverageを追加した
- **python/python-pip.md**: pip/pipxを追記した
- **python/python-pydantic.md**: 再代入時のバリデーションを追記した
- **python/python-pyproject.md**: キャレットが使えなくなったことを追記した
- **python/python-uv.md**: uvを追加した
- **sphinx/sphinx-html-css.md**: CSSのレイヤー機能を追加した

## v1.44.2 (2025-03-03)

### Fix

- **docker/docker-container-run.md**: docker container runを修正した
- **docker/docker-dockerfile-copy.md**: COPYを追記した
- **docker/docker-dockerfile-from.md**: マルチステージビルドを追記した
- **docker/docker-dockerfile-run.md**: RUNコマンドを追記した
- **docker/docker-dockerfile-shell.md**: シェルの設定を追記した
- **docker/docker-dockerfile-workdir.md**: ディレクトリ名のサンプルを追記した
- **docker/docker-examples.md**: 目次を整理した
- **docker/docker-python3.md**: Python3イメージを追記した
- **docker/docker-setup.md**: 目次を整理した
- **docker/docker-texlive.md**: TeX LiveのDockerfileを追加した
- **docker/docker-usage.md**: 目次を整理した
- **docs/source/_static/latex/examples/main.tex**: tex-fmtした
- **latex/latex-docker.md**: DockerでTeXLiveする方法を追記した
- **latex/latex-font-family.md**: フォント要素を整理した
- **latex/latex-fonts.md**: udpmapを確認する方法を追記した
- **latex/latex-glossaries-extra.md**: glossaries-extraを追加した
- **latex/latex-glossaries.md**: glossariesを追加した
- **latex/latex-imakeidx.md**: imakeidxを追加した
- **latex/latex-makeglossaries.md**: makeglossariesを追加した
- **latex/latex-makeidx.md**: makeidxに修正した
- **latex/latex-makeindex.md**: makeindexを追加した
- **latex/latex-masterthesis.md**: 全体を修正した
- **latex/latex-siunitx.md**: S列を追加した
- **latex/latex-tex-fmt.md**: tex-fmtを追加した
- **latex/latex-usefont.md**: エンコーディングを表に整理した
- **pyproject.toml**: PEP621準拠に修正した
- **pyproject.toml**: poetry-plugin-exportを追加した
- **python/python-pyproject.md**: pyprojectを整理した
- **root/root-config.md**: 設定確認を追記した
- **root/root-genv.md**: gEnvを追加した
- **root/root-notebook.md**: ROOT Notebookを追加した
- **root/root-rdataframe.md**: RDataFrameを追加した
- **root/root-rint.md**: Rintを整理した
- **root/root-rntuple.md**: RNTupleを追加した
- **root/root-th1-title.md**: タイトルの設定方法を別ページに整理した
- **root/root-th1.md**: TH1を整理した
- **root/root-th1.md**: タイトルを変更する方法を追加した
- **root/root-th1.md**: 平均値、RMSを取得する方法を追記した
- **root/root-th1.md**: 統計ボックスを表示した
- **root/root-th1.md**: 軸タイトルの変更方法を追記した
- **root/root-th2.md**: TH2を整理した
- **vscode/vscode-devcontainer.md**: devcontainerを追加した

## v1.44.1 (2025-02-10)

LaTeX強化リリース

### Fix

- **.gitignore**: LaTeX関係の補助ファイルを除外した
- **docs/source/_static/latex/beamer/main.tex**: beamerのサンプルを更新した
- **docs/source/_static/latex/examples/latexmkrc**: latexmkの設定を変更した
- **docs/source/_static/latex/examples/main.tex**: サンプルを更新した
- **docs/source/_static/latex/poster/latexmkrc**: pvcを無効にした
- **docs/source/_static/latex/slides/main.tex**: ltjsarticleでスライドを作成するサンプルを追加した
- **docs/source/_static/latex/templates/lualatex-jlreq/main.tex**: このファイルの内容は別のファイルに移行することにした
- **geant4/geant4-sensor.md**: 目次のリンクを修正した
- **geant4/geant4-usage.md**: 目次のリンクを修正した
- **git/git-usage.md**: git-cliffを追加した
- **latex/beamer/main.tex**: 確認済みの内容はバックアップに移動した
- **latex/examples/latexmkrc**: LaTeXのサンプルの設定を修正した
- **latex/latex-amsmath.md**: 同位体コマンドを追記した
- **latex/latex-amsmath.md**: 数式の使い方を整理した
- **latex/latex-beamer.md**: beamerの使い方を追加した
- **latex/latex-beamer.md**: モード設定を追記した
- **latex/latex-booktabs.md**: booktabsを整理した
- **latex/latex-changes.md**: changesを追加した
- **latex/latex-changes.md**: 色の変更を追加した
- **latex/latex-documentclass-beamer.md**: パスを整理した
- **latex/latex-draftwatermark.md**: draftwatermarkを追加した
- **latex/latex-fncychap.md**: fncychapを整理した
- **latex/latex-font-family.md**: 数式フォントの操作も追記した
- **latex/latex-font-series.md**: シリーズを整理した
- **latex/latex-fonts.md**: フォント設定の目次を整理した
- **latex/latex-fontsetup.md**: fontsetupを追加した
- **latex/latex-fontspec.md**: フォント設定の参考を追加した
- **latex/latex-geometry.md**: スライドサイズの設定を追記した
- **latex/latex-japanese.md**: 日本語LaTeXについて追記した
- **latex/latex-kanji.md**: AdobeJapan1を追記した
- **latex/latex-latexdiff.md**: latexdiffを追加した
- **latex/latex-latexpand.md**: latexpandを追加した
- **latex/latex-lmodern.md**: LatinModernを追記した
- **latex/latex-ltjsclasses.md**: englishオプションを追加した
- **latex/latex-luatexja-fontspec.md**: luatexja-fontspecを整理した
- **latex/latex-luatexja-otf.md**: luatexja-otfとotfの内容をまとめた
- **latex/latex-luatexja-preset.md**: luatexja-presetを整理した
- **latex/latex-luatexja-ruby.md**: latexja-rubyを整理した
- **latex/latex-luatexja.md**: luatexjaを整理した
- **latex/latex-markdown.md**: hybridオプションに関する警告を追記した
- **latex/latex-minted.md**: 背景色のサンプルコードを変更した
- **latex/latex-misc.md**: 雑談を整理した
- **latex/latex-needstexformat.md**: NeedsTeXFormatを追加した
- **latex/latex-newcommand.md**: NewDocumentCommandを追加した
- **latex/latex-otf.md**: 削除した
- **latex/latex-package.md**: パッケージを作成するためのセクションを作成した
- **latex/latex-polyglossia.md**: 方言の設定を追記した
- **latex/latex-requirepackage.md**: バージョン指定を追記した
- **latex/latex-section.md**: 見出しの使い方を整理した
- **latex/latex-table.md**: 図表の使い方を整理した
- **latex/latex-tabularray.md**: tabularrayのサンプルを追加した
- **latex/latex-tcolorbox.md**: tcolorboxを追加した
- **latex/latex-titlepage.md**: 表紙のパターンを追加した
- **latex/latex-titlesec.md**: 標準タイトルの設定を追加した
- **latex/latex-tlmgr.md**: tlmgrを更新した
- **latex/latex-unicode-math.md**: unicode-mathを追加した
- **latex/latex-usage.md**: 目次を整理した
- **latex/latex-usefont.md**: フォント要素の簡単な説明を追加した
- **latex/latex-xcolor.md**: pagecolorを追加した
- **latex/latex-xcolor.md**: 使うとよさそうな色名を追記した
- **latex/latex-xcolor.md**: 透過度を追記した

## v1.44.0 (2025-01-27)

LaTeX 強化リリース

### Feat

- **command/command-fc-list.md**: fc-listを追加した
- **command/command-openssl.md**: OpenSSLを追加した

### Fix

- **command/command-openssl.md**: CSR生成のコマンドを追記した
- **command/command-openssl.md**: 暗号化アルゴリズムを追記した
- **command/command-openssl.md**: 自己署名証明書の作成手順を追記した
- **conf.py**: copyright year を更新した
- **docs/source/conf.py**: luatexjaパッケージを追加した
- **latex-documentclass-twocolumn.md**: 2段組を整理した
- **latex/fonts**: フォント設定の構成を整理した
- **latex/latex-bib.md**: bibファイルの作り方を追記した
- **latex/latex-biblatex.md**: biblatexの使い方を整理した
- **latex/latex-bibliography.md**: thebibliographyの使い方を整理した
- **latex/latex-bibtex.md**: bibtexを追加した
- **latex/latex-bibunsho.md**: LaTeX美文書を追加した
- **latex/latex-booktabs.md**: booktabsを整理しました
- **latex/latex-caption.md**: captionを追記した
- **latex/latex-chktex.md**: chktexを追加した
- **latex/latex-classes.md**: 欧文クラスを追加した
- **latex/latex-cleveref.md**: cleverefを追加した
- **latex/latex-detex.md**: detexを追加した
- **latex/latex-documentclass-options.md**: クラスオプションを別ページにした
- **latex/latex-documentclass-tate.md**: 見出しを修正した
- **latex/latex-documentclass-twoside.md**: 両面印刷を追加した
- **latex/latex-documentclass.md**: ドキュメントクラスを整理した
- **latex/latex-documentclass.md**: 和文クラスの説明を整理した
- **latex/latex-documentclass.md**: 早見表を追加した
- **latex/latex-feynman.md**: ファインマン図を追加した
- **latex/latex-font-dotgothic16.md**: ドット文字の設定を追加した
- **latex/latex-font-family**: 書体の特徴を追加した
- **latex/latex-font-hiragino.md**: ヒラギノを追加した
- **latex/latex-font-kiwi-maru.md**: KiwiMaruを追加した
- **latex/latex-font-zen-maru-gothic.md**: Zen丸ゴシックを追加した
- **latex/latex-fonts.md**: フォント設定を整理した
- **latex/latex-geometry.md**: geometryの設定を追記した
- **latex/latex-group.md**: ローカルスコープを追加した
- **latex/latex-heading.md**: 見出し用のコマンドを整理した
- **latex/latex-history.md**: TeXの系譜を整理した
- **latex/latex-hyperref.md**: hyperrefを整理した
- **latex/latex-install.md**: MacTeXのインストールを整理した
- **latex/latex-jlreq.md**: jlreqのオプションを確認中
- **latex/latex-kanji-config-udpmap-sys.md**: いまは不要なことを明記した
- **latex/latex-kpsewhich.md**: kpsewhichを追加した
- **latex/latex-latexmk.md**: latexmkを追記した
- **latex/latex-link.md**: 参照系の項目を整理した
- **latex/latex-list.md**: 箇条書きの環境を整理した
- **latex/latex-lualatex.md**: biberを追加した
- **latex/latex-lualatex.md**: lualatexの使い方を整理した
- **latex/latex-maketitle.md**: 表紙の設定を整理した
- **latex/latex-markdown.md**: markdownパッケージを追加した
- **latex/latex-masterthesis.md**: 修論の書き方を整理した
- **latex/latex-minted.md**: mintedの使い方を整理した
- **latex/latex-misc.md**: 雑談スペースを作成した
- **latex/latex-newcommand.md**: codeコマンドを追加した
- **latex/latex-online.md**: Zoteroの使い方を追記した
- **latex/latex-page.md**: ページ設定の目次を整理した
- **latex/latex-par.md**: テキスト編集の目次を整理した
- **latex/latex-preamble.md**: 目次を整理した
- **latex/latex-providespackage.md**: パッケージかする手順を追加した
- **latex/latex-ref.md**: 相互参照を整理した
- **latex/latex-setlength.md**: 長さ指定を追記した
- **latex/latex-setup.md**: 目次を整理した
- **latex/latex-siunitx.md**: siunitxのコマンドを整理した
- **latex/latex-subcaption.md**: subcaptionを追加した
- **latex/latex-texdoc.md**: texdocを追加した
- **latex/latex-tikz-feynman.md**: tikz-feynmanを追記した
- **latex/latex-titlepage.md**: titlepageを追加した
- **latex/latex-tlmgr.md**: tlmgrを別ページにした
- **latex/latex-uplatex.md**: uplatexの使い方を整理した
- **latex/latex-usage.md**: 目次を整理した
- **latex/latex-xcolor.md**: カラーパレットを追加した
- **pandas/pandas-fit-curve_fit.md**: pmatrixの誤記を修正した
- **python/python-poetry.md**: poetry shell -> poetry env activate への移行が必要
- **sphinx/sphinx-autobuild.md**: autobuildの設定を整理した
- **sphinx/sphinx-latex-docclass.md**: ドキュメントクラスを整理した
- **sphinx/sphinx-latex-engine.md**: lualatexをオススメした

## v1.43.1 (2025-01-05)

### Fix

- **command/command-softwareupdate.md**: softwareupdateを追加した
- **command/command-xcode.md**: Command Line Toolsのインストールを追記した
- **docs/source/gas/gas-spreadsheet-pivottable.md**: ヒストグラムを追記した
- **gas/gas-namespace.md**: 名前空間を追記した
- **gas/gas-properties.md**: PropertiesServiceを追加した
- **gas/gas-spreadsheet-chart.md**: グラフの作り方を追加した
- **gas/gas-spreadsheet-pivottable.md**: ピボットテーブル操作を追記した
- **gas/gas-spreadsheet-range.md**: 範囲選択を整理した
- **gas/js-function.md**: 関数宣言を整理した
- **gas/js-map.md**: Map型の操作を追記した
- **geant4/geant4-scoring-accumulable.md**: G4AccValueに変更されたことを追記した
- **geant4/geant4-versions.md**: CMakeのミニマムバージョンを追記した
- **geant4/geant4-versions.md**: Geant4 11.3.0 がリリースされた
- **latex/latex-luatexja-otf.md**: latexja-otfを追記した
- **latex/latex-luatexja-ruby.md**: ルビの振り方を追記した
- **latex/latex-luatexja.md**: 和文フォントを追記した
- **latex/latex-minipage.md**: minipage環境を追加した
- **latex/latex-pmatrix.md**: 行列の追加した
- **latex/latex-showframe.md**: showframeパッケージを追加した
- **latex/latex-usepackage-geometry.md**: geometryパッケージを整理した
- **notebooks/scipy-interpolate.ipynb**: 補間の使い方を確認中
- **pandas/pandas-interpolate-spline.md**: スプライン補間を追加した
- **python/python-uv.md**: upgrade --all を追記した
- **scripts/pexpect.py**: 更新した
