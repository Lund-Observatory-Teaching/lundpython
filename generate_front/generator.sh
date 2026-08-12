#!/bin/bash

teachers=('Isabella Henum')
n_teachers=${#teachers[@]}
contact=('isabella.henum@fysik.lu.se')
topic=(Basics Numpy Matplotlib Tools)

for n in {1..4}; do
    convert front.jpeg \
        \( -size "3000x200" -pointsize 120 -background none -gravity northwest -fill white \
        -font "$HOME/Library/Fonts/LiberationMono-Bold.ttf" \
        caption:"Introduction to Python programming" \
        \( +clone -background black -shadow 80x5 \) +swap -background none -layers merge +repage \) \
        -geometry +50+600 -composite \
        \( -size "3000x300" -pointsize 220 -background none -gravity northwest -fill white \
        -font "$HOME/Library/Fonts/LiberationMono-Bold.ttf" \
        caption:"Lecture $n" \
        \( +clone -background black -shadow 80x2 \) +swap -background none -layers merge +repage \) \
        -geometry +50+750 -composite \
        \( -size "3000x300" -pointsize 120 -background none -gravity northwest -fill white \
        -font "$HOME/Library/Fonts/LiberationMono-Bold.ttf" \
        caption:"${topic[$((n - 1))]}" \
        \( +clone -background black -shadow 80x5 \) +swap -background none -layers merge +repage \) \
        -geometry +50+1000 -composite \
        \( -size "3000x300" -pointsize 60 -background none -gravity southwest -fill white \
        -font "$HOME/Library/Fonts/LiberationSans-Regular.ttf" \
        caption:"Division of Astrophysics" \
        \( +clone -background black -shadow 80x5 \) +swap -background none -layers merge +repage \) \
        -geometry +50+0 -composite \
        "../imgs/front_$n.jpeg"

    for ((nn = 0; nn < ${#teachers[@]}; nn++)); do
        convert "../imgs/front_$n.jpeg" \
            \( -size "3000x200" -pointsize 80 -background none -gravity southwest -fill white \
            -font "$HOME/Library/Fonts/LiberationSans-Regular.ttf" \
            caption:"${teachers[$nn]} - (${contact[$nn]})" \
            \( +clone -background black -shadow 80x5 \) +swap -background none -layers merge +repage \) \
            -geometry +50+$((80 + nn * 80)) -composite \
            "../imgs/front_$n.jpeg"
    done
done
