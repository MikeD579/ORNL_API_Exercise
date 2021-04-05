# Respose to OLCF Coding Exercise 01

Here is the [Assignment](https://github.com/olcf/support-software-interview-exercise-01)

## What I Did

Using Flask, I created a RESTful API with a single endpoint interfaces with a data base and returns a [JSON-API](http://jsonapi.org/format/#fetching-resources) document.

why I used (justifications)
how to install

```bash
pip install db-sqlite3 Flask
```

what i did
why I did it








there are two files: etl.py and server.py

## etl.py

This script gets passed a csv file through the terminal `etl.py < example\_batch\_records.csv`, then it will remove any datasets that are not complete. Finaly, it will load the vetted data into a MySQL DB.

This file will not check if the data is an integer, or ISO date.

## server.py
TODO
