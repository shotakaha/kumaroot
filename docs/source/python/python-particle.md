# 素粒子したい（``particle``）

```python
from particle import Particle

Particle.from_pdgid(-11)
# e+

Particle.from_pdgid(13)
# mu-

Particle.from_pdgid(22)
# gamma
```

``particle``パッケージで、PDGで定義された素粒子の情報を確認できます。
Geant4で生成した粒子のPDGコードから、粒子名を逆引きするときに便利です。

## インストールしたい

```console
$ pip3 install particle
$ poetry add particle
$ rye add particle
```

## リファレンス

- [scikit-hep/particle - GitHub](https://github.com/scikit-hep/particle)
