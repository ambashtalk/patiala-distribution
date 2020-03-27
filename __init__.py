from flask import Flask, render_template, request, url_for, request
#from dbconnect import Cursor

import pymysql
#import pandas as pd

def Cursor():
    db = pymysql.connect("remotemysql.com","P8fLcTUs68","JOx0xeTV8S","P8fLcTUs68",3306)
    cursor = db.cursor()
    return cursor

from math import radians, cos, sin, asin, sqrt 

def distance(lat1, lat2, lon1, lon2): 
	lon1 = radians(float(lon1)) 
	lon2 = radians(float(lon2)) 
	lat1 = radians(float(lat1)) 
	lat2 = radians(float(lat2)) 
	
	# Haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

	c = 2 * asin(sqrt(a)) 
	
	# Radius of earth in kilometers. Use 3956 for miles 
	r = 6371
	
	# calculate the result 
	return(c * r) 

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'somerandoxhex'
# app.config['template_auto_reload'] = 2
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title = 'Home')

@app.route('/Grocery', methods=['GET', 'POST'])
def grocery():
    cur = Cursor()
    msg = ""
    latitude = ""
    longitude = ""
    query = f'SELECT DISTINCT area FROM main ORDER BY area'
    cur.execute(query)
    areaList = [x for x, in cur.fetchall()]
    # print(areaList)
    shops = []
    if request.method == 'POST':
        area = request.form.get('area')
        # print(area)
        operation = request.form.get('fetch')
        # print(operation)
        if operation == 'search_area':
            query = f'SELECT shop, contact, area FROM main where category="Groceries" AND area="{area}"'
            cur.execute(query)
            shops = [(name,contact,area) for name,contact,area in cur.fetchall()]
        # elif operation == 'search_nearest':
        elif operation == 'search_nearest':
            #get nearest shops
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            if latitude == "" or longitude == "":
                msg = "Please click on 'Get My Location' first"
            else:
                query = 'SELECT shop, contact, area, lat, lon FROM main WHERE category="Groceries"'
                cur.execute(query)
                res = [(name,contact,area, distance(latitude, lat, longitude, lon)) for name,contact,area,lat,lon in cur.fetchall()]
                # threshold_radius = 0.7 #units in Kilometer
                res.sort(key=lambda x: x[3])
                shops = [(name,contact,area) for name,contact,area,dist in res[:5]]
                if shops == []:
                    msg = "NotFound"
                else:
                    msg = "Success"

            # print(latitude, longitude)
            # print("after Query")
            # print("after execute")
            # areaList = []
            
    cur.close()
    # print("before render")
    # print(shops)
    return render_template('grocery.html', title='Grocery Shops', areaList = areaList, shops=shops, latitude=latitude, longitude=longitude, msg=msg)

@app.route('/Milk_Dairy', methods=['GET', 'POST'])
def Milk_Dairy():
    return render_template('milk.html', title='Dairy Shops')

@app.route('/Chemist', methods=['GET', 'POST'])
def Chemist():
    return render_template('chemist.html', title='Chemist Shops')

if __name__ == '__main__':
    app.run(debug=True)