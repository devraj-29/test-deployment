from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import LoginSerializer, UserSerializer
from .permissions import IsAdminRole, IsUserRole
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF validation
class LoginView(APIView):  # This should be a class-based view, not a function
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)

class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

class AdminStatsView(APIView):
    permission_classes = [IsAdminRole]

    def get(self, request):
        from .models import User
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        return Response({
            "total_users": total_users,
            "active_users": active_users
        }, status=status.HTTP_200_OK)

class UserSummaryView(APIView):
    permission_classes = [IsUserRole]

    def get(self, request):
        last_login = request.user.last_login.isoformat() if request.user.last_login else None
        return Response({
            "last_login": last_login,
            "message": f"Welcome back, {request.user.name}"
        }, status=status.HTTP_200_OK)
