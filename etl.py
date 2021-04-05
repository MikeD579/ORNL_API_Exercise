# This script will get passed a .csv file through the terminal
# then it will take out any rows missing data. Finally, it will
# load the corected data into a MySQL DB.
import re
import sqlite3
import sys
 
# Connect to the DB and create a cursor object
DB = 'batch_jobs.db'
CON = sqlite3.connect(DB)
CUR = CON.cursor()
OMITTED = []

def load_data():
    # Open the file passed in form terminal, and check the values
    with open(sys.argv[1], 'r') as fin:
        for line in fin:
            line = line.strip()
            elements = line.split(',')
            add_line = True
 
            # Check to see if any elements are missing, if they are
            # dont add the line to the new csv file 
            for e in elements:
                if e == '':
                    add_line = False
            if add_line:
                # Insert the line into the DB
                datetime = elements[1].split('+')[0]
                print (datetime)
                CUR.execute('INSERT INTO batch VALUES(?,?,?)', (elements[0], datetime, elements[2]))
            else:
                # Omittes line will be printed out at end of program
                OMITTED.append(line)
        # After all lines have been itterated through commit to DB
        CON.commit()

if __name__ == '__main__':
    # Simple error handling
    if len(sys.argv) != 2:
        print('please provide a file to ETL: python3 etl.py file.csv')
        CON.close()
        exit(1)
    if not re.match('.*.csv', sys.argv[1]):
        print('Please use a .csv file to ETL')
        CON.close()
        exit(1)

    # If no error, then load the data into the database
    load_data()
    print('Loaded', sys.argv[1], 'into', DB)
    print('Lines omitted')
    for e in OMITTED:
        print (e)
    CON.close()
