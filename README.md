# Respose to OLCF Coding Exercise 01

[Here](https://github.com/olcf/support-software-interview-exercise-01) is the complete excerise.

## What I Did

Using Flask, I created a RESTful API with a single endpoint that interfaces with a data base (SQLite3) and returns a [JSON-API](http://jsonapi.org/format/#fetching-resources) document.

## What I Used

### Python and Flask

I used Python because it works well with JSON object, and I am more fimiliar with its syntax than Ruby. Flask is a light weight framework that doesnt need to be packaged to run, you can use a small model instead. I used Flask for its simplicity and smaller learning curve.

### SQLite3

I chose SQLite3 because it is included in pythons standard libraries, Though you still need to install it onto your system to create the database. SQLite3 is another light weight program which that uses one file as the DB. In my case its `batch_jobs.db`. I did have an issue with the datetime but I found a temperary fix (see "Issue" section below)

## Install

to install python, Flask, and SQLite3 on a Linux system

### Ubuntu

```bash
sudo apt install python3 sqlite3
```

```bash
pip install flask
```

## Setup

Once you have everything install the setup is pretty easy. unzip the fiolder `ORNL_API_EXERCISE.zip` and cd into it. make sure the database is working properly and you're good to go. You could also copy this code:

```bash
unzip ORNL_API_EXERCISE.zip
cd ORNL_API_EXERCISE
sqlite3 batch_jobs.db
```

You should see a prompt similar to this:

```SQLite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite>
```

type `.database` and `.quit` like so:

```SQLite3
sqlite> .database
main: /home/username/Desktop/ORNL_API_EXERCISE/batch_jobs.db
sqlite> .quit
```

and you're done.

## A Breif Description of the Files

there are three files of intrest:`sqlite_schema.py`, `etl.py` and `server.py`

### sqlite_schema.py

This file sets up the database. It drops a table named `batch` and recreates it. to run it use this command:

```bash
python3 sqlite_schema.py
```

### etl.py

This script gets passed a csv file through the terminal, then it will remove any datasets that are not complete. Finaly, it will load the vetted data into the DB `batch_job.db`. To run it use this command:

```bash
python3 etl.py file.csv
```

there is `example_batch_records.csv` in the directory for easy of use.

### server.py

Lastly there server.py will run the actual API. to run it in debug mode use this command:

```bash
python3 server.py
```

This will run on **port 5000** So, when qeurying the database use http://localhost:5000/batch_jobs/

## Test Cases

To test out here are a few qeuries to try:

### Qeury

http://localhost:5000/batch_jobs/

### Response

a

### Qeury

http://localhost:5000/batch_jobs/

### Response

b

### Qeury

http://localhost:5000/batch_jobs/

### Response

c

### Qeury

http://localhost:5000/batch_jobs/

### Response

d
