from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')  #first page
def home():
    return render_template('home.html')

@app.route('/tableview')
def list():
    return render_template('list.html')

@app.route('/add_baker')
def add_baker():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('Name', '').strip()
        age = request.form.get('Age', '').strip()
        phone_number = request.form.get('PhoneNumber', '').strip()
        security_level = request.form.get('SecurityLevel', '').strip()
        password = request.form.get('Password', '').strip()

    return render_template('add_baker.html')

if __name__ == '__main__':
    app.run(debug=True)

