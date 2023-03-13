#!python3

import os
import json
import psycopg2
from urllib.parse import urlparse

from flask import Flask, request, abort
from flask_restful import Resource, Api
from flask_restful import reqparse


# Base Shared Connection.
app = Flask(__name__)
api = Api(app)


pg_url = ""

def _db(pg_url):
    url_parsed = urlparse(pg_url)
    username = url_parsed.username
    password = url_parsed.password
    database = url_parsed.path[1:]
    hostname = url_parsed.hostname
    port = url_parsed.port
    connection = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    )
    return connection

def db():
    global pg_url
    return _db(pg_url)

def query_db_json(query, args=(), one=False):
    cur = db().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    res = (r[0] if r else None) if one else r
    return json.dumps(res)

class QueryToPgSQL(Resource):
  def post(self):
    res = {}
    if 'query' in request.form:
        res = query_db_json(request.form['query'])
    elif 'q' in request.form:
        res = query_db_json(request.form['q'])
    return res

api.add_resource(QueryToPgSQL, '/query')
#api.add_resource(QueryToPgSQL, '/q')


if __name__ == '__main__':
    os.system("steampipe service status --show-password | grep Connection | awk '{print $3}' > /tmp/pwds")
    pg_url = open('/tmp/pwds','r').read().strip()
    app.run(host='0.0.0.0', debug=True)

