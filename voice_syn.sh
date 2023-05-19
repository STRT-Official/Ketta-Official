#!/usr/bin/env bash
##space=" "
##string=($(cat tospeak.txt))

##for item in "${string[@]}"; do
    #echo "$item"
##    string+="${space} ${item}"
##echo "$string"
##larynx -v cmu_eey-glow_tts "$string" > output.wav

##done
file1=`< tospeak.txt`
echo $file1
larynx -v cmu_eey-glow_tts "$file1" > output.wav
