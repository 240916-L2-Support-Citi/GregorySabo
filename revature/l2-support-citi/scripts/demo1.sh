#!/bin/bash

# set a reuse variable within our script

name="Issac"

# access the thing i named name a few lines ago
echo "$name"

get_name() {
  echo "$name"
}

echo "your name is $(get_name)"

#######################################################

get_name() {
  echo "$1"
}

echo "your name is $(get_name Miguel) nice to see you"

##################################################

# if you have a repetitive. once i is 9, this will be last
for ((i = 0;i<10;i++)); do
	echo "my name is greg $i"
done

###################################################

# conditional logic - to pay someone on friday
current_day=5
bank_account=0

if [[ current_day -eq 5 ]]; then
	bank_account=$((bank_account+500))
elif [[ current_day -eq 1 ]]; then 
	echo ":("
else
	echo "just another day"
fi

echo "$((bank_account))"

###########################################

#call a specific function from the command line

called_from_cli(){
	echo "this function was called from outside script"
}
#********need when calling
"$@"

###########################################
#we can call other scripts from within out demo1
	#use functions for other scripts
		#multiple options here

source ./demo2.sh
say_hello
