# HMS - Hospital Management System

A Django-based Hospital Management System for managing patient records, doctor appointments, and booking slots.

## Features

-    Patient Management
-    Doctor Management
-    Appointment Booking
-    Slot Management
-    Secure Authentication

## Tech Stack

-   **Backend**: Django 6.0
-   **Database**: PostgreSQL
-   **Frontend**: HTML, CSS, JavaScript
-   **Deployment**: Vercel

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hms.gitcd hms
```

### 2. Create Virtual Environment

```bash
python -m venv venvsource venv/bin/activate  # On Windows: venvScriptsactivate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Create .env File

Copy `.env.example` to `.env` and fill in your database credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```
SECRET_KEY=your-secret-keyDEBUG=TrueALLOWED_HOSTS=localhost,127.0.0.1DB_NAME=your_database_nameDB_USER=your_database_userDB_PASSWORD=your_database_passwordDB_HOST=localhostDB_PORT=5432
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

## Project Structure

```
hms/├── manage.py                 # Django management├── requirement.txt           # Dependencies├── vercel.json              # Vercel deployment config├── build_files.sh           # Build script├── DEPLOYMENT_GUIDE.md      # Deployment instructions│├── hms/                     # Main project folder│   ├── settings.py          # Configuration│   ├── urls.py              # URL routing│   ├── wsgi.py              # WSGI application│   └── asgi.py              # ASGI application│└── home/                    # Main app    ├── models.py            # Database models    ├── views.py             # View functions    ├── urls.py              # App URLs    ├── admin.py             # Admin configuration    │    ├── Templates/           # HTML templates    │   ├── index.html    │   ├── form.html    │   ├── confirmation.html    │   └── static/          # CSS, JS, Images    │       └── js/    │           └── slot.js    │    └── migrations/          # Database migrations
```

## Usage

### Access Admin Panel

1.  Go to `http://localhost:8000/admin`
2.  Login with superuser credentials
3.  Manage patients, doctors, and appointments

### Main Application

-   Visit `http://localhost:8000/` to access the main interface
-   Book appointments using the form
-   View confirmation after booking

## API Endpoints

Endpoint

Method

Description

`/`

GET

Home page

`/admin`

GET

Admin panel

## Database Models

**Patient**: Stores patient information**Doctor**: Stores doctor details  
**Appointment**: Manages appointment bookings**MappingModel**: Links patients and doctors

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for step-by-step Vercel deployment instructions.

Quick steps:

1.  Push code to GitHub
2.  Connect repo to Vercel
3.  Add environment variables
4.  Deploy automatically on push

## Environment Variables

```
SECRET_KEY          # Django secret keyDEBUG               # True for development, False for productionALLOWED_HOSTS       # Comma-separated domain listDB_NAME             # Database nameDB_USER             # Database userDB_PASSWORD         # Database passwordDB_HOST             # Database hostDB_PORT             # Database port (default: 5432)
```

## Troubleshooting

### Database Connection Error

-   Check database credentials in `.env`
-   Ensure PostgreSQL is running
-   Verify database exists

### Static Files Not Loading

```bash
python manage.py collectstatic
```

### Port Already in Use

```bash
python manage.py runserver 8001
```

## Support

For issues and questions, check the DEPLOYMENT_GUIDE.md or Django documentation.

## License

This project is open source and available under the MIT License.

---

**Happy coding! 🚀**