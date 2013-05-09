from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import urllib2
import json

app = Flask(__name__)
#might need psycopg2
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:devpass@127.0.0.1/sese'
db = SQLAlchemy(app)


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
	
@app.route('/dbtest')
def db_test():
	segments = Segment.query.all()
	return "%s" % segments

def getServerData(url):
	response = urllib2.urlopen(url)
	return response.read()

#Models

class Segment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sid = db.Column(db.Integer, unique=True)
	rating = db.Column(db.Integer)
	
	def __init__(self, sid, rating):
		self.sid = sid
		self.rating = rating
	
	def __repr__(self):
		return 'sid: %d' % self.sid
	
	

if __name__ == '__main__':
    app.run(debug=True)
