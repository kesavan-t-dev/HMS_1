# Vercel Deployment Guide for HMS Project

## Prerequisites

1.  **Vercel Account**: Create an account at [vercel.com](https://vercel.com)
2.  **Git Repository**: Push your code to GitHub, GitLab, or Bitbucket
3.  **PostgreSQL Database**: Set up a PostgreSQL database (Vercel Storage or external service like AWS RDS, Railway, Neon)
4.  **Environment Variables**: Prepare your `.env` values

## Step-by-Step Deployment

### Step 1: Prepare Your Local Repository

```bash
# Initialize git if not already donegit initgit add .git commit -m "Initial commit - Ready for Vercel deployment"
```

### Step 2: Push to GitHub

```bash
# Add remote repositorygit remote add origin https://github.com/your-username/hms.gitgit branch -M maingit push -u origin main
```

### Step 3: Connect to Vercel

1.  Visit [vercel.com/dashboard](https://vercel.com/dashboard)
2.  Click **"Add New..." → "Project"**
3.  Select your GitHub repository (HMS)
4.  Click **"Import"**

### Step 4: Configure Environment Variables

In the Vercel dashboard:

1.  Go to your project settings
2.  Navigate to **"Settings" → "Environment Variables"**
3.  Add the following environment variables:

```
SECRET_KEY: <your-django-secret-key>DEBUG: falseALLOWED_HOSTS: yourdomain.vercel.app,www.yourdomain.vercel.appDB_NAME: <your-database-name>DB_USER: <your-database-user>DB_PASSWORD: <your-database-password>DB_HOST: <your-database-host>DB_PORT: 5432
```

### Step 5: Configure Database

**Option A: Vercel Postgres (Recommended)**

1.  In Vercel dashboard, go to **"Storage" → "Create" → "Postgres"**
2.  Connect to your project
3.  Copy credentials and add to environment variables above

**Option B: External PostgreSQL (AWS RDS, Railway, Neon, etc.)**

-   Get your database connection details
-   Add them as environment variables in Vercel

### Step 6: Deploy

1.  Make sure all changes are committed and pushed to GitHub
2.  Vercel will automatically deploy on every push to main branch
3.  Monitor deployment progress in the Vercel dashboard

### Step 7: Run Migrations

After first deployment:

1.  Go to your project in Vercel dashboard
2.  Click **"Deployments"** → select your deployment
3.  Click **"Functions"** or use terminal:

```bash
# Connect to Vercel CLInpm i -g vercelvercel env pull# Run migrations locally with pulled environmentpython manage.py migrate --settings=hms.settings# Or use Vercel Functions:# Create vercel/migrations.py to run migrations post-deploy
```

Alternative: Use a `api/migrations.py` file that runs on deployment.

### Step 8: Collect Static Files

The `build_files.sh` script handles this automatically:

-   Collects all static files to `staticfiles/`
-   WhiteNoise middleware serves them

### Step 9: Create Superuser (Optional)

For database setup:

```bash
python manage.py createsuperuser
```

## File Changes Summary

**Updated Files:**

-   `vercel.json` - Fixed project name (hms → correct path)
-   `requirement.txt` - Added dependencies:
    -   gunicorn (for production server)
    -   python-decouple (for environment variables)
    -   whitenoise (for static file serving)
    -   psycopg2-binary (for PostgreSQL)
-   `hms/settings.py` - Updated for production:
    -   SECRET_KEY now uses environment variable
    -   DEBUG set to False
    -   ALLOWED_HOSTS configured via env
    -   STATIC_ROOT configured for collectstatic
    -   WhiteNoise middleware added

**New Files:**

-   `.vercelignore` - Excludes unnecessary files from deployment
-   `.env.example` - Template for environment variables
-   `build_files.sh` - Build script (already exists, runs collectstatic)

## Troubleshooting

### Import Error: "No module named decouple"

-   Ensure `python-decouple` is in `requirement.txt`
-   Redeploy the project

### Static files not loading

-   Check STATIC_ROOT and STATIC_URL in settings
-   Verify `collectstatic` ran successfully
-   Check WhiteNoise middleware is in MIDDLEWARE

### Database connection errors

-   Verify environment variables are set correctly in Vercel
-   Check DATABASE credentials
-   Ensure PostgreSQL is accessible from Vercel servers (check firewall/security groups)

### Domain/ALLOWED_HOSTS errors

-   Add your Vercel domain to ALLOWED_HOSTS environment variable
-   Format: `domain1.vercel.app,domain2.vercel.app`

## Post-Deployment Checklist

-    Environment variables set in Vercel
-    Database connection working
-    Migrations applied
-    Static files loading (CSS, JS, images)
-    Admin interface accessible at `/admin`
-    Home page loads correctly

## Useful Commands

```bash
# Test locally before deploymentvercel env pullpython manage.py runserver# Check deployment logsvercel logs# Rollback to previous deployment# (Through Vercel dashboard - Deployments tab)
```

## Support

-   [Vercel Django Documentation](https://vercel.com/docs/frameworks/django)
-   [Django Documentation](https://docs.djangoproject.com/)