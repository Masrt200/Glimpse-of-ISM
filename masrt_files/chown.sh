#!/bin/bash
dir=`ls`

for i in ${dir}
do
echo $i
chown -R root:$i $i && chmod -R 750 $i
done
