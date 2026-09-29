#!/usr/bin/env bash
# Take the render edge off a generated frame so it reads as a photograph:
# pull saturation and contrast back a touch, roll the highlights off like
# film, soften the over-sharp edges, add a mild lens vignette, then lay a
# fine luminance grain on top (last, so nothing blurs it). Subtle on purpose.
#   photo_grade.sh in.png out.jpg [width]
set -e
in=$1; out=$2; w=${3:-1800}
ffmpeg -y -v error -i "$in" -vf "\
scale=$w:-2,\
eq=saturation=0.88:contrast=0.96:brightness=0.004,\
curves=m='0/0.012 0.22/0.20 0.55/0.56 0.82/0.84 1/0.975',\
unsharp=5:5:-0.35:5:5:0,\
vignette=angle=PI/5.2:mode=forward,\
noise=c0s=6:c0f=t+u:c1s=2:c1f=t+u:c2s=2:c2f=t+u" \
-q:v 3 "$out"
