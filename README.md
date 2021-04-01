<h1>Respose to ORNL API Exercise</h1>
there are two files: etl.py and server.py

<h2>etl.py</h2>
This script gets passed a csv file through the terminal <code>etl.py < example\_batch\_records.csv</code>, then it will remove any datasets that are not complete. Finaly, it will load the vetted data into a MySQL DB.

This file will not check if the data is an integer, or ISO date.

<h2>server.py</h2>
TODO
