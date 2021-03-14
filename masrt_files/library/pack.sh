#!/bin/bash

methods=( "zip" "7z" "gzip" "xz" "bzip2" "tar" )
ZIPME=$1
len=$2

#making backup
cp $ZIPME $ZIPME.bak

for((i=0;i<len;i++))
do
	idx=$(($RANDOM%6))
	printf "$i "
	if [[ ${methods[idx]} == "7z" ]]
		then
			7z a book$i $ZIPME > /dev/null
			echo "7ZIP" 
	elif [[ ${methods[idx]} == "zip" ]]
		then
			zip -q book$i $ZIPME
			echo "ZIP"
	elif [[ ${methods[idx]} == "bzip2" ]]
		then
			bzip2 $ZIPME -c > book$i
			echo "BZIP2"
	elif [[ ${methods[idx]} == "tar" ]]
		then
			tar -cf book$i $ZIPME
			echo "TAR"
	elif [[ ${methods[idx]} == "xz" ]]
		then
			xz $ZIPME -c > book$i
			echo "XZ"
	elif [[ ${methods[idx]} == "gzip" ]]
		then
			gzip $ZIPME -c > book$i
			echo "GZIP"
	fi

	rm $ZIPME
	if [[ ${methods[idx]} == "7z" ]]
		then
			ZIPME=book$i.7z
	elif [[ ${methods[idx]} == "zip" ]]
		then
			ZIPME=book$i.zip
	else
		ZIPME=book$i
	fi
done

