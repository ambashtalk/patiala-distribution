from flask import Flask, render_template, request, url_for, request
from dbconnect import Cursor

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'somerandoxhex'
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title = 'Home')

@app.route('/Grocery', methods=['GET', 'POST'])
def grocery():
    cur = Cursor()
    query = f'SELECT DISTINCT area FROM main'
    cur.execute(query)
    areaList = [x for x, in cur.fetchall()]
    # print(areaList)
    shops = []
    operation = request.form.get('fetch')
    print(operation)
    area = request.form.get('area')
    print(area)
    if operation == 'search_nearest':
        #get nearest shops
        query = 'SELECT shop, contact, area, category FROM main'
        cur.execute(query)
        shops = [(name,contact,area,category) for name,contact,area,category in cur.fetchall()]
        pass
    elif operation == 'search_area':
        query = f'SELECT shop, contact, area, category FROM main where area={area}'
        cur.execute(query)
        shops = [(name,contact,area,category) for name,contact,area,category in cur.fetchall()]
        pass
    cur.close()
    return render_template('grocery.html', title='Grocery Shops', areaList = areaList, shops=shops)

@app.route('/Milk_Dairy', methods=['GET', 'POST'])
def Milk_Dairy():
    return render_template('milk.html', title='Dairy Shops')

@app.route('/Chemist', methods=['GET', 'POST'])
def Chemist():
    return render_template('chemist.html', title='Chemist Shops')

if __name__ == '__main__':
    app.run(debug=True)