#! /usr/bin/env bash

make latexpdf
mv build/latex/kumaroot.pdf source/_static/
make html
# rsync --delete -auvzn build/html/ mypage:~/www/kumaroot/
