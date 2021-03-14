#!/bin/bash
function check_space {
        if [[ $1 == *[bdks';''&'' ']* ]]
        then
                return 0
        fi

        return 1
}

while :
do
        printf "keyword plz: "
        read input
        if check_space "$input"
        then
                echo -e '\033[0;31mhmmph, bad keyword\033[0m'
        else
                output="echo -e '\033[0;32mthis was left for you:\033[0m' $input"
                eval $output
        fi
	printf "\n"
done
