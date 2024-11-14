from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        # Validate username
        elif len(username) < 3:
            raise UserInputError("Username must be at least three characters long.")
        elif not all(char.isalpha() for char in username):
            raise UserInputError("Username must contain only characters.")
        # Validate password
        elif password != password_confirmation:
            raise UserInputError("Passwords didn't match.")
        elif len(password) < 8:
            raise UserInputError("Password must be at least eight characters long.")
        elif not any(char.isdigit() for char in password):
            raise UserInputError("Password must have atleast one number.")
        elif all(char.isdigit() for char in password):
            raise UserInputError("Password must have atleast one character.")

        return True

user_service = UserService()
