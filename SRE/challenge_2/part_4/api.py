#!/usr/bin/python

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests
from subprocess import Popen,PIPE
import subprocess
import json

app = Flask(__name__)
api = Api(app)

url = "https://hooks.slack.com/services/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"
token = "xoxp-796777290785-802751601940-791747080643-31861dc7a74e9db83f542934cfa31293"

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer {0}".format(token)
}

@app.route("/api/v1/query/report/<isocode>/<date>", methods=['GET'])

def report(isocode, date):
	process1 = subprocess.Popen(['bash', 'api1.sh',isocode, date], stdout=subprocess.PIPE)
	stdout1 = process1.communicate()[0]
	out = stdout1.decode("utf-8")
	out1 = out.strip("\n")
	out2 = out1.split(",")
	out3 = out2[3].strip()
	if 'out3' > '100':
		message = {
                	"channel": "#devops",
                	"text": isocode+","+out3
		}
		requests.post(url, headers=headers, data=json.dumps(message))
	return stdout1
if __name__ == '__main__':
     app.run()
