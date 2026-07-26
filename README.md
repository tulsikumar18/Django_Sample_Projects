# Django Sample Projects Collection

![Status](https://img.shields.io/badge/status-Demo%20Collection-yellow)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Project Overview

This repository is a curated collection of Django sample applications and learning projects. It demonstrates core Django concepts such as templating, form handling, model-based views, static file management, multi-page navigation, and simple database integration.

The collection is intended for learners, instructors, and developers who want to review working Django examples or use them as a starting point for new applications.

### Target Users

- Django beginners learning project structure and routing
- Students studying Python web development
- Developers reviewing examples for templates, forms, and models
- Instructors building teaching materials around Django basics

### Key Objectives

- Show small, self-contained Django applications
- Demonstrate basic CRUD display patterns with templates
- Illustrate how Django handles forms and POST data
- Provide examples for static files and image serving
- Highlight both SQLite and MySQL configuration examples

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Requirements Installation](#requirements-installation)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [Admin Panel](#admin-panel)
- [API Documentation](#api-documentation)
- [Screenshots Section](#screenshots-section)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- ✅ Multiple example Django projects in one workspace
- ✅ Calculator forms with POST handling and result rendering
- ✅ Multi-page navigation using simple view functions
- ✅ Django form rendering with `forms.Form`
- ✅ Model-driven pages using the Django ORM
- ✅ Static file setup for CSS and images
- ✅ Template loops, conditionals, and context data
- ✅ SQLite database examples for most projects
- ✅ MySQL integration example in `internaldb`
- ✅ Admin interface available in many projects

---

## Tech Stack

- Python
- Django 6.0.x
- SQLite
- MySQL (in `internaldb` project)
- HTML
- CSS
- Bootstrap (used in `formsproj`)
- Django Template Language (DTL)

---

## Project Structure

The root workspace contains several sample Django projects and related assets.

```text
Django/
  calci/myproj/          # Calculator sample app
  modelpro/              # Model project skeleton with car model
  myproj1/               # Multi-page template demo
  myproject1/            # Single display page demo
Djangoproj/
  myproj1/               # Minimal admin-only Django project
formsproj/               # Django form rendering demo
internaldb/              # MySQL-backed student model demo
multipleHtml/htmlproj/   # Multiple HTML pages and calculator example
staticFile/staticproj/   # Static CSS + image serving demo
venv/                    # Local virtual environment (ignore in Git)
```

### Important folders

- `templates/`: shared project templates in some root projects
- `static/`: sample static assets for static file demos
- `manage.py`: Django command-line entrypoint for each project
- `db.sqlite3`: sample SQLite databases used by demo apps

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Django
```

2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

If a `requirements.txt` file is added later, use:

```bash
pip install -r requirements.txt
```

Otherwise install Django manually:

```bash
pip install Django==6.0.7
```

4. Choose a project folder and run migrations

Example for `formsproj`:

```bash
cd formsproj
python manage.py migrate
```

---

## Requirements Installation

There is no `requirements.txt` file detected in this workspace at the moment. For new installs, use:

```bash
pip install Django==6.0.7
```

If you add a `requirements.txt` file, install dependencies with:

```bash
pip install -r requirements.txt
```

For the `internaldb` MySQL example, also install a MySQL client package:

```bash
pip install mysqlclient
```

---

## Environment Variables

This workspace currently uses hard-coded settings in each project. For production use, move sensitive values into a `.env` file and update project settings accordingly.

Example `.env` file:

```env
DJANGO_SECRET_KEY=replace-with-your-secret-key
DEBUG=True
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

> Note: The `internaldb` project currently uses MySQL with the following connection pattern in `internaldb/internaldb/settings.py`:
> `ENGINE=django.db.backends.mysql`, `NAME=djangodb`, `USER=root`, `PASSWORD`, `HOST=localhost`, `PORT=3306`

---

## Database Setup

Each project uses Django migrations to build its database schema.

Run from the chosen project directory:

```bash
python manage.py makemigrations
python manage.py migrate
```

For projects using SQLite, the database file is created automatically. For `internaldb`, ensure MySQL is installed, running, and the configured database exists.

---

## Running the Project

Start the Django development server from the selected project folder:

```bash
cd formsproj
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

If you switch to another sample project, change into its folder and run the same command.

---

## Admin Panel

Most sample projects include Django admin support via `django.contrib.admin`.

Create a superuser in the chosen project:

```bash
python manage.py createsuperuser
```

Then visit:

```text
http://127.0.0.1:8000/admin/
```

---

## API Documentation

No Django REST Framework or REST API endpoints were detected in this workspace.

This repository focuses on standard Django views, templates, forms, and ORM-based rendering.


## Future Improvements

- Add a central `requirements.txt` file for reproducible installs
- Move environment-specific values to `.env` and use `python-decouple` or `django-environ`
- Expand the `internaldb` project with CRUD operations and admin customization
- Add Django REST Framework endpoints for API examples
- Add automated tests for views, forms, and models
- Introduce Docker / Docker Compose for local project setup
- Standardize project names and consolidate example apps
- Add README notes inside each sample project directory

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes with clear messages
4. Open a pull request describing your changes
5. Keep code style consistent and use the Django template patterns already present

Please avoid committing local virtual environments, database files, or editor-specific config files.

---

## License

This project is available under the MIT License. See `LICENSE` for details.

---

## Author

- Name: Tulsi Kumar Yadav
- Email: tk6377054@gmail.com

