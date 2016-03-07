from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('email',)
















# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
    # """subclass UserCreationForm to remove username field"""
    
    # def __init__(self, *args, **kwargs):
        # super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # del self.fields['username']
        
        
    # class Meta:
        # model = CustomUser
        # fields = ('email',)
        
        
# class CustomUserChangeForm(UserChangeForm):
    # """subclass UserChangeForm to remove username field"""
    
    # def __init__(self, *args, **kwargs):        
        # super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        # del self.fields['username']
        
        
        # class Meta:
            # model = CustomUser