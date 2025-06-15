# -*- coding: utf-8 -*-
"""
This backend can be set in django project settings in order to enable email authentication
In this case, the user will logged with his email rather than with a username
"""

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(ModelBackend):
    """
    Email Authentication Backend: make possible to use email rather than username for user authentication
    """

    def authenticate(self, email=None, password=None, **kwargs):
        """
            check if user can log in:
            return the user if login is successfull
            return None if login fails
         """

        #clean email
        email = email.strip() if email else email

        if email:
            #if email is defined, get every active user corresponding to the given email
            for user in User.objects.filter(email=email, is_active=True):

                if user.check_password(password):
                    #If password is correct: return user to accept it as logged user
                    return user

        #No valid user found : refuse login
        return None

