from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('forgot/', views.forgot),
    path('login/', views.login),
    path('signup/', views.signup),
]