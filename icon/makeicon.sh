#!/bin/sh

if [ -z "$1" ];then
    echo "Usage: makeicon.sh IconName"
    exit 1
fi

set -x

mkdir $1.iconset

sips -s format png  -z 16 16      $1.png --out $1.iconset/icon_16x16.png
sips -s format png  -z 32 32      $1.png --out $1.iconset/icon_16x16@2x.png
sips -s format png  -z 32 32      $1.png --out $1.iconset/icon_32x32.png
sips -s format png  -z 64 64      $1.png --out $1.iconset/icon_32x32@2x.png
sips -s format png  -z 128 128    $1.png --out $1.iconset/icon_128x128.png
sips -s format png  -z 256 256    $1.png --out $1.iconset/icon_128x128@2x.png
sips -s format png  -z 256 256    $1.png --out $1.iconset/icon_256x256.png
sips -s format png  -z 512 512    $1.png --out $1.iconset/icon_256x256@2x.png
sips -s format png  -z 512 512    $1.png --out $1.iconset/icon_512x512.png
sips -s format png  -z 1024 1024  $1.png --out $1.iconset/icon_512x512@2x.png

iconutil -c icns $1.iconset

rm -R $1.iconset
