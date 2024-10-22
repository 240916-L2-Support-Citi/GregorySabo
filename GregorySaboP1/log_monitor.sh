#!/bin/bash

LOGFILE="logs/app.log"
#database
DB="proj1"
#machine username
USER="saybobobo"


#this is a algorithm for taking a logfile  a reading it line by line
		#because it 
                #reads each line from the logfile(logs/app.log).
		# and stores it in the variable line
		#pipe the logfile to  the while loop
tail -F $LOGFILE | while read line; do
       
          #This BASH shell will be monitoring for ERROR and FATAL
          
    if [[ $line == *"[ERROR]"* ]] || [[ $line == *"[FATAL]"* ]]; then

        #awk grab timestamp,level,message
			  #'####-##-## ##:##:##'
        TIMESTAMP=$(echo $line | awk '{print $1" "$2}')
            #it will be in spot three . argument 3.
        #error/priorityLevel "INFO WARNING ERROR FATAL)"
        LEVEL=$(echo $line | awk '{print $3}')
        #descriptive message is in field 2
        MESSAGE=$(echo $line | awk -F ']' '{print $2}')
        
        # Insert into PostgreSQL
        psql -U $USER -d $DB -c "INSERT INTO LogData (timestamp, errorlevel, messages) VALUES ('$TIMESTAMP', '$LEVEL', '$MESSAGE')"
    fi
done
