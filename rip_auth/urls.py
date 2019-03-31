from django.urls import path
from .views import login_user, register_user, logout_user

urlpatterns = [
    path('signup', register_user, name="rip_user_registration"),
    path('login', login_user, name="rip_user_login"),
    path('logout', logout_user, name="rip_user_logout")
]
