from flask import Flask, render_template, request, url_for, request

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'somerandoxhex'
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title = 'Home')

@app.route('/Grocery', methods=['GET', 'POST'])
def grocery():
    areaList = ['Area 1', 'Area 2', 'Area 3', 'Area 4'] # from SQL QUERY for area
    shops = []
    operation = request.form.get('fetch')
    area = request.form.get('area')
    if operation == 'search_nearest':
        #get nearest shops
        shops = [('Name','Contact', 'Address'), ('Tuple', 'of', 'shop_details')] # from SQL query get nearest shops and send all details
        pass
    elif operation == 'search_area':
        #get shows in the area specified
        shops = [('Name','Contact', 'Address'), ('Tuple', 'of', 'shop_details')] # from SQL query get nearest shops and send all details
        pass
    return render_template('grocery.html', title='Grocery Shops', areaList = areaList, shops=shops)

@app.route('/Milk_Dairy', methods=['GET', 'POST'])
def Milk_Dairy():
    return render_template('milk.html', title='Dairy Shops')

@app.route('/Chemist', methods=['GET', 'POST'])
def Chemist():
    return render_template('chemist.html', title='Chemist Shops')

if __name__ == '__main__':
    app.run(debug=True)