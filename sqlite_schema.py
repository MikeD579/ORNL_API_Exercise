# This is a script that will setup/re-setup the database
# with the correct table needed for the batch_job
import sqlite3

con = sqlite3.connect('batch_jobs.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS batch')
con.commit()
print ('Droped table. (if it existed at all)')

# Creating a table with two primary keys, because the batch
# number is not unique by itself, but only with the day in
# which the batch was created.
cur.execute('''CREATE TABLE batch (
	batch_number    INT         NOT NULL,
	submitted_at    DATETIME    NOT NULL,
	nodes_used      INT	    NOT NULL,
        PRIMARY KEY(batch_number, submitted_at));''')
print('Created table. ("batch")')

con.commit()
con.close()
print('Closed Connection.')
