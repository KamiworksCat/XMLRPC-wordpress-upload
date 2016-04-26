from __future__ import unicode_literals

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class BoltUser(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now=True, verbose_name=_('Created Date'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('Last Modified Date'))

    email = models.EmailField(_('Email Address'), unique=True, max_length=255, default='guest@bolttest.com')
    is_staff = models.BooleanField(_('Staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    first_name = models.CharField(_('First Name'), max_length=100, default='', blank=True)
    last_name = models.CharField(_('Last Name'), max_length=100, default='', blank=True)

    wordpress_link = models.CharField(_('Wordpress Link'), max_length=255, blank=True)
    wordpress_id = models.CharField(_('Wordpress User Name'), max_length=255, blank=True)
    wordpress_pass = models.CharField(_('Wordpress Password'), max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
