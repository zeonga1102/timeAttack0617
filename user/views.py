from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import User, UserType

# Create your views here.
class UserView(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        user_type = request.data.get('user_type', '')
        user_type_object = UserType.objects.get(user_type=user_type)

        User.objects.create( email=email, password=password, user_type=user_type_object)

class UserApiView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request):
        logout(request)
        return Response({'message': '로그아웃 성공'})