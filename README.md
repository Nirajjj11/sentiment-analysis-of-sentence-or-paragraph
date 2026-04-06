# NLP Learning

A simple Django project for paragraph sentiment analysis using NLTK's VADER sentiment analyzer.

## Project Overview

This repository contains a Django web app that lets users enter sentences or paragraphs and receive a sentiment evaluation: Positive, Neutral, or Negative.

The app includes:
- A landing page with navigation
- A sentiment analysis page powered by `nltk.sentiment.SentimentIntensityAnalyzer`
- A Django app named `para_sentiment_analysis`

## Folder Structure

```
README.md
manage.py
db.sqlite3
nlp_learning/
    __init__.py
    asgi.py
    settings.py
    urls.py
    views.py
    wsgi.py
para_sentiment_analysis/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
    migrations/
        __init__.py
    templates/
        sentiment.html
templates/
    index.html
    sidebar.html
```

## Installation

### Prerequisites
- Python 3.10+ installed
- `pip` package manager available

### Setup steps

1. Open a terminal inside the project root.
2. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install required packages:

```powershell
pip install django nltk
```

4. (Optional) If you prefer to install the VADER lexicon manually:

```powershell
python -m nltk.downloader vader_lexicon
```

## Running the Project

1. Apply migrations:

```powershell
python manage.py migrate
```

2. Start the Django development server:

```powershell
python manage.py runserver
```

3. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## How to Use

- Visit the home page at `/`
- Click the `Sentiment` link or go to `/sentiment_analysis/`
- Enter a sentence or paragraph in the input field
- Submit to see the sentiment score and classification

## Routes

- `/` - Main landing page
- `/sentiment_analysis/` - Sentiment analysis page

## Notes

- The project uses SQLite by default: `db.sqlite3`
- Debug mode is enabled in `nlp_learning/settings.py` for local development
- If running in production, set `DEBUG = False` and configure `ALLOWED_HOSTS`

## Troubleshooting

- If the app fails because `vader_lexicon` is missing, run:

```powershell
python -m nltk.downloader vader_lexicon
```

- If the server does not start, verify that your virtual environment is activated and dependencies are installed.

## License

This repository does not include an explicit license file.

