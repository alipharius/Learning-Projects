# Website checker

> A Python script that checks the status of websites from a CSV file and generates a report.

## What This Does
This tool reads a list of websites from a CSV file, checks their HTTP status codes, and outputs the results both to the console and a new CSV file with detailed status descriptions.

## Why I Built This
- To learn web scraping and HTTP status handling

- To solve the problem of bulk website monitoring

- Because I was curious about website reliability and response codes

## Quick Start
```bash
cd website-checker
python main.py
```

## Features
- Reads website URLs from CSV files

- Automatically adds HTTPS protocol if missing

- Uses realistic browser user agents to avoid blocking

- Provides detailed HTTP status descriptions

- Exports results to a formatted CSV report

- Handles connection errors gracefully

## What I learned
- HTTP status codes and their meanings using Python's http module

- Working with CSV files for both input and output

- Using the requests library for web interactions

- Implementing fake_useragent to mimic real browsers

- Error handling for network requests and timeouts
## Notes / Future Improvements

- Add support for checking multiple URLs per row

- Implement retry logic for failed requests

- Add concurrent checking for faster performance

- Include response time measurements

- Add command-line arguments for input/output files

---

*Built as part of my learning journey*
