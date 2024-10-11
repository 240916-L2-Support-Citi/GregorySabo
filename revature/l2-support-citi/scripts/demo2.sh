#!/bin/bash

#this script is going to hold function. called from outside .sh file

say_hello() {
	echo "Greetings from demo2!!"
}

its_friday() {
	echo "time to touch grass"
}

"$@"
#this will now take arguments from where ever
