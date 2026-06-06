#!/usr/bin/env bash
# Build a cinematic Sarasota drone-style MP4 reel from our own real
# Sarasota photos. 1600x900, ~17 s, ~3-5 MB, H.264 +faststart, no audio.
#
# Output:
#   assets/video/sarasota-reel.mp4  — primary (H.264)
#   assets/video/sarasota-reel.webm — fallback (VP9, ~30 % smaller)
#   assets/video/sarasota-reel-poster.jpg — first-frame poster
#
# Notes:
#   - All motion is done with `crop` using time expressions (`t`).
#     `zoompan` was avoided because it interacts badly with `-loop 1`.
#   - Each input is up-scaled larger than the final 1600×900 viewport
#     so the crop window can pan/zoom without revealing edges.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHOTOS="$ROOT/assets/photos"
OUT="$ROOT/assets/video"
TMP="$(mktemp -d -t lumareel.XXXXXX)"

mkdir -p "$OUT"
echo "tmp:    $TMP"
echo "photos: $PHOTOS"
echo "out:    $OUT"

W=1600           # final width
H=900            # final height
FPS=30           # frame rate
DUR=4.5          # seconds per clip
XF=0.7           # crossfade duration

# Helper: render one Ken Burns clip (motion via crop+scale).
# Args: $1 src image, $2 vf-filter, $3 output mp4
render_clip () {
  local src="$1" vf="$2" out="$3"
  ffmpeg -y -loglevel error \
    -loop 1 -t "$DUR" -i "$src" \
    -vf "$vf,scale=${W}:${H}:flags=lanczos,format=yuv420p,fps=$FPS" \
    -frames:v $(awk -v d=$DUR -v f=$FPS 'BEGIN{printf "%d", d*f}') \
    -c:v libx264 -preset medium -crf 21 -pix_fmt yuv420p -an \
    "$out"
}

# ─ Clip 1: turtle-aerial (1600x2400 portrait) — vertical pan top→bottom,
#   gives a feeling of a drone descending from sky toward Gulf surf.
#   We scale to width=2200 (h≈3300), then pan a 2200×1238 viewport (16:9)
#   from y=0 (sky) to y=2062 (water). Final scale 1600x900.
render_clip "$PHOTOS/sarasota-turtle-aerial.jpg" \
  "scale=2200:-2:flags=lanczos,crop=2200:1238:0:'(in_h-1238)*t/$DUR'" \
  "$TMP/c1.mp4"
echo "  built c1 (turtle aerial — vertical descent)"

# ─ Clip 2: downtown-bayfront (1600x1067 landscape) — diagonal glide,
#   upper-left → lower-right. Scale to 2400×1601, crop a 1920×1080
#   viewport panning across the wider source. End frame favours the
#   bayfront skyline at the centre.
render_clip "$PHOTOS/sarasota-downtown-bayfront.jpg" \
  "scale=2400:-2:flags=lanczos,\
crop=1920:1080:'(in_w-1920)*t/$DUR':'(in_h-1080)*t/$DUR'" \
  "$TMP/c2.mp4"
echo "  built c2 (downtown — diagonal glide)"

# ─ Clip 3: ringling-bridge (1600x899 landscape) — left→right pan,
#   reveals bridge span. Scale to 2600×1461, crop 2080×1170 (16:9)
#   panning x from 0 to (in_w-out_w).
render_clip "$PHOTOS/sarasota-ringling-bridge.jpg" \
  "scale=2600:-2:flags=lanczos,crop=2080:1170:'(in_w-2080)*t/$DUR':'(in_h-1170)*0.55'" \
  "$TMP/c3.mp4"
echo "  built c3 (Ringling bridge — horizontal pan)"

# ─ Clip 4: marina (1600x899 landscape) — reverse diagonal,
#   lower-right → upper-left (drone pulling back / rising up). Scale to
#   2400×1349, crop a 1920×1080 viewport that drifts back to the corner.
render_clip "$PHOTOS/sarasota-marina.jpg" \
  "scale=2400:-2:flags=lanczos,\
crop=1920:1080:'(in_w-1920)*(1-t/$DUR)':'(in_h-1080)*(1-t/$DUR)'" \
  "$TMP/c4.mp4"
echo "  built c4 (marina — reverse diagonal pull-back)"

# Sanity: all clip durations should equal $DUR.
for f in c1 c2 c3 c4; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$TMP/$f.mp4")
  s=$(du -h "$TMP/$f.mp4" | cut -f1)
  echo "  $f.mp4  duration=$d  size=$s"
done

# Compute xfade offsets:
#   the i-th xfade fires at (i*DUR - i*XF) seconds.
OFF1=$(awk -v d=$DUR -v xf=$XF 'BEGIN{printf "%.3f", d-xf}')
OFF2=$(awk -v d=$DUR -v xf=$XF 'BEGIN{printf "%.3f", 2*d-2*xf}')
OFF3=$(awk -v d=$DUR -v xf=$XF 'BEGIN{printf "%.3f", 3*d-3*xf}')
echo "  xfade offsets: $OFF1, $OFF2, $OFF3"

# Concat the four clips with crossfade dissolves.
ffmpeg -y -loglevel error \
  -i "$TMP/c1.mp4" -i "$TMP/c2.mp4" -i "$TMP/c3.mp4" -i "$TMP/c4.mp4" \
  -filter_complex "
    [0:v][1:v]xfade=transition=fade:duration=$XF:offset=$OFF1[a];
    [a][2:v]xfade=transition=fade:duration=$XF:offset=$OFF2[b];
    [b][3:v]xfade=transition=fade:duration=$XF:offset=$OFF3[v]
  " \
  -map "[v]" \
  -c:v libx264 -preset slow -crf 24 -pix_fmt yuv420p \
  -profile:v high -level 4.0 -movflags +faststart -an \
  "$OUT/sarasota-reel.mp4"
echo "  reel built"

# Poster: a frame ~1 s in (avoids the very first scaled frame).
ffmpeg -y -loglevel error -ss 1.0 -i "$OUT/sarasota-reel.mp4" \
  -frames:v 1 -q:v 3 "$OUT/sarasota-reel-poster.jpg"
echo "  poster built"

# WebM (VP9) fallback — Chrome/Firefox/Edge prefer it, ~30 % smaller.
ffmpeg -y -loglevel error -i "$OUT/sarasota-reel.mp4" \
  -c:v libvpx-vp9 -b:v 0 -crf 36 -row-mt 1 -tile-columns 2 -threads 4 \
  -pix_fmt yuv420p -an "$OUT/sarasota-reel.webm" \
  || echo "  WARN: webm encode failed (skipping)"

echo ""
ls -lh "$OUT"
echo ""
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/sarasota-reel.mp4" \
  | awk '{printf "final duration: %.2f s\n", $1}'

rm -rf "$TMP"
echo "done."
