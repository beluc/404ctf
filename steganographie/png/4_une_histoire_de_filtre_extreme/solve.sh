#!/bin/bash

file=$1

rm -rf $file.* $file.zlib $file.dat output
pngsplit $file
for i in $file.*.IDAT; do echo $i && dd if=$i bs=1 skip=8 of=$i.zlib; done
for i in $file.*.IDAT.zlib; do echo $i && truncate -s -4 $i; done
for i in $file.*.IDAT.zlib; do echo $i && cat $i >> $file.zlib ; done
file $file.zlib
cat $file.zlib | pigz -c -d > $file.dat
file $file.dat
#foremost -vi $file.dat
