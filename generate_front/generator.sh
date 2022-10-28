#!/bin/bash

teachers=('Simon Alinder' 'Eero Vaher')
n_teachers=${#teachers[@]}
contact=(simon.alinder@astro.lu.se eero.vaher@astro.lu.se mikkola@astro.lu.se)
topic=(Basics Numpy Matplotlib Tools)
for n in {1..4}; do
  convert front.jpeg\
    \( -size "3000x200" -pointsize 120 -background none -gravity northwest -fill white \
    caption:"Introduction to Python programming" \
    \( +clone -background black -shadow 80x5  \) +swap -background none -layers merge +repage \) \
    -geometry +50+600 -composite \
    \
    \( -size "3000x300" -pointsize 220 -background none -gravity northwest -fill white \
    caption:"Lecture $n" \
    \( +clone -background black -shadow 80x2  \) +swap -background none -layers merge +repage \) \
    -geometry +50+750 -composite \
    \
    \( -size "3000x300" -pointsize 120 -background none -gravity northwest -fill white \
    caption:"${topic[`expr $n - 1`]}" \
    \( +clone -background black -shadow 80x5  \) +swap -background none -layers merge +repage \) \
    -geometry +50+1000 -composite \
    \
    \( -size "3000x300" -pointsize 60 -background none -gravity southwest -fill white \
    caption:"Department of Astronomy and Theoretical Physics" \
    \( +clone -background black -shadow 80x5  \) +swap -background none -layers merge +repage \) \
    -geometry +50+0 -composite \
    ../imgs/$(echo front_$n.jpeg)

  for ((nn=0; nn<=`expr ${#teachers[@]} - 1`; nn++)); do
    convert ../imgs/$(echo front_$n.jpeg)\
      \( -size "3000x200" -pointsize 80 -background none -gravity southwest -fill white \
      caption:"${teachers[$nn]} - (${contact[$nn]})" \
      \( +clone -background black -shadow 80x5  \) +swap -background none -layers merge +repage \) \
      -geometry +50+`expr 80 + $nn \* 80` -composite \
      ../imgs/$(echo front_$n.jpeg)
  done
done
