from flask import Flask, render_template, request, url_for, request
from dbconnect import Cursor

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
            query = f'SELECT shop, contact, area FROM main where area="{area}"'
            cur.execute(query)
            shops = [(name,contact,area) for name,contact,area in cur.fetchall()]
        # elif operation == 'search_nearest':
        elif operation == 'search_nearest':
            #get nearest shops
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            if latitude == "" or longitude == "":
                msg = 'Please click on "Get my location" first'
            else:
                query = 'SELECT shop, contact, area FROM main'
                cur.execute(query)
                shops = [(name,contact,area) for name,contact,area in cur.fetchall()]

            print(latitude, longitude)
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