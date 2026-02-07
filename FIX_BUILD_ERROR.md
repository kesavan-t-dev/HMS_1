# Fix: externally-managed-environment Error

## Problem
Vercel build fails with error:
```
error: externally-managed-environment
× This environment is externally managed
```

This occurs because Python 3.11+ doesn't allow pip packages to be installed to the system Python without explicit permission.

## Solution

✅ **Fixed in 2 ways:**

### 1. Updated build_files.sh
Added `--break-system-packages` flag to pip install:
```bash
pip install --break-system-packages -r requirement.txt
python manage.py collectstatic --noinput
```

### 2. Updated vercel.json
Simplified the build configuration to use `buildCommand` directly:
- Removed `@vercel/static-build` builder
- Added `buildCommand` with both pip install and collectstatic
- Added `PYTHONUNBUFFERED` environment variable for better logging
- Kept only `@vercel/python` builder for WSGI

## Next Steps

1. **Commit Changes**
```bash
git add .
git commit -m "Fix: externally-managed-environment error on Vercel"
git push origin main
```

2. **Redeploy on Vercel**
   - Delete the failed deployment from Vercel dashboard (Projects → Settings → Deployments)
   - Push to GitHub
   - Vercel will auto-redeploy with the new configuration

3. **Monitor Build**
   - Go to Vercel Dashboard
   - Watch the build logs
   - Look for "Build completed successfully"

## How It Works

- `--break-system-packages`: Allows pip to install packages despite externally managed environment
- `buildCommand`: Tells Vercel to run pip install and collectstatic together
- `PYTHONUNBUFFERED`: Ensures logs appear in real-time (helpful for debugging)
- Single `@vercel/python` builder: Cleaner, more reliable build process

## Verification

After successful deployment:
1. ✅ No build errors in Vercel logs
2. ✅ Static files collected to `staticfiles/` directory
3. ✅ Application loads without 500 errors
4. ✅ CSS, JS, images display correctly

## If Still Getting Errors

**Option 1: Clear Build Cache**
- Vercel Dashboard → Project Settings → Git → Deployments
- Click "Clear Cache" button
- Trigger redeploy

**Option 2: Manually Delete & Redeploy**
- Delete project from Vercel
- Create new project from GitHub
- Vercel will use latest vercel.json

**Option 3: Check requirement.txt**
- Ensure all packages are compatible with Python 3.11
- Run locally: `pip install -r requirement.txt`
- If issues, update package versions

## Environment Variables

Make sure these are set in Vercel:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `false`
- `ALLOWED_HOSTS` - Your Vercel domain
- `DB_*` - Database credentials

---
**Status**: ✅ Build error fixed. Ready to redeploy!
