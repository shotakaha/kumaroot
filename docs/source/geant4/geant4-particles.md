# 粒子したい（``/particle/list``）

```console
Idle> /particle/list
gamma,
opticalphoton
alpha, anti_alpha
neutron, anti_neutron
proton, anti_proton,
pi+, pi-, pi0,

// レプトン
e+ e-,
mu+, mu-
tau+, tau-,

// ニュートリオ
nu_e, anti_nu_e,
nu_mu, anti_nu_mu,
nu_tau anti_nu_tau,

// 仮想粒子（たぶん）
geantino,
```

対話モードの``/particle/list``コマンドで、利用可能な粒子名の一覧を確認できます。
素粒子物理学、原子核物理学で扱う粒子・反粒子がすべて揃っています。

粒子名そのものや、記号で表現します。
反粒子は``anti_*``ではじまるものがほとんどですが、
荷電レプトン（とパイ中間子）は、そのまま``*-``／``*+``と書きます。
