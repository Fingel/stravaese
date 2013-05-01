from flask import Flask, render_template
import urllib2
import json
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ride/<ride>')
def get_ride(ride):
	url = "".join(['http://www.strava.com/api/v2/rides/',ride,'/map_details?token=e8cf53eee7a51d8bef8c&threshold=100'])
	response = urllib2.urlopen(url)
	content = response.read()
	return "%s" % content
	
@app.route('/usr/<username>')
def user_profile(username):
	return 'User %s' % username
	
@app.route('/post/<int:some_id>')
def adtwo(some_id):
	return 'Times 2 %d' % (2*some_id)

if __name__ == '__main__':
    app.run(debug=True)
