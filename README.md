## 🔐 Password Manager

A secure and user-friendly web-based Password Manager built with Flask, SQLite, and Python Cryptography.
It allows users to store, retrieve, and manage login credentials securely with encryption and a master authentication system.

## Features

* Master Password Authentication – Secure access using a master password.
* Add & Store Credentials – Save website, username, and password securely.
* Encrypted Storage – Passwords encrypted using Fernet (symmetric encryption).
* Unlock & View Passwords – Decrypt and view credentials temporarily after verification.
* Session Management – Prevents unauthorized access.
* Delete Credentials – Remove saved credentials securely.
* Live Search (Typeahead) – Instant search for credentials like Google search.

## Project Structure
Password-Manager/
│── static/                 
│── templates/              
│   ├── index.html        
│   ├── login.html        
│   ├── unlock.html        
│   └── view.html          
│── app.py                  
│── generate_key.py        
│── passwords.db           
│── secret.key             
│── README.md              
│── requirements.txt      

## Getting Started
1. Clone the repository
git clone https://github.com/Santhiya1005/password_manager.git
cd password_manager

2. Install dependencies
pip install -r requirements.txt

3. Generate encryption key
python generate_key.py
This creates secret.key used for encrypting/decrypting credentials.

4. Run the application
python app.py
The app runs on http://127.0.0.1:5000/   by default.

## ----------------------------------------------------------------------------------------------------------------------------------
Demo Access - You can try the app using the demo master password:
Mater Password: admin123 
Note: This is only for demo purposes. For real usage, set your own secure master password.
-------------------------------------------------------------------------------------------------------------------------------------

## Live Search (Typeahead)

* Google-like instant search for website/username.
* Built with JavaScript debounce on the frontend.
* Backend provides a /search API endpoint (Flask + SQLite).
* Results update in real time.

## Security Notes

* Keep secret.key safe (add it to .gitignore).
* Master password should ideally be hashed with bcrypt or argon2.
* Always run the app over HTTPS in production.
* The database (passwords.db) should not be exposed directly.

## ----------------------------------------------------------------------------------------------------------------------------------
## Live Demo
https://passwordmanager-6plj.onrender.com
## ----------------------------------------------------------------------------------------------------------------------------------

## Technologies Used

* Python 3.13
* Flask 3.1
* SQLite
* Python Cryptography (Fernet)

HTML, CSS, JavaScript

Gunicorn (Deployment)

