# Simple Email Sender

> A small Python script to send emails with optional image attachments using SMTP.

## What This Does
This script connects to an SMTP server (Outlook), logs in securely, and sends an email with optional image attachments from the command line.

## Why I Built This
- To learn how SMTP works in Python  
- To practice error handling and exception management  
- To understand SSL/TLS connections in real applications  

## Quick Start
```bash
cd email_sender
python email_sender.py
```
## Features
- Send plain text emails

- Attach image files to emails

- Clear error messages for login, connection, and SSL failures

- Input validation for required fields

## What I Learned
- Using smtplib and ssl from the Python standard library

- Handling specific exceptions instead of generic errors

- Structuring a small but complete Python CLI program

## Notes / Future Improvements
- Support HTML emails

- Add inline images

- Load credentials from environment variables

- Add logging instead of print statements

___
Built as part of my learning journey
