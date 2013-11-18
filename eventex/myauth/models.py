# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, cpf, name=None, password=None):
        user = self.model(cpf=cpf, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, name=None, password=None):
        return self.create_user(cpf, name, password)


class User(AbstractBaseUser):
    cpf = models.CharField(max_length=11, unique=True, db_index=True)
    name = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = 'cpf'

    objects = UserManager()

    @property
    def is_staff(self):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name