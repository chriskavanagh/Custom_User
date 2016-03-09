from models import CustomUser
from django.db.models import Q


class CustomUserAuth(object):
    """authentication for custom user. user can login with username OR email."""
    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(Q(first_name=username)| Q(email=username))
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
            
            
            
            
            
## original code using only email to login.
# class CustomUserAuth(object):
    # """authentication for custom user."""
    # def authenticate(self, username=None, password=None):
        # try:
            # user = CustomUser.objects.get(email=username)
            # if user.check_password(password):
                # return user
        # except CustomUser.DoesNotExist:
            # return None
            
    # def get_user(self, user_id):
        # try:
            # user = CustomUser.objects.get(pk=user_id)
            # if user.is_active:
                # return user
            # return None
        # except CustomUser.DoesNotExist:
            # return None