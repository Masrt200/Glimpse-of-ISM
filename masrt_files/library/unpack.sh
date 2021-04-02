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
elif [[ "$FTYPE" == *"Zip archive data"* ]]; then
    echo "ZIP"
    unzip -p "$INPUT" > tmp
elif [[ "$FTYPE" == *"bzip2 compressed"* ]]; then
    echo "BZIP"
    bzcat "$INPUT" > tmp
elif [[ "$FTYPE" == *"gzip compressed data"* ]]; then
    echo "GZIP"
    zcat "$INPUT" > tmp
elif [[ "$FTYPE" == *"XZ compressed data"* ]]; then
    echo "XZ"
    xzcat "$INPUT" > tmp
elif [[ "$FTYPE" == *"7-zip archive data"* ]]; then
    echo "7ZIP"
    7z e -so "$INPUT" -y > tmp
else
    echo "NOT RECOGNIZED"
    echo ${FTYPE}
    exit
fi

cp tmp $INPUT
done
#run it with while true;
