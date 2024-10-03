# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # ROOTしたい（PyROOT）
#
# ## ROOT関係の環境変数を確認する
#
# - PyROOTを使う場合、ROOTの環境変数を適切に設定する必要がある
#   - とくに``PYTHONPATH``の設定が重要
# - ROOT付属の設定スクリプトが用意されている
#   - Fishシェルの場合、ROOT付属の``bin/thisroot.fish``を読み込む
# - ``thisroot.fish``は2箇所にある
#   - ``$(root-config --prefix)/bin/thisroot.fish``（本体）
#   - ``/opt/homebrew/bin/thisroot.fish``（エイリアス）
# - 必ず本体を読み込む
#   - エイリアスを実行すると``ROOTSYS``が``/opt/homebrew``になって、うまくいかない

# ## 環境変数の設定
#
# - 次のセルを実行し、この環境でROOTを設定する

# !. $(root-config --prefix)/bin/thisroot.fish

# ## 環境変数の確認
#
# - 必要な環境変数が設定されていることを確認する
# - 上記のコマンドが実行されていない場合は、すべて`None`になる

# +
import os

env_names = [
    "ROOTSYS",
    "LD_LIBRARY_PATH",
    "DYLD_LIBRARY_PATH",
    "PYTHONPATH",
    # "MANPATH",
    "CMAKE_PREFIX_PATH",
    "JUPYTER_PATH",
    "JUPYTER_CONFIG_DIR",
]

for name in env_names:
    k = name
    v = os.environ.get(name)
    print(f"{k}: {v}")
# -

# ## PyROOTの動作確認
#
# - ``import ROOT``でPyROOTをインポートする
# - ``ROOT.__version__``でバージョンを確認する
# - ``ROOT.__file__``で実体があるパスを確認する

# +
import ROOT

ROOT.__version__
# -

ROOT.__file__

# CERNがウェブで公開しているチュートリアルに沿って確認する

from ROOT import TCanvas, TPad, gBenchmark, TFormula, TF1, TPaveLabel, TH1F, TFile

# TCanvas("name", "title", wwidth, wheight)
# TCanvas("name", "title", wtopx, wtopy, wwidth, wheight)
c1 = TCanvas("c1", "The FillRandom example", 500, 500)

# TPad("name", "title", xlow, ylow, xup, yup, color, bordersize, bordermode)
pad1 = TPad("pad1", "The pad with the function", 0.05, 0.50, 0.95, 0.95)
pad2 = TPad("pad2", "The pad with the histogram", 0.05, 0.05, 0.95, 0.45)

pad1.Draw()
pad2.Draw()

pad1.cd()

gBenchmark.Start("fillrandom")

# TFormula("name", "formula")
formula1 = TFormula("formula1", "abs(sin(x)/x)")

# TF1("name", "formula", xmin, xmax)
sqroot = TF1("sqroot", "x * gaus(0) + [3] * formula1", 0, 10)
sqroot.SetParameters(10, 4, 1, 20)
sqroot.SetLineColor(4)
sqroot.SetLineWidth(6)


pad1.SetGridx()
pad1.SetGridy()
pad1.GetFrame().SetBorderMode(-1)
pad1.GetFrame().SetBorderSize(5)

sqroot.Draw()
lfunction = TPaveLabel(5, 39, 9.8, 46, "The sqroot function")
lfunction.Draw()
c1.Update()

c1.Update()

pad2.cd()
pad2.GetFrame().SetBorderMode(-1)
pad2.GetFrame().SetBorderSize(5)

# TH1F("name", "title", nbinsx, xlow, xup)
# TH1F("name", "title", nbinsx, xbins)
h1f = TH1F("h1f", "Test Random Numbers", 200, 0, 10)
h1f.SetFillColor(45)
h1f.FillRandom("sqroot", 10000)
h1f.Draw()
c1.Update()

# TFile("filename", "mode")
f = TFile("fillrandom-py.root", "RECREATE")
formula1.Write()
sqroot.Write()
h1f.Write()
gBenchmark.Show("fillrandom")

# +
from ROOT import gROOT

gROOT.GetListOfCanvases().Draw()
# -

from ROOT import gStyle

gStyle.SetPadGridX

h1f.Draw()
c1.Update()
c1.Draw()

c1.Draw()
