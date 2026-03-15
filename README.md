# django--project__first--pageToDownload
Prakticky test

Simple Django app that uses SerpAPI to perform Google searches and returns the first organic result as a downloadable JSON file.

> Main magic is inside:
> - `test_stuff/mainf/views.py`
> - `test_stuff/mainf/tests.py`
> - `test_stuff/mainf/templates/index.html`

## Features

- Accepts a search query via POST
- Calls SerpAPI to fetch Google search results
- Returns the first organic result as a JSON file download
- Configured to use `.env` for secrets

---

## Requirements

- Python 3.12+
- Django 5.2+
- `requests`
- `python-dotenv`

---
