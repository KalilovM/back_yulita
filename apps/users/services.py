import logging

from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from .exceptions import (InvalidCredentialsException, TokenErrorException,
                         UserNotFoundException)
from .repositories import UserRepository

User = get_user_model()


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.get_by_email(email)
        if not user:
            raise UserNotFoundException("User not found")
        if not user.check_password(password):
            raise InvalidCredentialsException("Invalid email or password")
        user = authenticate(email=email, password=password)
        try:
            tokens = RefreshToken.for_user(user)
        except:
            raise TokenErrorException("Error while generating tokens")

        return {
            "email": user.email,
            "access_token": str(tokens.access_token),
            "refresh_token": str(tokens),
        }

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_by_email(email)
