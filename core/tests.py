from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


class BaseTest(TestCase):
    
    def make_user(self, username='user', password='password',email='user@mail.com'):  # noqa
                
        return User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
    
    def make_user_permissions(self, user, model, perms=None):
        content_type = ContentType.objects.get_for_model(model)
        model_permissions = Permission.objects.filter(content_type=content_type)  # noqa
        
        print([perm.codename for perm in model_permissions])
            
        for permission in model_permissions:
            if perms:
                if permission.codename in perms:
                    user.user_permissions.add(permission)
            else:    
                user.user_permissions.add(permission)
        
        user.save()    
