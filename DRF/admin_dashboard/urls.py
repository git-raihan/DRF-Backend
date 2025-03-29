from django.urls import path
from admin_dashboard.views import AdminLoginView, AdminDashboardView

urlpatterns = [
    path("login/", AdminLoginView.as_view(), name="admin-login"),
    path("", AdminDashboardView.as_view(), name="admin-dashboard"),
]
