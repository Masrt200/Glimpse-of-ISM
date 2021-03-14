#!/bin/bash

INPUT=$1
len=$2

#make backup for original file
cp $INPUT $INPUT.bak

for((i=0;i<len;i++))
do
FTYPE=`file ${INPUT}`

if [[ "$FTYPE" == *"POSIX tar"* ]]; then
    echo "TAR"
    tar -xOvf "$INPUT" > tmp
    cp tmp $INPUT
elif [[ "$FTYPE" == *"Zip archive data"* ]]; then
    echo "ZIP"
    unzip -p "$INPUT" > tmp
    cp tmp $INPUT
elif [[ "$FTYPE" == *"bzip2 compressed"* ]]; then
    echo "BZIP"
    bzcat "$INPUT" > tmp
    cp tmp $INPUT
elif [[ "$FTYPE" == *"gzip compressed data"* ]]; then
    echo "GZIP"
    zcat "$INPUT" > tmp
    cp tmp $INPUT
elif [[ "$FTYPE" == *"XZ compressed data"* ]]; then
    echo "XZ"
    xzcat "$INPUT" > tmp
    cp tmp $INPUT
elif [[ "$FTYPE" == *"7-zip archive data"* ]]; then
    echo "7ZIP"
    7z e -so "$INPUT" -y > tmp
    cp tmp $INPUT
else
    echo "NOT RECOGNIZED"
    echo ${FTYPE}
fi
done
#run it with while true;
