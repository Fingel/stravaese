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
	response = urllib2.urlopen(url)
	content = response.read()
	return "%s" % content
	
@app.route('/rides/<userid>')
def user_profile(userid):
	url = "".join(['http://www.strava.com/api/v1/rides?athleteId=',userid])
	response = urllib2.urlopen(url)
	content = response.read()
	return "%s" % content
	
@app.route('/post/<int:some_id>')
def adtwo(some_id):
	return 'Times 2 %d' % (2*some_id)

if __name__ == '__main__':
    app.run(debug=True)
