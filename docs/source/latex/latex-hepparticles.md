# 素粒子を表示したい（`hepparticles`）

```latex
\usepackage{hepparticles}  % upright（デフォルト）で表記
\usepackage[italic]{hepparticles}  % イタリックで表記
```

素粒子の記号は、upright（立体）とitalic（斜体）のどちらでも表記できます。
特定の粒子を書くときはupright、粒子の一般的な分類を書くときはitalicにするのが慣習です。
`italic`オプションを指定しない場合は、uprightで表記されます。

## 粒子したい（`\HepParticle`）

```latex
% プリアンブル
\usepackage{hepparticles}

% 本文
$\HepParticle{B}{d}{0}$
```

`\HepParticle{主記号}{下付き}{上付き}`で、特定の粒子の名前を表示できます。
下付きと上付きは、ないときは空の`{}`を指定します。

## 反粒子したい（`\HepAntiParticle`）

```latex
% 本文
$\HepAntiParticle{B}{d}{0}$
```

`\HepAntiParticle{主記号}{下付き}{上付き}`で、反粒子の名前を表示できます。
反粒子は、主記号の上にバーが付いた表記になります。

## 共鳴状態したい（`\HepParticleResonance`）

```latex
% 本文
$\HepParticleResonance{J/\psi}{1S}{}{\star}$
```

`\HepParticleResonance{名前}{質量}{質量の下付き}{質量の上付き}`で、共鳴状態の名前を表示できます。
共鳴状態は、粒子名の後ろに、かっこで囲んだ質量の情報が付きます。

## 超対称性粒子したい（`\HepSusyParticle`）

```latex
% 本文
$\HepSusyParticle{\chi}{}{}$
```

`\HepSusyParticle{主記号}{下付き}{上付き}`で、超対称性粒子の名前を表示できます。
超対称性粒子は、標準模型の粒子の表記にチルダが付いた形になります。
