from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import authenticate
from rest_framework import status
from admin_dashboard.permissions import IsSuperUser
from admin_dashboard.serializers import AdminLoginSerializer

class AdminLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(username=email, password=password)

            if user and user.is_superuser:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "message": "Login successful"
                })
            return Response({"error": "Invalid credentials or not an admin"}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated,IsSuperUser]

    def get(self, request):
        user_data = {
            "id": request.user.id,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "is_superuser": request.user.is_superuser,
            "is_staff": request.user.is_staff,
            "is_active": request.user.is_active,
        }
        return Response(
            {
                "message": "Welcome to the Admin Dashboard", 
                "data":user_data
            }
        )