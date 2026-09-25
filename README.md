# EventHub — Django Event Ticketing Platform

EventHub is a web application for publishing events and booking tickets online. It connects two kinds of users:

- **Organisers** can create, update, publish, and manage their events.
- **Attendees** can browse available events, view event details, and reserve tickets.

The project is built step by step with Django. Its main purpose is to turn core Django concepts into one complete, practical application—from the first page and database model to booking logic and deployment.

## What the application will do

- Show a list of available events.
- Display a dedicated detail page for each event.
- Let organisers create, edit, and remove their own events.
- Let attendees sign up, log in, and log out.
- Use role-based access so organisers and attendees see the right actions and pages.
- Collect validated event and booking data through Django forms.
- Store users, events, tickets, and bookings in a relational database.
- Prevent overbooking when only a limited number of tickets remain.
- Support event images and static assets.
- Run locally during development and be prepared for production deployment.

## Project goal

The goal is to build a real event-booking workflow, not just individual Django examples. By the end, an organiser should be able to publish an event with a ticket limit, while an attendee should be able to find that event and make a booking safely.

## 14-day build journey

| Day | Focus | Project outcome |
| --- | --- | --- |
| 1 | How the web works | Understand browser requests, server responses, and URLs. |
| 2 | Server-side programming | Learn how a server receives a request and returns a response. |
| 3 | Introduction to Django | Understand Django and its MVT (Model–View–Template) structure. |
| 4 | Development setup | Install Python and Django, create a virtual environment, start the project, and run the local server. |
| 5 | Django project structure | Understand the role of `manage.py`, settings, URL configuration, and the application server. |
| 6 | Views and URLs | Create the first application pages and connect views to URL routes. |
| 7 | Database and models | Define data models, create migrations, and read/write data with the Django ORM. |
| 8 | Templates | Render dynamic event pages, pass context to templates, and use named URLs. |
| 9 | Forms and validation | Build forms that accept real user input and show useful validation errors. |
| 10 | Event management (CRUD) | Create, read, update, and delete event data through the application. |
| 11 | User accounts | Add signup, login, logout, and ownership of user-created content. |
| 12 | Roles and permissions | Separate organiser and attendee experiences and protect restricted actions. |
| 13 | Ticket booking | Build booking logic, manage ticket availability, and handle concurrent booking safely. |
| 14 | Production deployment | Configure environment settings, static files, PostgreSQL, and deploy the app to a live URL. |

## Main concepts covered

- Django MVT architecture
- URL routing and views
- Templates and dynamic page rendering
- Models, migrations, SQLite, and PostgreSQL
- Django ORM queries and model relationships
- Forms, validation, and the Post/Redirect/Get pattern
- Authentication, user roles, and access control
- CRUD operations
- File uploads and static files
- Safe ticket availability and booking flow
- Environment-based configuration and deployment

## Technology

- Python
- Django
- SQLite for local development
- PostgreSQL for production deployment
- HTML and CSS templates

## Current project structure

```text
django-ticketing-app/
├── myproject/
│   ├── manage.py              # Django management commands
│   ├── db.sqlite3             # Local development database
│   └── myproject/
│       ├── settings.py        # Project configuration
│       ├── urls.py            # Root URL routes
│       ├── asgi.py            # ASGI application entry point
│       └── wsgi.py            # WSGI application entry point
├── env/                       # Local virtual environment
└── README.md
```

## Run locally

From the project root:

```powershell
cd myproject
..\env\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. Django's administration panel is available at `http://127.0.0.1:8000/admin/` after creating an administrator account.

To create an administrator account:

```powershell
python manage.py createsuperuser
```

## Development approach

Each stage adds a working part of EventHub to the same project. The app grows from a basic Django setup into a deployable ticketing platform with real users, events, bookings, and production configuration.
