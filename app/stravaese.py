from flask import Flask, render_template
import urllib2
import json
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ride/<ride>')
def get_ride(ride):
	url = "".join(['http://app.strava.com/api/v1/streams/',ride])
	return "%s" % getServerData(url)
	
@app.route('/ride/details/<ride>')
def get_ride_details(ride):
	url = "".join(['http://www.strava.com/api/v2/rides/',ride])
	return "%s" % getServerData(url)
	
@app.route('/rides/<userid>/<offset>')
def user_profile(userid, offset):
	url = "".join(['http://www.strava.com/api/v1/rides?athleteId=',userid,'&offset=',offset])
	return "%s" % getServerData(url)

def getServerData(url):
	response = urllib2.urlopen(url)
	return response.read()

@app.route('/post/<int:some_id>')
def adtwo(some_id):
	return 'Times 2 %d' % (2*some_id)

if __name__ == '__main__':
    app.run(debug=True)
