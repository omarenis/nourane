from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from user_auth_management.models import User


def login(email, password):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            try:
                token = RefreshToken.for_user(user=user)
                return token, user
            except TokenError:
                return "error in server", 500
        return "password didn't match", HTTP_403_FORBIDDEN
    except User.DoesNotExist:
        return "user not found", HTTP_404_NOT_FOUND
