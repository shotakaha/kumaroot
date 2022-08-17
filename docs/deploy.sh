#! /usr/bin/env bash

make latexpdf
rsync -auvz build/latex/kumaroot.pdf source/_static/
make html
rsync --delete -auvz build/html/ mypage:~/www/kumaroot/
