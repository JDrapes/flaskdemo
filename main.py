#Add imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pandas as pd
#Current file
app = Flask(__name__)
Bootstrap(app)
#When user goes to default page then below function activates
@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/classifiedData")
def classifiedData():
	return render_template("classifiedData.html")
	
@app.route("/allMACData")
def allMACData():
	df = pd.read_csv("/home/pi/DSP/godsEye/collatedBroadcasts.csv")
	return render_template("allMACData.html", tables=[df.to_html(classes='table table-striped" id = "myTable', header="true")])
		

if __name__ == "__main__":
	app.run(debug=True)
