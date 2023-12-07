
# Freedemy

Freedemy is a free online skill learning platform built using Django, HTML5 and CSS3, SQLite.
## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Run the Development Server](#run-the-development-server)
- [Access Admin Interface](#access-admin-interface)
- [Testing](#testing)


## Prerequisites

Ensure you have the following installed on your machine:

- **Python and pip**: [Download Python](https://www.python.org/downloads/)
- **Virtual Environment (optional but recommended)**
- **Git**: `sudo apt-get install git` (On Debian/Ubuntu) 

## Installation

```bash
git clone https://github.com/pothuguntaumesh/Freedemy.git
cd Freedemy``

`python3 -m venv venv`
`source venv/bin/activate`
`pip3 install -r requirements.txt`


## Database Setup

1. Create a new database and user in your preferred database system.
`python3 manage.py makemigrations`
`python3 manage.py migrate`

`DATABASES` configuration with your database details.

## Run the Development Server

`python3 manage.py migrate`
`python3 manage.py runserver`

# Access Admin Interface

If you created a superuser using
`python3 manage.py createsuperuser`
you can access the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Testing

To run the unit tests:
`python3 manage.py test
`
