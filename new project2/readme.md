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
- Password
- Submit button

## Form Validation

The project uses WTForms validators such as:

- `DataRequired()`
- `Email()`
- `Length()`
- `NumberRange()`

When the submitted form is invalid, the user stays on the registration page and the corresponding field errors are displayed.

## Session Protection

The registration page is protected using Flask sessions.

```python
if "user" not in session:
    return redirect(url_for("loginform"))