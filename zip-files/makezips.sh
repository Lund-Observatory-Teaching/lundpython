#!/bin/bash
lectures=(0 1 2)
dirs=("1-intro" "2-numpy" "3-plotting" "4-tools")
heads=(5 12 17)
tails=(5 6 4)

for nl in ${lectures[@]}; do
  mkdir ${dirs[$nl]}
  cp -r `head -${heads[$nl]} files.txt | tail -${tails[$nl]}`  ${dirs[$nl]}
  zip -r ${dirs[$nl]}.zip ${dirs[$nl]}
  rm -rf ${dirs[$nl]}
done
