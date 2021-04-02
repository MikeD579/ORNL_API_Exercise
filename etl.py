# This script will get passed a .csv file through the terminal
# then it will take out any rows missing data. Finally, it will
# load the corected data into a MySQL DB.
import sys
import sqlite3

def get_data():
    # This is the array to send to MySQL database
    fout = []

    for line in sys.stdin:
        line = line.strip();
        check_element = line.split(',')
        add_line = True

        # check to see if any elements are missing, if they are
        # dont add the line to the new csv file 
        for element in check_element:
            if element == '':
                add_line = False

        if add_line:
            fout.append(line)
    return fout

# This should connect to the DB and populate it with the new csv
def push_data():
    pass

if __name__ = '__main__':
    push_data(get_data())
