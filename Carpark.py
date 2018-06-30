from flask import Flask, render_template, request
from flask import jsonify
import requests
import json
app = Flask(__name__)

# to find carpark number corresponding to address
@app.route('/')
def address():
	return render_template("address.html")

# to find carpark number corresponding to address
@app.route('/address',methods = ['POST', 'GET'])
def address1():
	if request.method == 'POST':
		desired_CP_Address = request.form["address"]

		response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&q=" + desired_CP_Address)
		jack = response.json()
		jack1 = jack['result']['records']
		return render_template("address1.html", text=jack1)

# to find lot availability corresponding to carpark number
@app.route('/lotfinder',methods = ['POST', 'GET'])
def car1():
	if request.method == 'GET':
		return render_template("car1.html")

# to find lot availability corresponding to carpark number
@app.route('/carpark',methods = ['POST', 'GET'])
def car2():
	if request.method == 'POST':

		# DO CODE FOR CARPARK AVAILABILITY CORRESPONDING TO CARPARK NUMBER 
		desired_CP_Number = request.form["Carpark"] # IMPORTANT! desired_CP_Number == retrieval of form value from "index.html"

		carparkApi = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
		carparkJson = carparkApi.json()
		CP_Data = carparkJson['items'][0]["carpark_data"]

		for x in CP_Data: 								# run loop to obtain carpark info corresponding to input form
			if x["carpark_number"] == desired_CP_Number:
				car1 = x["carpark_info"]
				return render_template("car2.html", text=x["carpark_info"], data=desired_CP_Number) # passing variables text & data to "echo.html"


if __name__ == '__main__':
    app.run(debug = True)