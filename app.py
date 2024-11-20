from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('baking_info.db')
    curr = conn.cursor()


#Create the Baking_Info table
    curr.execute('''
    CREATE TABLE IF NOT EXISTS Baking_Info(
        entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        Name TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Phone_Number TEXT NOT NULL,
        Security_Level INTEGER NOT NULL,
        Login_Password TEXT NOT NULL
    )
    ''')
    conn.commit()  # Commit changes
    conn.close()


@app.route('/')  #first page
def home():
    return render_template('home.html')

@app.route('/tableview')
def list():
    return render_template('list.html')

@app.route('/add_baker', methods=['GET', 'POST'])
def add_baker():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('Name', '').strip()
        age = request.form.get('Age', '').strip()
        phone_number = request.form.get('PhoneNumber', '').strip()
        security_level = request.form.get('SecurityLevel', '').strip()
        password = request.form.get('Password', '').strip()


        errors = False
        if not name:
            flash("You cannot enter an empty name.")
            errors = True
        
        if not phone_number:
            flash("You cannot enter an empty phone number")
            errors = True
        
        if not age.isdigit() or not (0 < int(age) < 121):
            flash("The age must be a whole number greater than 0 and less than 121.")
            errors = True
        
        if not security_level.isdigit() or int(security_level) not in [1,2,3]:
            flash("The SecurityLevel must be a numeric value between 1 and 3")
            errors = True
        
        if not password:
            flash("You cannot enter an empty password")
            errors = True

        if errors:
            return redirect(url_for('add_baker'))
        
        conn = sqlite3.connect('baking_info.db')
        curr = conn.cursor()
        curr.execute('''
            INSERT INTO Baking_Info (user_id, Name, Age, Phone_Number, Security_Level, Login_Password)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (1, name, int(age), phone_number, int(security_level), password))  # Replace 1 with appropriate user_id logic
        conn.commit()
        conn.close()

        return render_template('success.html', message="Record successfully added")

    return render_template('add_baker.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

