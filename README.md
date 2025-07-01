# Flask Blog Application

This is a **Flask-based Blog Web Application** that provides user authentication, CRUD functionality for posts, profile management with image uploads, and password reset via email.

## 🚀 Features

- User registration and login.
- Password hashing using Bcrypt.
- User profile update with profile picture upload.
- CRUD (Create, Read, Update, Delete) operations for blog posts.
- Password reset via email with token-based verification.
- Custom error handling for 403, 404, and 500 errors.
- Pagination for posts display.
- Email integration using Flask-Mail.
- Form validation using Flask-WTF.

## 🛠 Technologies Used

- Python
- Flask
- Flask-Login
- Flask-Mail
- Flask-Bcrypt
- SQLite (SQLAlchemy ORM)
- HTML/CSS (Jinja2 templates)

## 📂 Project Structure

project/
│
├── frist/ # Application package
│ ├── templates/ # HTML templates
│ ├── **init**.py # Flask app setup
│ ├── form.py # Forms and validations
│ ├── models.py # Database models
│ ├── posts.json
│ └── routes.py # Application routes
│
├── Include/
├── instance/
├── Lib/
├── Scripts/
├── pyvenv.cfg
├── .gitignore
├── README.md
├── requirements.txt
└── run.py # Entry point

🏃‍♂️ Run Locally
Clone the project:
```bash
git clone https://github.com/mopharaoh/Flaskblog.git
```
Navigate to the project directory:
```bash
cd Flaskblog
```
Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
```bash
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Linux/macOS
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the app:
```bash
python run.py
```