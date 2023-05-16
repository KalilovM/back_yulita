from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.exceptions import (InvalidCredentialsException,
                                   TokenErrorException, UserNotFoundException)
from apps.users.repositories import UserRepository
from apps.users.serializers import UserSerializer
from apps.users.services import AuthService

User = get_user_model()


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_repository = UserRepository()
        self.auth_service = AuthService(self.user_repository)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = self.auth_service.authenticate_user(email, password)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        except UserNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except InvalidCredentialsException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except TokenErrorException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
