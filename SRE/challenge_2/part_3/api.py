#!/usr/bin/python

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import re
from collections import Counter
from subprocess import Popen,PIPE
import subprocess
import json

app = Flask(__name__)
api = Api(app)

@app.route("/api/v1/query/count/<isocode>/<date>", methods=['GET'])


def count(isocode, date):
	process = subprocess.Popen(['bash', 'api.sh', isocode, date], stdout=subprocess.PIPE)
	stdout = process.communicate()[0] 
	return stdout
	
		

@app.route("/api/v1/query/report/<isocode>/<date>", methods=['GET'])

def report(isocode, date):
	process1 = subprocess.Popen(['bash', 'api1.sh', isocode, date], stdout=subprocess.PIPE)
	stdout1 = process1.communicate()[0]
	return stdout1


if __name__ == '__main__':
     app.run()
