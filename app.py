from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  #first page
def home():
    return render_template('home.html')

@app.route('/tableview')
def list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)

