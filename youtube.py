from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/search/<queryStr>")
def search(queryStr):
	xml = requests.get('http://gdata.youtube.com/feeds/api/videos?q=' + queryStr + '&orderby=published&start-index=11&max-results=10&v=2')
	return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    app.run()