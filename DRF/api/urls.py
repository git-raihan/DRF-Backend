from django.urls import path, include
from api.views import BasicApiView
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', BasicApiView.as_view(), name="basic"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('admin-dashboard/', include('admin_dashboard.urls')),
]
