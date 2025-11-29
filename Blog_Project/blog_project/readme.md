InkSpace – Minimal Django Blog
--------------------------------
InkSpace is a clean and modern blogging platform built with Django.
It includes posts, tags, comments, likes, a user dashboard, and a simple minimal UI.

Features
-----------
Create, edit, delete posts

Draft/Published status

Featured images (ImageField + Pillow)

Tag system (django-taggit)

Search by title/content

Pagination

Comments (login required)

Like/unlike posts

User dashboard with author-only permissions

Custom template tag: recent posts

Minimal responsive layout with a unified base.html

Tech
-------
Django

SQLite (default)

Pillow

django-taggit

Setup
-----------
git clone https://github.com/yourusername/inkspace.git
cd inkspace

python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Visit:

http://127.0.0.1:8000/

Usage
--------
Main pages:

/ — Blog home

/post/<slug>/ — Post detail

/dashboard/ — User’s posts

/post/new/ — Create post

/tag/<tag>/ — Posts by tag

/accounts/login/ — Login

/accounts/signup/ — Register

Project Structure
--------------------
blogproject/
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/blog/
│   └── templatetags/
├── templates/
├── media/
└── manage.py

Requirements
---------------
Minimum:

Django
Pillow
django-taggit

Install Dependencies, Make sure your virtual environment is activated, then run:

pip install -r requirements.txt

