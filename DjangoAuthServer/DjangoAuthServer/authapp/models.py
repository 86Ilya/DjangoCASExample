from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    username = models.CharField(_('username'), unique=True, max_length=120, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return "it's user"

    def get_short_name(self):
        return "it's user"

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
