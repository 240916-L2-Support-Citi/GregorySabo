#!/bin/bash

#i'm going to create a variable and store the name of my file in it
	#this file doesnt exist until we run it once
LOG_FILE="/Users/saybobobo/desktop/repo/revature/l2-support-citi/cronjobdemo/time_log.txt"

#this will put the echo output into file
	#creates file if not already created
echo "current data and time is: $(date)" >> "$LOG_FILE"
