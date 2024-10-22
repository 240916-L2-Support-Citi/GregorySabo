import psycopg


fileName = "/Users/saybobobo/Desktop/repo/GregorySabo/GregorySaboP1/logs/errorlogs.txt"

try :

    # library psycopg file i/o, database connect, CRUD, 
        #1st create a connection a our postgres database
       
    with psycopg.connect("dbname=proj1 user=saybobobo") as connection:
        with connection.cursor() as cur:

            #select statement to pull count of errors from database
            cur.execute("SELECT COUNT(*) FROM LogData WHERE errorLevel='[ERROR]'")
            error_count =  cur.fetchone()[0]
        
            #select statement to pull count of FATAL from database
            cur.execute("SELECT COUNT(*) FROM LogData WHERE errorLevel='[FATAL]'")
            fatal_count = cur.fetchone()[0]
            
            #finally send and alert to the console when the threshold is reached
            if error_count >= 5 fatal_count >=1:
                print(f"ERROR - {error_count} logs")
            if fatal_count >=1:
                print(f"FATAL - {fatal_count}logs "}

except Exception as e:
    print("Error connecting to db: ", e)
