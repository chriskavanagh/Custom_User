from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth.signals import user_logged_in
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):
    """creates a custom user that uses email instead of username for logging in."""
    
    def _create_user(self, email, password, is_admin, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        
        if not email:
            raise ValueError('You Must Provide A Valid Email')
            
        email = self.normalize_email(email)
        
        user = self.model(email=email, is_admin=is_admin, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
                          
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
        
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)
        
        
        
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """the customer user class."""
    
    email       = models.EmailField(blank=True, unique=True)
    first_name  = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    address1    = models.CharField(max_length=254, blank=True)
    address2    = models.CharField(max_length=254, blank=True)
    area_code   = models.CharField(max_length=20, blank=True)
    country_code     = models.CharField(max_length=10, blank=True)
    date_joined  = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active    = models.BooleanField(default=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')    
    
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)
        
    def __unicode__(self):
        return self.email
        
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
        
    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email, to_email, **kwargs):
        send_mail(subject, message, from_email, [to_email], fail_silently=False)
        
        
        
class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    session = models.ForeignKey(Session)
        
        
################ Signals ################                      

@receiver(post_save, sender=CustomUser)
def send_user_mail(sender, created, instance, **kwargs):
    if created:
        user = CustomUser.objects.get(pk=instance.pk)
        subject = "Welcome To Our Community!"
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        message = "Thank You For Joining Our Django Powered Site!"
        #user.email_user(subject, message, from_email, [to_email], fail_silently=False)
        send_mail(subject, message, from_email, [to_email,], fail_silently=False)
        print "Email Sent To %s" % user.email    # print email address to cmd line
        
        
        
# sender: the CustomUser model class
# created: a boolean indicating if a new User has been created
# instance: the User instance being saved

################ End Signals ################
        
        

        
        
        
        
        
##Original Model Manager##

# Create your models here.
# class CustomUserManager(BaseUserManager):
    # """creates a custom user that uses email instead of username for logging in."""
    
    # def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        # now = timezone.now()
        
        # if not email:
            # raise ValueError('You Must Provide A Valid Email')
            
        # email = self.normalize_email(email)
        
        # user = self.model(email=email, is_staff=is_staff, is_active=True,
                          # is_superuser=is_superuser, last_login=now,
                          # date_joined=now, **extra_fields)
                          
        # user.set_password(password)
        # user.save(using=self._db)
        # return user
        
    # def create_user(self, email, password=None, **extra_fields):
        # return self._create_user(email, password, False, False, **extra_fields)
        
    # def create_superuser(self, email, password, **extra_fields):
        # return self._create_user(email, password, True, True, **extra_fields)
        
        
        
        
        
##Another Ex From StackOverflow##
##http://stackoverflow.com/questions/28981057/cant-get-django-custom-user-model-to-work-with-admin##

# class UserManager(BaseUserManager):
    # def create_user(self, email, password=None):
        # if not email:
            # raise ValueError('Users must have an email address')

        # user = self.model(email=self.normalize_email(email),
                          # )
        # user.is_active = True
        # user.set_password(password)
        # user.save(using=self._db)
        # return user

    # def create_superuser(self, email, password):
        # user = self.create_user(email=email, password=password)
        # user.is_admin = True
        # user.is_superuser = True
        # user.save(using=self._db)
        # return user