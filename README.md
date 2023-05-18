# booking_events
Sure! Here's a suggested README.md template for your Django booking event app:

# Django Booking Event App

This is a simple Django app for managing booking events with user authentication and email verification.

## Features

- User registration and login with email verification
- User profile with additional fields (first name, last name, birth date, etc.)
- Booking creation with options for hotel selection, start date, end date, room type, and user type
- Access control with superadmin, admin, and regular user roles
- Integration with email service provider (Postmark) for sending verification emails

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bepythonicblog/booking_events.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install Django:

   ```bash
   pip install Django
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Set up the email configuration:

   - If using Gmail, update the `EMAIL_BACKEND` and `EMAIL_HOST_USER` settings in `settings.py` with your Gmail account details.

   - If using Postmark, update the `EMAIL_BACKEND`, `POSTMARK_TOKEN`, and `POSTMARK_SENDER` settings in `settings.py` with your Postmark API token and sender address.

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Register a new user account by clicking on the "Register" link on the homepage.

2. Verify your email address by clicking on the verification link sent to your registered email.

3. Log in using your credentials.

4. Add a booking by navigating to the "Add Booking" page and providing the required information.

5. View and manage your bookings on the "My Bookings" page.

