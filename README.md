# Carpark.py


### Introduction

* Obtain number of Carpark Lots Available from any carpark in Singapore 
* Uses API from https://api.data.gov.sg/v1/transport/carpark-availability 


### What You Need
* Python 3:

```
https://www.python.org/downloads/
```
* [Pip](https://pip.pypa.io/en/stable/quickstart/) if you're on a fresh Python install and need the libraries below
* Requests (Python Module)

```
pip install requests
```
* Flask (Python Web App Framework)

```
pip install -U Flask
```

### How To Run
* Open up your terminal
* cd into the directory you extracted/cloned this program into
* e.g: With Terminal open, this should be how your first line looks like

```
cd C:\users\user\Desktop\EXAMPLEFOLDER
```
* Now all you need to do is type in the following:
```
python Carpark.py
```
* Go to https://localhost:5000 in your browser
* Enter your respective carpark numbers / addresses
* ~~Should probably use in conjunction with https://data.gov.sg/dataset/hdb-carpark-information to find desired carpark No. ~~


## Built With

* Python
* Flask


## Authors

Khaislt

## Final Notes:
* Finally integrated second API onto app, it finds your carpark number based on an address given
* (Still in works, need to add more styling, also needs to return an error in a jinja template if address does not return successfully*
* Priority is trying to get it deployed on my remote Nginx Server
* Need to work on transitioning it into a full-fledged Web App with Google Maps Accessibility ~~and an easier way to find your desired Carpark No without referring to another site.~~


