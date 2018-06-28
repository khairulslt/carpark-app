from flask import Flask, render_template, request
from flask import jsonify
import requests
import json
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def main():
	if request.method == 'POST':
		data = request.form["Carpark"] # var data used to access input form value directly
		response = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
		jack = response.json()
		daniel = jack['items'][0]["carpark_data"]
		for d in daniel: 								# run loop to obtain carpark info corresponding to input form
			if d["carpark_number"] == data:
				return render_template("echo.html", text=d["carpark_info"], data=data) # passing variables text & data to "echo.html"
	else:
		return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)