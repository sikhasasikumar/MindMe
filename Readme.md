# MindMe
A reminder web application built using **Python-Django**. 

**SQLite** is the database used in the web app.

The tables in the database can be seen in the `reminder/models.py`. I have used a single table for storing reminder with fields, `title`,
`description`, `date` (stores both date and time). The primary key `id` is managed by Django itself.

**Bootstrap4** is used for styling the HTML templates for the views. 

## Installation and Setup

Install the requirements.

`pip install -r requirements.txt`

Do the Database migrations

`python manage.py makemigrations`

`python manage.py migrate`

Run the development server using

`python manage.py runserver`

Access the web app in the URL: 

`http://127.0.0.1:8000`

The index page will display the list of all reminders. You can create a new reminder by clicking on the **New Reminder** button.