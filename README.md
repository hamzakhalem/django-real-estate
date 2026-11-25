# Real Estate Listings

A Django web app for property listings. You can add, browse, edit and delete properties with their price, rooms, area and address.

## Features

- List all properties on the home page
- Property page with title, price, bedrooms, bathrooms, square footage and address
- Create and edit listings with a Django `ModelForm`
- Delete a listing
- Manage listings from the Django admin

## Pages

| Path | What it does |
| --- | --- |
| `/` | All listings |
| `/listing/<id>/` | One listing |
| `/listing-create/` | Add a listing |
| `/listing-update/<id>/` | Edit a listing |
| `/listing-delete/<id>/` | Delete a listing |

## Built with

- Python 3, Django
- Django templates
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django-real-estate.git
cd django-real-estate
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

## Project structure

```
realestate/   Project settings and root URLs
listings/     Listing model, form, views and templates
```
