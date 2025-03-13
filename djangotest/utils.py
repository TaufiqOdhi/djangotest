from django.contrib.auth.models import User

def check_level_user(user: User):
    if user.is_authenticated:        
        if user.is_superuser:
            return 'superuser'
        elif user.groups.filter(name='manager').exists():
            return 'manager'
        elif user.groups.filter(name='user').exists():
            return 'user'
    else:
        return 'public'