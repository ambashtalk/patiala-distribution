from flask import Flask, render_template, request, url_for

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'somerandoxhex'
@app.route('/', methods=['GET', 'PSOT'])
@app.route('/home', methods=['GET', 'PSOT'])
def home():
    return render_template('index.html', title = 'Home')
    # return "Hello"


if __name__ == '__main__':
    app.run(debug=True)