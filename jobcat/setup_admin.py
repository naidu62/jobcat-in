# setup_admin.py (standalone)
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobcat.settings")
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

# Apply migrations and collect static files
call_command("migrate", interactive=False)
call_command("collectstatic", interactive=False)

# Create superuser if not exists
User = get_user_model()
if not User.objects.filter(username="naidu62").exists():
    User.objects.create_superuser(
        username="naidu62",
        email="vn04081994@gmail.com",
        password="naidu123"  # Replace with a strong password or use an env variable
    )
    print("✅ Superuser created")
else:
    print("✅ Superuser already exists")
