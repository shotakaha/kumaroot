==================================================
１次元ヒストグラムを作成したい（ ``TH1D`` ）
==================================================


==================================================
２次元ヒストグラムを作成したい（ ``TH2D`` ）
==================================================

.. code:: cpp

    TH2D TH2D(const char* name, const char* title, Int_t nbinsx, Double_t xlow, Double_t xup, Int_t nbinsy, Double_t ylow, Double_t yup)
    Int_t Fill(Double_t x, Double_t y)
    void Draw(Option_t* option = "")
