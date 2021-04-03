# This script will get passed a .csv file through the terminal
# then it will take out any rows missing data. Finally, it will
# load the corected data into a MySQL DB.
import re
import sqlite3
import sys

DB = 'batch_jobs.db'
# Connect to the DB and create a cursor object
CON = sqlite3.connect(DB)
CUR = CON.cursor()
OMITTED = []
def get_data():
    # This is the array to send to MySQL database
    fout = []
    with open(sys.argv[1], 'r') as fin:
        for line in fin:
            line = line.strip();
            check_element = line.split(',')
            add_line = True
            command = 'INSERT INTO batch VALUES ('
     

            # check to see if any elements are missing, if they are
            # dont add the line to the new csv file 
            for element in check_element:
                if element == '':
                    add_line = False
            if add_line:
                command += check_element[0] + ",'" + check_element[1] + "'," + check_element[2] + ")"
                CUR.execute(command)
            else:
                OMITTED.append(line)
        CON.commit()
    return fout

# This populates the DB with all data containing all elements

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

    get_data()
    print('Loaded', sys.argv[1], 'into', DB)
    CON.close()
