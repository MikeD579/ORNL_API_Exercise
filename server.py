from flask import Flask, jsonify, request, url_for
import sqlite3
app = Flask(__name__)

# Builds the query and formats response to get ready to jsonify
def query(filters):
    con = sqlite3.connect('batch_jobs.db')
    cur = con.cursor()

    build_query = ' SELECT * FROM batch WHERE 1'

    for key in filters:
        # delet later
        print(key, filters[key])
        if key == 'filter[submitted_after]':
            build_query += ' AND submitted_at >= ' + filters[key]
        elif key == 'filter[submitted_before]':
            build_query += ' AND submitted_at <= ' + filters[key]
        elif key == 'filter[min_nodes]':
            build_query += ' AND nodes_used >= ' + filters[key]
        elif key == 'filter[max_nodes]':
            build_query += ' AND nodes_used <= ' + filters[key]
        else:
            return ('Something has gone wrong. I cannot filter ' + key)
    build_query += ';'
    cur.execute(build_query)
    # Returns a list of n-tuples, in our case a 3-tuple (batch #, datetime, nodes)
    rows = cur.fetchall()
    
    # Creating a dictionary to return
    data = []
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

    con.close()
    return data

def format_json(data):
    links = {
        'self': request.url,
    }
    
    json_str = {
        'links': links,
        'data': data
    }

    return json_str
    

@app.route('/batch_jobs/')
def batch_jobs():
    # The dictionary that will be built and converted as a JSON
    # request.args returns a dictionary with the form filters
    # query will return a list a dictionary with the values for the JSON data field
    data = query(request.args)
    return jsonify(format_json(data))
    #return complete_json 
    #jsonify({"links": { "self": "http://localhost:5000/batch_jobs"}})

if __name__ == '__main__':
    app.run(debug=True)
