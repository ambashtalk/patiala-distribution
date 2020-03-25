from flask import Flask, render_template, request, url_for

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'somerandoxhex'
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title = 'Home')

@app.route('/Grocery', methods=['GET', 'POST'])
def grocery():
    return render_template('grocery.html', title='Grocery Shops')

@app.route('/Milk_Dairy', methods=['GET', 'POST'])
def Milk_Dairy():
    return render_template('milk.html', title='Dairy Shops')

@app.route('/Chemist', methods=['GET', 'POST'])
def Chemist():
    return render_template('chemist.html', title='Chemist Shops')

if __name__ == '__main__':
    app.run(debug=True)