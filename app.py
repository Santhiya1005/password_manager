from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = "any_secret_key_for_session"

def load_key():
    return open("secret.key", "rb").read()

key = load_key()
fernet = Fernet(key)

def init_db():
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            website TEXT,
            username TEXT,
            password TEXT)
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    if 'user' not in session:
        return redirect('/unlock')

    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html", passwords=data)

@app.route("/add", methods=["POST"])
def add_password():
    website = request.form["website"]
    username = request.form["username"]
    password = request.form["password"]

    encrypted = fernet.encrypt(password.encode())

    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, encrypted.decode()))

    conn.commit()
    conn.close()

    return redirect("/")

@app.route('/unlock', methods=['GET', 'POST'])
def unlock():
    if request.method == 'POST':
        master_password = request.form['masterpassword']
        if master_password == 'admin123':
            session['user'] = master_password
            return redirect('/')
        else:
            return "Incorrect Master Password"
    return render_template('login.html')  # ✅ Shows login page on GET





@app.route('/view')
def view():
    if 'user' not in session:
        return redirect('/unlock')

    conn = sqlite3.connect('passwords.db')
    cur = conn.cursor()
    cur.execute("SELECT website, username, password FROM passwords")
    data = cur.fetchall()
    conn.close()

    decrypted_data = []
    for website, username, encrypted_password in data:
        try:
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        except:
            decrypted_password = "[Decryption Failed]"
        decrypted_data.append((website, username, decrypted_password))

    return render_template("view.html", passwords=decrypted_data)

@app.route("/decrypt", methods=["POST"])
def decrypt_password():
    data = request.get_json()
    row_id = data.get("id")
    username_input = data.get("username")
    master_input = data.get("master")

    if master_input != "admin123":
        return jsonify({"success": False, "message": "Incorrect master password"})

    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("SELECT username, password FROM passwords WHERE id=?", (row_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return jsonify({"success": False, "message": "Password entry not found"})

    db_username, encrypted = row

    if db_username != username_input:
        return jsonify({"success": False, "message": "Incorrect username"})

    try:
        if isinstance(encrypted, str):
            if encrypted.startswith("b'") or encrypted.startswith('b"'):
                encrypted = eval(encrypted)
            else:
                encrypted = encrypted.encode()

        decrypted = fernet.decrypt(encrypted).decode()

    except:
        return jsonify({"success": False, "message": "Decryption failed"})

    return jsonify({"success": True, "password": decrypted})

@app.route("/delete/<int:id>", methods=["POST"])
def delete_password(id):
    conn = sqlite3.connect("passwords.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM passwords WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/unlock")

if __name__ == "__main__":
    app.run(debug=True)
