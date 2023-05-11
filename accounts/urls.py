
from django.urls import path
from accounts.views import CustomLoginView,RegisterView


urlpatterns = [
    path('login/', CustomLoginView.as_view(),name="login"),
    path('register/', RegisterView.as_view(), name="register")
]