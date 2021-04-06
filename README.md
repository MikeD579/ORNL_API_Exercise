# Respose to OLCF Coding Exercise 01

[Here](https://github.com/olcf/support-software-interview-exercise-01) is the complete exercise.

## What I Did

Using Flask, I created a RESTful API with a single endpoint that interfaces with a database (SQLite3) and returns a [JSON-API](http://jsonapi.org/format/#fetching-resources) document.

## What I Used

### Python and Flask

I used Python because it works well with JSON objects, and I am more familiar with its syntax than Ruby. I used Flask for its simplicity. Flask is a lightweight framework that does not need to be packaged to run, you can use a small model instead.

### SQLite3

I chose SQLite3 because it is included in Python standard libraries, Though you still need to install it onto your system to create the database. SQLite3 is another lightweight program which that uses one file as the DB. In my case, it is `batch_jobs.db`. I did have an issue with the DateTime but I found a temporary fix (see "Issue" section below)

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

Once you have everything install the setup is pretty easy. unzip the folder `ORNL_API_EXERCISE.zip` and cd into it. make sure the database is working properly and you're good to go. You could also copy this code:

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

## How to Run the Web App

there are three files of intrest:`sqlite_schema.py`, `etl.py` and `server.py`

### sqlite_schema.py

This file sets up the database. It drops a table named `batch` and recreates it. to run it use this command:

```bash
python3 sqlite_schema.py
```

### etl.py

This script gets passed a .csv file through the terminal, then it will remove any datasets that are not complete. Finally, it will load the transformed data into the DB `batch_job.db`. To run it use this command:

```bash
python3 etl.py file.csv
```

there is `example_batch_records.csv` in the directory for easy use.

### server.py

Lastly there server.py will run the actual API. to run it in debug mode use this command:

```bash
python3 server.py
```

This will run on **port 5000** So, when querying the database use <http://localhost:5000/batch_jobs/>

## Test Cases

To test out here are a few queries to try using `example_batch_records.csv` as the data:

### Query 1

<http://localhost:5000/batch_jobs?filter[submitted_after]='2018-03-04T23:00:00+00:00'>

### Response 1

```JSON
{
"data": [
{
"attributes": {
"batch_number": 993, 
"nodes_used": 12986, 
"submitted_at": "2018-03-04T23:02:25+00:00"
}, 
"id": "1", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 994, 
"nodes_used": 3681, 
"submitted_at": "2018-03-04T23:09:37+00:00"
}, 
"id": "2", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 996, 
"nodes_used": 7126, 
"submitted_at": "2018-03-04T23:24:01+00:00"
}, 
"id": "3", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 997, 
"nodes_used": 1, 
"submitted_at": "2018-03-04T23:31:13+00:00"
}, 
"id": "4", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 998, 
"nodes_used": 19715, 
"submitted_at": "2018-03-04T23:38:25+00:00"
}, 
"id": "5", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 999, 
"nodes_used": 14233, 
"submitted_at": "2018-03-04T23:45:37+00:00"
}, 
"id": "6", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 1000, 
"nodes_used": 9623, 
"submitted_at": "2018-03-04T23:52:49+00:00"
}, 
"id": "7", 
"type": "articles"
}
], 
"links": {
"self": "http://localhost:5000/batch_jobs/?filter%5Bsubmitted_after%5D=%272018-03-04T23:00:00+00:00%27"
}
}

```

### Query 2

<http://localhost:5000/batch_jobs?filter[submitted_after]='2017-03-01T00:00:00+00:00'&filter[submitted_before]='2019-03-01T23:59:59+00:00'>

### Response 2

`Everything in the database`

### Query 3

<http://localhost:5000/batch_jobs?filter[submitted_after]='2018-02-28T07:00:00+00:00'&filter[submitted_before]='2018-03-01T09:00:00+00:00'&filter[max_nodes]=500>

### Response 3

```JSON
{
"data": [
{
"attributes": {
"batch_number": 138, 
"nodes_used": 454, 
"submitted_at": "2018-02-28T16:26:25+00:00"
}, 
"id": "1", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 165, 
"nodes_used": 89, 
"submitted_at": "2018-02-28T19:40:49+00:00"
}, 
"id": "2", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 181, 
"nodes_used": 414, 
"submitted_at": "2018-02-28T21:36:01+00:00"
}, 
"id": "3", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 189, 
"nodes_used": 22, 
"submitted_at": "2018-02-28T22:33:37+00:00"
}, 
"id": "4", 
"type": "articles"
}, 
{
"attributes": {
"batch_number": 262, 
"nodes_used": 308, 
"submitted_at": "2018-03-01T07:19:13+00:00"
}, 
"id": "5", 
"type": "articles"
}
], 
"links": {
"self": "http://localhost:5000/batch_jobs/?filter%5Bsubmitted_after%5D=%272018-02-28T07:00:00+00:00%27&filter%5Bsubmitted_before%5D=%272018-03-01T09:00:00+00:00%27&filter%5Bmax_nodes%5D=500"
}
}

```

### Query 4

<http://localhost:5000/batch_jobs?filter[submitted_after]='2018-02-28T15:00:00+00:00'&filter[submitted_before]='2018-03-01T15:00:00+00:00'&filter[min_nodes]=2&filter[max_nodes]=20>

### Response 4

```JSON
{
"data": null, 
"links": {
"self": "http://localhost:5000/batch_jobs/?filter%5Bsubmitted_after%5D=%272018-02-28T15:00:00+00:00%27&filter%5Bsubmitted_before%5D=%272018-03-01T15:00:00+00:00%27&filter%5Bmin_nodes%5D=2&filter%5Bmax_nodes%5D=20"
}
}
```
