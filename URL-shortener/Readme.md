# URL shortener

> A simple Python script that shortens long URLs using the Cutt.ly API.

## What This Does
This script takes a long URL from the user, automatically adds `https://` if missing, and returns a shortened link using the Cutt.ly URL shortening service.

## Why I Built This
- To learn how to work with web APIs in Python

- To solve the problem of sharing long and messy URLs

- Because I was curious about how URL shorteners work behind the scenes
## Quick Start
```bash
cd [project-folder]
python URL-shortener.py
```

## Features
- Shortens any valid URL using the Cutt.ly API

- Automatically adds https:// if the user forgets it

- Handles API errors and invalid responses gracefully

## What I learned
- How to send HTTP requests using the requests library

- How to work with JSON responses from an API

- Basic error handling and clean function structure

## Notes / Future Improvements

- Add a .env file to hide the API key securely

- Create a GUI or web interface instead of using the terminal

- Add ability to copy the shortened link automatically


---

*Built as part of my learning journey*
