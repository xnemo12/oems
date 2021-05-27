from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDERS = (
    ('male', _('Male')),
    ('female', _('Female')),
)


class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('Active'), default=True)
    date_of_birthday = models.DateField(_('date of birthday'), null=True, blank=True, )
    gender = models.CharField(choices=GENDERS, max_length=6, null=True, blank=True, )
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', null=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    phone = models.CharField(_('Phone number'), max_length=20, null=True, blank=True)
    language = models.CharField(max_length=5, default='ru')

    class Meta(AbstractUser.Meta):
        app_label = 'users'
