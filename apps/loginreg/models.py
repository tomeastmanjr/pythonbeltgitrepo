from __future__ import unicode_literals
from django.db import models

import bcrypt
import re


class UserManager(models.Manager):
    def register(self, reg_data):
        name = reg_data['name']
        username = reg_data['username']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            user = self.get(username=username)
        except:
            user = False
        if len(name) >2 and len(username) >2 and len(password) >7 and password == confirm_password and not user:
            u = self.create(name=name, username=username, password=hashed)
            print u
            print reg_data
            return (True,u)
        return (False,"Try again using only letters in name and username and double check your password")

    def login(self, log_data):
        username = log_data['username']
        user = self.filter(username=username)
        password = log_data['password']
        if len(user) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        return (False, 'Password or username are incorrect')



class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
