from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Set up initial migrations and superuser'

    def handle(self, *args, **kwargs):
        from django.core.management import call_command
        call_command('migrate')
        call_command('collectstatic', interactive=False)
        User = get_user_model()
        if not User.objects.filter(username='naidu62').exists():
            User.objects.create_superuser(
                username='naidu62',
                email='vn04081994@gmail.com',
                password='naidu123'  # Replace with your actual password
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
