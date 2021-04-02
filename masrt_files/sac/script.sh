#!/bin/bash
printf "Sanity Check! input this level's password: "
read password

if [[ $password == "hi" ]]
then
        printf "\033[0;32mpassed\033[0m\n"
        echo "------------------------"

        cat script.sh
        printf "\n"
        printf "\n"

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
else
printf "\033[0;93mYOU ARE INSANE!!!\033[0m"
fi
