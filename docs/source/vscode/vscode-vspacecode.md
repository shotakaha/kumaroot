# EmacsとVimしたい（``VSpaceCode``）

[VSpaceCode](https://vspacecode.github.io/)は、VS CodeでSpacemacsを使えるようにするプラグインです。
基本的にはEmacs操作したいけど、たまにVim操作するために慣れておきたいというひとにはもってこいだと思います。

## 画面構成の名称

| Emacs | VS Code |
|---|---|
| buffer | editor |
| window | editor group |
| frame | window |

EmacsとVS Codeでは画面構成の名称が異なります。
[Conventions](https://vspacecode.github.io/docs/conventions)に対応表が載っていました。

## よく使うキーバインド

| キーバインド | 操作内容 |
|---|---|
| {kbd}`SPC SPC` | Command Palette |
| {kbd}`Ctrl + g` / {kbd}`ESC` | Cancel |
| {kbd}`SPC g s` | Magit status |
| {kbd}`SPC f f` | Open file/folder |
| {kbd}`SPC w /` | Split window right |
| {kbd}`SPC w w` | Focus next window |
| {kbd}`SPC b b` | Show all buffers |
| {kbd}`SPC j l` | Jump to line (EASYMOTION) |

## モードを切り替えたい

Vimのように**モード**切り替えできます。

NORMALモード（{kbd}`Esc`）
: 閲覧・編集モードです。
  {kbd}`j` / {kbd}`k` / {kbd}`l` / {kbd}`h`でカーソルを操作できます。
  また、コマンドモードとも呼ばれ、各種コマンドを使って編集できます。
  {kbd}`i`や{kbd}`a`などの挿入コマンドを押すとINSERTモードに入り変わります。

INSERTモード（{kbd}`i` / {kbd}`a` / {kbd}`o` /）
: 挿入モードです。文字を入力できます。
  VSpaceCodeの場合、ここがEmacs操作の出番です。
  {kbd}`Esc`キーを押すとNORMALモードに切り替わります。

VISUALモード（{kbd}`v` / {kbd}`V`）
: 矩形選択モードです。
  範囲を選択して、コマンド操作できます。
  VSpaceCodeではあまり出番がありません。
  このモードに入ってしまったら、とりあえず{kbd}`Esc`を押してNORMALモードに切り替えます。

:::{note}
すぐに書き込めないのは不便ですが、読むモードと書くモードを切り替えるのは、いまの作業に集中するのにも役立つかなと思っています。
Emacsでも読み取りモード（{kbd}`ctr-x` + {kbd}`ctr-q`）を愛用してました。
そのときはステータスラインに色をつけて、視覚的にモードを区別できるようにしてました。
VSpaceCodeでもそれをしたい・・・が、やりかたわからない。
:::

## ユーザー設定

### ステータスバーに色をつけたい

```json
{
    "vim.statusBarColorControl": true,
}
```

``vim.statusBarColorControl``で、Vimのモードごとにステータスバーの色を表示できます。

### ステータスバーの色を変更したい

```json
{
    "vim.statusBarColorControl": true,
    // "vim.statusBarColors.モード名": ["#背景色", "#文字色"]
    "vim.statusBarColors.normal": ["#e27878", "#161821"],  // red系
    "vim.statusBarColors.insert": ["#b4be82", "#161821"],  // green系
    "vim.statusBarColors.replace": ["#e2a478", "#161821"], // orange系
    "vim.statusBarColors.visual": ["#a093c7", "#161821"],       // purple系
    "vim.statusBarColors.visualline": ["#a093c7", "#161821"],   // purple系
    "vim.statusBarColors.visualblock": ["#a093c7", "#161821"],  // purple系
    // "vim.statusBarColors.commandlineinprogress": ["#e2a478", "#161821"],
    // "vim.statusBarColors.searchinprogressmode": ["#e2a478", "#161821"],
    // "vim.statusBarColors.easymotionmode": ["#e2a478", "#161821"],  // orange系
    // "vim.statusBarColors.easymotioninputmode": ["#e2a478", "#161821"],
    // "vim.statusBarColors.surroundinputmode": ["#e2a478", "#161821"],
}
```

Vimのモードごとにステータスバーの色を変更できます。
``normal``は書き込みNGなので赤系、
``insert``は書き込みOKなので緑系、
``visual``は紫系、にしてあります。

全体に[Iceberg](https://cocopon.github.io/iceberg.vim/)テーマを使っているため、
そのパレットから色を選択しました。
