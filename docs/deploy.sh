#! /usr/bin/env bash

poetry run make latexpdf
rsync -auvz build/latex/kumaroot.pdf source/_static/
poetry run make html
rsync --delete -auvz build/html/ mypage:~/www/kumaroot/
