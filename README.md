# 🗳️ Voting System (Django Project)

This is a Django-based Voting System where users can participate in polls. 
It consists of multiple apps, including `polls` for poll management and `pages` for static content.

✨ Features
Create, update, and delete polls

Vote on available questions

See poll results

Simple and clean UI using Django templates
## 📁 Project Structure

pollster_project/
├── pages/ # Static and informational pages
├── polls/ # Polls application (voting logic)
├── pollster/ # Main Django project settings
├── templates/ # Shared HTML templates
├── db.sqlite3 # SQLite database file
└── manage.py # Django's command-line utility


## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/paras-bista/Voting_System.git
cd Voting_System

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies
pip install django

5. Run Migrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver
Then open your browser and go to: http://127.0.0.1:8000/



🛠️ Tech Stack
Backend: Django (Python)

Database: SQLite

Frontend: HTML/CSS (Django Templates)

📂 Future Improvements
Add user authentication (login/register)

Restrict multiple voting

Real-time results using AJAX or WebSockets

Admin dashboard for managing polls

📄 License
This project is open-source and available under the MIT License.
