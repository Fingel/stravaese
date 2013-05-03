from flask import Flask, render_template
import urllib2
import json
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/ride/<ride>')
def ride(ride):
	details = get_ride_details(ride)
	ride_data = json.loads(details)
	ride_details = ride_data['ride']
	
	segments = get_ride_segments(ride)
	segment_data = json.loads(segments)
	segment_list = segment_data['efforts']
	return render_template('ride.html', ride=ride_details, segment_list=segment_list)

@app.route('/ride/<ride>/path/')
def get_ride(ride):
	url = "".join(['http://app.strava.com/api/v1/streams/',ride])
	return "%s" % getServerData(url)
	
@app.route('/ride/<ride>/details')
def get_ride_details(ride):
	url = "".join(['http://www.strava.com/api/v2/rides/',ride])
	return "%s" % getServerData(url)

@app.route('/ride/<ride>/segments')
def get_ride_segments(ride):
	url = "".join(['http://www.strava.com/api/v2/rides/',ride,'/efforts'])
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
