
from django.urls import path
from stats.views import AddInstagramView,user


urlpatterns = [
    path('add_instagram/', AddInstagramView.as_view(),name="add_instagram"),
     path('user/', user, name="user"),
]