from flask import request, Response
from . import tmp


class FlaskBasicAuth:
    def __init__(self, users):
        """
        Initialize the FlaskBasicAuth class.
        
        :param users: A dictionary where the keys are usernames and the values are corresponding passwords.
        """
        self.users = users

    def check_auth(self, username, password):
        """
        Check if a username/password combination is valid.
        
        :param username: The username
        :param password: The password
        :return: True if valid, False otherwise
        """
        return username in self.users and self.users[username] == password

    def authenticate(self):
        """
        Send a 401 response that enables basic auth.
        
        :return: A response object
        """
        return Response(
            'Could not verify your access level for that URL.\n'
            'You have to login with proper credentials', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'})

    def require_auth(self, f):
        """
        Decorator that protects routes with basic auth.
        
        :param f: The function to be decorated
        :return: The wrapped function
        """
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not self.check_auth(auth.username, auth.password):
                return self.authenticate()
            return f(*args, **kwargs)
        return decorated
