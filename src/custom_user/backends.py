from models import CustomUser
from django.db.models import Q


class CustomUserAuth(object):
    """authentication for custom user."""
    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(email=username)
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
            
            
            

## using username OR email OR phone to log user in.

# class AuthBackend(object):
    # supports_object_permissions = True
    # supports_anonymous_user = False
    # supports_inactive_user = False


    # def get_user(self, user_id):
       # try:
          # return UserProfile.objects.get(pk=user_id)
       # except UserProfile.DoesNotExist:
          # return None


    # def authenticate(self, username, password):
        # try:
            # user = UserProfile.objects.get(
                # Q(username=username) | Q(email=username) | Q(phone=username)
            # )
        # except UserProfile.DoesNotExist:
            # return None

        # return user if user.check_password(password) else None