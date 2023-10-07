from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions, status
from rest_framework.response import Response

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            username = request.data.get('username')

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise exceptions.ValidationError("Пользователь не найден")

            if not user.phone_number:
                return Response({"user_id": user.id}, status=status.HTTP_400_BAD_REQUEST)

        return response
