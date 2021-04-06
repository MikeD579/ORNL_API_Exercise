# This script will get passed a .csv file through the terminal
# then it will take out any rows missing data. Finally, it will
# load the corected data into a SQLite3 DB.
import re
import sqlite3
import sys
 
# Connect to the DB and create a cursor object
DB = 'batch_jobs.db'
CON = sqlite3.connect(DB)
CUR = CON.cursor()
# A list of omitted lines
OMITTED = []
COUNT = 0

if __name__ == '__main__':
    # Simple error handling
    if len(sys.argv) < 2:
        print('please provide a file to ETL: python3 etl.py file.csv')
        CON.close()
        exit(1)
    if not re.match('.*.csv', sys.argv[1]):
        print('Please use a .csv file to ETL')
        CON.close()
        exit(1)

    # If no error, then ETL the data into the database.
    # Open the file passed in form terminal, and check the values.
    with open(sys.argv[1], 'r') as fin:
        for line in fin:
            COUNT += 1
            line = line.strip()
            elements = line.split(',')
            add_line = True
 
            # Check to see if any elements are missing, if they are
            # don't add the values to the DB. 
            for e in elements:
                if e == '':
                    add_line = False
            if add_line:
                # Insert the line into the DB without timezone
                datetime = elements[1].split('+')[0]
                CUR.execute('INSERT INTO batch VALUES(?,?,?)', (elements[0], datetime, elements[2]))
            else:
                # Keep track of the ommited lines
                OMITTED.append(line)
        # After all lines have been itterated through, commit to DB.
        CON.commit()
    
    print('Loaded', sys.argv[1], 'into', DB)
    print('Lines omitted (' + str(len(OMITTED)-1) + ') out of (' + str(COUNT-1) + ')')
    if len(sys.argv) == 3 and sys.argv[2] == '--verbose':
        for o in OMITTED:
            print ('   ', o)
    else:
        print('To see which lines are removed run "python3 etl.py ' + sys.argv[1] + ' --verbose"')
    CON.close()
