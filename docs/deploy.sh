#! /usr/bin/env bash

uv run make latexpdf
rsync -auvz build/latex/kumaroot.pdf source/_static/
uv run make html
rsync --delete -auvz build/html/ mypage:~/www/kumaroot/
