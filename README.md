# python-login-system
A simple Python login system with password authentication, failed attempt tracking, and temporary blocking after multiple wrong attempts.
# Python Login System

A beginner-friendly Python project that simulates a secure login system with limited login attempts.

## Features
- Password authentication
- Hidden password input using getpass
- Tracks wrong login attempts
- Blocks login after 3 failed attempts
- Adds temporary delay for security

## Technologies Used
- Python 3
- getpass module
- time module

## How It Works
The program:
1. Asks the user to enter a password
2. Checks whether the password is correct
3. Counts failed login attempts
4. Blocks the user temporarily after 3 wrong attempts

## Concepts Used
- while loop
- if-else conditions
- getpass module
- time.sleep()
- Authentication logic

## Run the Program

```bash
python login_system.py
