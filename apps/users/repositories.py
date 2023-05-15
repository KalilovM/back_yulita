from django.contrib.auth import get_user_model

User = get_user_model()


class UserRepository:
    def get_by_email(self, email: str) -> User:
        return User.objects.get(email=email)
