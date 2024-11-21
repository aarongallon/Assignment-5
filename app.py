from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('./baking_info.db')
    curr = conn.cursor()


#Create the Baking_Info table
    curr.execute('''
    CREATE TABLE IF NOT EXISTS Baking_Info(
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

@app.route('/add_baker', methods=['GET', 'POST'])
def add_baker():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('Name', '').strip()
        age = request.form.get('Age', '').strip()
        phone_number = request.form.get('PhoneNumber', '').strip()
        security_level = request.form.get('SecurityLevel', '').strip()
        password = request.form.get('Password', '').strip()
        print("name, age, phone, sec, password")
        print(f"{name}, {age}, {phone_number}, {security_level}, {password}")


        errors = False
        if not name:
            print("64")
            flash("You cannot enter an empty name.")
            errors = True
        
        if not phone_number:
            print("69")
            flash("You cannot enter an empty phone number")
            errors = True
        
        if not age.isdigit() or not (0 < int(age) < 121):
            print("74")
            flash("The age must be a whole number greater than 0 and less than 121.")
            errors = True
        
        if not security_level.isdigit() or int(security_level) not in [1,2,3]:
            print("79")
            flash("The SecurityLevel must be a numeric value between 1 and 3")
            errors = True
        
        if not password:
            print("84")
            flash("You cannot enter an empty password")
            errors = True

        if errors:
            print("89")
            return redirect(url_for('success'))
        
        conn = sqlite3.connect('./baking_info.db')
        curr = conn.cursor()
        curr.execute('''
            INSERT INTO Baking_info (Name, Age, Phone_Number, Security_Level, Login_Password)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, int(age), phone_number, int(security_level), password)) 
        conn.commit()
        conn.close()
        flash("Record Successfully added")
        return render_template('success.html')

    return render_template('add_baker.html')

@app.route('/success')
def success():
    return render_template('success.html')

def get_users_list():
    conn = sqlite3.connect('./baking_info.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name, Age, Phone_Number, Security_Level, Login_Password FROM Baking_Info")
    users = cursor.fetchall()
    conn.close()
    return users
    
@app.route('/tableview')
def list():
    users = get_users_list()
    print(users)
    print("HELLOLOKOKOFODFODOFDOFODO")
    return render_template('list.html', users=users)

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

