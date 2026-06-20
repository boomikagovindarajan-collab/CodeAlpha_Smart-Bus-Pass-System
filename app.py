from flask import Flask, render_template, request, redirect, session
import sqlite3
import random
import qrcode

app = Flask(__name__, static_folder="static")
app.secret_key = "buspass123"


# Create database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS passes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        source TEXT,
        destination TEXT,
        pass_type TEXT,
        price INTEGER,
        pass_id TEXT
    )
    ''')

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def test():
    return "Test Route Working"


@app.route("/check")
def check():
    return {
        "static_folder": app.static_folder,
        "template_folder": app.template_folder
    }


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = c.fetchone()

        conn.close()

        if user:
            session['username'] = user[1]
            return redirect('/dashboard')
        else:
            return "Invalid Email or Password"

    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':

        source = request.form['source']
        destination = request.form['destination']
        pass_type = request.form['pass_type']

        if pass_type == "Daily":
            price = 50
        elif pass_type == "Weekly":
            price = 250
        else:
            price = 800

        pass_id = "BP" + str(random.randint(1000, 9999))

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute(
            '''
            INSERT INTO passes
            (username, source, destination, pass_type, price, pass_id)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                session['username'],
                source,
                destination,
                pass_type,
                price,
                pass_id
            )
        )

        conn.commit()
        conn.close()

        return render_template(
            'dashboard.html',
            username=session['username'],
            booked=True,
            source=source,
            destination=destination,
            pass_type=pass_type,
            price=price,
            pass_id=pass_id
        )

    return render_template(
        'dashboard.html',
        username=session['username']
    )
@app.route('/book', methods=['GET', 'POST'])
def book():

    if request.method == 'POST':

        source = request.form['source']
        destination = request.form['destination']
        travel_date = request.form['travel_date']
        travel_time = request.form['travel_time']
        seat_no = request.form['seat_no']
        pass_type = request.form['pass_type']

        if pass_type == "Daily":
            price = 50
        elif pass_type == "Weekly":
            price = 250
        else:
            price = 800

        pass_id = "BP1234"

        qr_data = f"""
Pass ID: {pass_id}
User: {session['username']}
Source: {source}
Destination: {destination}
Type: {pass_type}
Price: ₹{price}
"""

        img = qrcode.make(qr_data)

        qr_path = f"static/{pass_id}.png"
        img.save(qr_path)

        return render_template(
            'book_pass.html',
            booked=True,
            source=source,
            destination=destination,
            travel_date=travel_date,
            travel_time=travel_time,
            seat_no=seat_no,
            pass_type=pass_type,
            price=price,
            pass_id=pass_id,
            qr_image=f"{pass_id}.png"
        )

    return render_template('book_pass.html', booked=False)

@app.route('/history')
def history():
    return render_template('booking_history.html')


@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect('/login')

    return render_template(
        'profile.html',
        username=session['username']
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)