# This is the API connection from the URL endpoint to the database.
from flask import Flask, jsonify, render_template, request
import sqlite3
app = Flask(__name__)

# Sets a root endpoint and servers a index.html
@app.route('/')
def root():
    return render_template('index.html')

# When the endpoint /batch_jobs is called the API with handle
# queries with a list of filters, then return a dictionary 
@app.route('/batch_jobs/')
def batch_jobs():
    con = sqlite3.connect('batch_jobs.db')
    cur = con.cursor()

    # request.agrs retruns a dictionary that contains the filters
    filters = request.args
    build_query = 'SELECT * FROM batch WHERE 1'

    for key in filters:
        value = filters[key]
        # Check each filter to see if its right
        if key == 'filter[submitted_after]':
            # SQLite cannot handle timezones. Therefore, because the 
            # data is all in the same timezone, we can remove the timezone
            # TODO convert the timezone if needed
            datetime = value.split()[0] + "'"
            build_query += " AND datetime(submitted_at) >= datetime(" + datetime + ")"
        elif key == 'filter[submitted_before]':
            datetime = value.split()[0] + "'"
            build_query += " AND datetime(submitted_at) <= datetime(" + datetime + ")"
        elif key == 'filter[min_nodes]':
            # Check if it is an int or a literal
            try:
                if isinstance(int(value), int):
                    build_query += ' AND nodes_used >= ' + value
            except:
                print('ERROR: not an int')
        elif key == 'filter[max_nodes]':
            # Check if it is an int or a literal
            try:
                if isinstance(int(value), int):
                    build_query += ' AND nodes_used <= ' + value
            except:
                print('ERROR: not an int')
        else:
            return ('Something has gone wrong. Cannot query ' + key + '=' + value + '<br>Check to see if the value is wrong.')
    build_query += ';'

    # Sends query to the DB
    try:
        cur.execute(build_query)
    except Exception as e:
        print(e)
        return render_template('404.html')

    # rows = a list of 3-tuples (batch_number, submitted_at, nodes_used)
    rows = cur.fetchall()
    
    # Builds the JSON structure form the bottom up
    data = []
    if len(rows) > 0:
        for n,r in enumerate(rows):
            attributes = {
                'batch_number': r[0],
                'submitted_at': r[1] + '+00:00',
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
    return json_str

if __name__ == '__main__':
    app.run(debug=True)
