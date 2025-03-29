from django.urls import path
from api.views import BasicApiView
urlpatterns = [
    path('', BasicApiView.as_view(), name="basic"),
]
