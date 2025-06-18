# Password Manager
A secure and user-friendly web-based Password Manager built using Flask, SQLite, and Python Cryptography. This application allows users to store, retrieve, and manage login credentials securely using encryption and a master authentication system.

# Features
* Master Password Authentication - Access to the app is protected with a master password.
* Add Credentials - Store website login details including website name, username, and password.
* Encrypted Storage - Passwords are encrypted using Fernet symmetric encryption before being saved.
* View Passwords on Request - Passwords are revealed temporarily after verifying the master password and username. The fuction will run for 10 secs defaulty to decrpt the password using node.js.
* Live Search - Instantly search for entries based on website or username.
* Delete Entries - Remove stored credentials easily and securely.
* Session-Based Access Control - Prevents unauthorized access through session management.

# Technologies Used
Frontend: HTML5, CSS3, JavaScript  
Backend: Python (Flask Framework)  
Database: SQLite  
Encryption: Fernet (from `cryptography` library)

# Getting Started
1.https://github.com/yourusername/password-manager.git
2.pip install flask cryptography
3. Generate Encryption Key (Only once)
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("secret.key", "wb") as f:
    f.write(key)

4.python app.py - Run the application in local host.

**Author**
Santhiya Suresh
B.Tech AI & Data Science | Full Stack Developer | Python Enthusiast
GitHub: Santhiya1005 | Email: sureshsanthiya613@gmail.com
