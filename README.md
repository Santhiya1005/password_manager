Password Manager 🔐

A secure and user-friendly web-based Password Manager built with Flask, SQLite, and Python Cryptography.
It allows users to store, retrieve, and manage login credentials securely with encryption and a master authentication system.

📌 Features

Master Password Authentication – Secure access using a master password.

Add & Store Credentials – Save website, username, and password securely.

Encrypted Storage – Passwords encrypted using Fernet (symmetric encryption).

Unlock & View Passwords – Decrypt and view credentials temporarily after verification.

Session Management – Prevents unauthorized access.

Delete Credentials – Remove saved credentials securely.

Live Search – Search instantly for credentials like Google-type search (typeahead).

🛠️ Project Structure
Password-Manager/
│── static/                 # CSS, JavaScript files
│── templates/              # HTML templates
│   ├── index.html          # Dashboard / Home
│   ├── login.html          # Master password login page
│   ├── unlock.html         # Unlock credentials page
│   └── view.html           # View decrypted password
│── app.py                  # Flask application
│── generate_key.py         # Generate encryption key (secret.key)
│── passwords.db            # SQLite database
│── secret.key              # Fernet encryption key (DO NOT share)
│── README.md               # Documentation

🚀 Getting Started
1. Clone the repo
git clone https://github.com/yourusername/password-manager.git
cd password-manager

2. Install dependencies
pip install flask cryptography

3. Generate encryption key
python generate_key.py


This creates secret.key file used for encrypting/decrypting credentials.

4. Run the application
python app.py


The app runs on http://127.0.0.1:5000/
 by default.

🔎 Live Search (Typeahead)

The app supports Google-like live search where users can type a website/username and instantly see results.

Built with JavaScript debounce on the frontend.

Backend provides a /search API endpoint (Flask + SQLite).

Results update in real time.

⚠️ Security Notes

Keep secret.key safe (add it to .gitignore).

Master password should be hashed (e.g., bcrypt/argon2) instead of plain text.

Always run on HTTPS in production.

Database should not be exposed directly.

👩‍💻 Author

Santhiya Suresh
B.Tech AI & Data Science | Full Stack Developer | Python Enthusiast
