#!/bin/bash

args=("$@")
GIT='git --git-dir='$PWD'/.git'
MARKPLATE=/home/cecinuga/Scrivania/Github/markplate

alias python=${MARKPLATE}'/env/lib/python3.12' 
source ${MARKPLATE}/env/bin/activate

python ${MARKPLATE}/markplate.py --temp ${MARKPLATE}/templates/computational_complexity.jinja --out ./${args[0]} --out-file README.md --cb ${MARKPLATE}/callbacks/computational_complexity.py --ex-cb-dir ./${args[0]}/algorithms --exclude [.git,.gitignore,README.md,git-pipeline.sh] -username cecinuga

deactivate
$GIT add .
$GIT commit -m ${args[1]}
$GIT push

