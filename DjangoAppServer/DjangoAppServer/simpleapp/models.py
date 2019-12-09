from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class AuthappUser(AbstractBaseUser):
    username = models.CharField(_('username'), unique=True, max_length=120, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        managed = False
        db_table = 'authapp_user'
