from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import update_last_login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers, status

from apps.token.services import create_token 



class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})
        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True
        super().__init__(*args, **kwargs)


class Login(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(required=True)
        password = PasswordField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.validated_data)
        if user is None:
            raise AuthenticationFailed(_('Invalid Credentials'))
        
        login(request, user)
        update_last_login(None, user)
        access_token = create_token(user)

        return Response({"access_token": access_token})


