# Student College Registration System

A simple **Student College Registration System** built with **Python and Flask** to practice backend development and Flask fundamentals.

## Project Overview

This project follows a login-based college registration system.

The user must first log in before accessing the registration form.

### Application Flow

1. User opens the **Login Page**.
2. User enters their name and password.
3. If the login details are correct, the user's name is stored in the Flask session.
4. The user can then access the **College Registration Form**.
5. The user fills in their registration details.
6. Flask-WTF validates the submitted form.
7. The registration name is compared with the logged-in user's name.
8. If both names match, the user is redirected to the **Success Page**.
9. If the names do not match, an error message is displayed and the user is asked to fill in the form again.
10. The user can log out and return to the Login Page.

## Features

- Login system
- Session-based authentication
- Protected registration route
- Student registration form
- Form validation using Flask-WTF and WTForms
- Name matching between login and registration
- Flash messages
- Success and error messages
- Logout functionality
- Input normalization using Python's `re` library

## Registration Form

The registration form contains:

- Full Name
- Age
- Course
- Email
- Submit button

## Form Validation

The project uses WTForms validators such as:

- `DataRequired()`
- `Email()`
- `Length()`
- `NumberRange()`

When the submitted form is invalid, the user stays on the registration page and the corresponding field errors are displayed.

## Session Protection

## Registration Page Protection

The registration page is protected using **Flask sessions**. A user must log in before they can access the registration page:

```python
if "user" not in session:
    return redirect(url_for("loginform"))
```

### Name Verification Process

After the registration form passes validation, the entered registration name is compared with the name stored in the session.

#### Scenario 1: Names Match
* Login Name 
* ↓ 
* Registration Name 
* ↓ 
* **Names Match** 
* ↓ 
* **Registration Successful** 
* ↓ 
* Success Page

#### Scenario 2: Names Do Not Match
* Login Name 
* ↓ 
* Registration Name 
* ↓ 
* **Names Do Not Match** 
* ↓ 
* **Error Flash Message** 
* ↓ 
* Redirect to Registration Page

---

### Handling Extra Spaces

The project automatically cleans up unnecessary spaces in names using Python's **`re`** library. For example, an input with accidental extra spaces like:

`Mohana   Pal`

Is converted into a clean string:

`Mohana Pal`

This is achieved using the following regex substitution, which prevents unnecessary spacing from causing a name mismatch:

```python
import re

name = re.sub(r"\s+", " ", name)
```

---

### Flash Messages

Flask's `flash()` function displays temporary notification feedback to the user:

* **Successful registration:** Displays a success message.
* **Different registration name:** Displays an error message.

These categorized messages are retrieved and displayed in the HTML templates using:

```python
get_flashed_messages(with_categories=True)
```


## Technologies Used
- Python
- Flask
- Flask-WTF
- WTForms
- Jinja2
- HTML
- Regular Expressions (re)

## Project Structure
```text
new project2/
│
├── app.py
├── form.py
├── login.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── registration.html
│   └── success.html
│
├── requirements.txt
└── README.md
```


## What I Learned

Through this project, I learned and practiced:

- Flask routes
- GET and POST requests
- render_template()
- redirect()
- url_for()
- Flask sessions
- Protected routes
- Flask-WTF
- WTForms
- validate_on_submit()
- Form validators
- Field validation errors
- Flash messages
- Flash message categories
- Jinja2 template inheritance
- Login and registration workflow
- Logout functionality
- Regular expressions
- Normalizing user input
- Git and GitHub

## Purpose

This project is part of my Backend Learning journey.

The purpose of this project was to understand how different Flask concepts such as sessions, forms, validation, redirects, flash messages, and Jinja templates work together in a complete backend applicatio
