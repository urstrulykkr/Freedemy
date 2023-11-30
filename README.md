# Freedemy
Freedemy is an open-source, free online skill learning platform built using Django, HTML5, CSS3, and SQLite.
Installation:

git clone https://github.com/pothuguntaumesh/Freedemy.git
cd Freedemy

Set up a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip3 install -r requirements.txt

Database Setup
Create a new database and user in your preferred database system.

Run database migrations:
python3 manage.py makemigrations
python3 manage.py migrate

Update the database configuration in settings.py with your database details.

Run the Development Server
Start the development server.
python 3 manage.py runserver


Access Admin Interface
If you've created a superuser using:
python3 manage.py createsuperuser

Testing
To run unit tests:
python3 manage.py test

