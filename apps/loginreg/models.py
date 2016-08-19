from __future__ import unicode_literals
from django.db import models

import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')


class UserManager(models.Manager):
    def register(self, reg_data):
        name = reg_data['name']
        alias = reg_data['alias']
        email = reg_data['email']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(email=email)
        except:
            user = False
        if re.match("^[A-Za-z0-9]+$", name) and re.match("^[A-Za-z0-9]+$", alias) and len(email) > 4 and EMAIL_REGEX.match(email) and len(password) >7 and password == confirm_password and not user:
            u = self.create(name=name, alias=alias, email=email, password=hashed)
            print u
            print reg_data
            return (True,u)
        return (False,"Try again using only letters in name and alias and double check your email/password")

    def login(self, log_data):
        email = log_data['email']
        user = self.filter(email=email)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or email are incorrect')



class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
