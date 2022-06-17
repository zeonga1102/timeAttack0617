from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserView.as_view()),
    path('login/', views.UserApiView.as_view()),
]
