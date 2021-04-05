from datetime import datetime, MAXYEAR, MINYEAR
from flask import Flask, jsonify, render_template, request
import re
import sqlite3
app = Flask(__name__)

# Sets a root endpoint
@app.route('/')
def root():
    return render_template('index.html')

# Builds the query and formats a json response
@app.route('/batch_jobs/')
def batch_jobs():
    con = sqlite3.connect('batch_jobs.db')
    cur = con.cursor()

    # request.agrs retruns a dictionary that contains the filters
    filters = request.args
    
    build_query = 'SELECT * FROM batch WHERE 1'
    for key in filters:
        value = filters[key]
        if key == 'filter[submitted_after]':
            #TODO regex check for datetime
            build_query += ' AND submitted_at >= ' + filters[key]
        elif key == 'filter[submitted_before]':
            build_query += ' AND submitted_at <= ' + filters[key]
        elif key == 'filter[min_nodes]':
            try:
                if isinstance(int(filters[key], int)):
                    build_query += ' AND nodes_used >= ' + filters[key]
            except:
                print('ERROR: not an int')
        elif key == 'filter[max_nodes]':
            try:
                if isinstance(int(filters[key], int)):
                    build_query += ' AND nodes_used <= ' + filters[key]
            except:
                print('ERROR: not an int')
        else:
            return ('Something has gone wrong. Cannot query ' + key + '=' + value + '<br>Check to see if the value is wrong.')
    build_query += ';'

    # Sends query to the DB
    try:
        cur.execute(build_query)
    except e:
        return render_template('404.html')
    # rows = a list of 3-tuples (batch_number, submitted_at, nodes_used)
    rows = cur.fetchall()
    
    # Builds the JSON structure form the bottom up
    data = []
    if len(rows) > 0:
        for n,r in enumerate(rows):
            attributes = {
                'batch_number': r[0],
                'submitted_at': r[1],
                'nodes_used': r[2]
            }
            data_values = {
                'type': 'articles',
                'id': str(n+1),
                'attributes': attributes
            }
            data.append(data_values)
    else:
        data = None

    links = {'self': request.url}
    json_str = {'links': links, 'data': data}

    con.close()
    return jsonify(json_str)

if __name__ == '__main__':
    app.run(debug=True)
