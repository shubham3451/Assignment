# Django Restaurant Order Management System

This Django project is a simple order management system where users can switch between different accounts, view products, place orders, and see their order history.

## Features

- **User Switching**: Allows users to switch between accounts without logging in.
- **Product Page**: Displays a list of available products and allows users to order.
- **Order Submission**: Users can place orders for products with quantities and special instructions.
- **Order History**: Displays the orders placed by the user.
- **Error Handling**: Handles errors such as duplicate orders or invalid input.

## Requirements

- Python 3.x
- Django 3.x or higher
- Database (SQLite by default)

## Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/shubham3451/Assignment.git
```

2. Create Two Users (Without Authentication)

Since this application uses session-based user switching, you can create two users using the Django shell.

To create two users, use the following commands:

    Open the Django shell:

python manage.py shell

Create the first user (e.g., user1):

from django.contrib.auth.models import User
user1 = User.objects.create_user(username='user1', password='password1')
user1.save()

Create the second user (e.g., user2):

user2 = User.objects.create_user(username='user2', password='password2')
user2.save()

Exit the Django shell:

exit()


### 3. Apply Migrations

Run the following commands to apply database migrations and create the necessary tables:

```bash
python manage.py migrate
```

### 4. Create a Superuser (Optional)

If you want to manage the admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser.

### 5. Run the Development Server

To start the Django development server, run:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## Project Structure

- **`views.py`**: Contains the logic for handling HTTP requests, such as creating orders, displaying products, switching users, and showing order history.
- **`models.py`**: Defines the `Product` and `Order` models for the application.
- **`forms.py`**: Contains the form for creating orders (`OrderForm`).
- **`templates/`**: Contains the HTML templates for rendering pages.
- **`urls.py`**: Routes URLs to the appropriate views.

## Notes

- The project uses session-based user switching instead of traditional user authentication.
- The order history is stored and displayed by date.
- Duplicate orders for the same product on the same day are prevented.

## License

This project is open-source and available under the [MIT License](LICENSE).
