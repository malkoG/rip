from django.urls import path

from .views import list_ddays, create_dday

urlpatterns = [
    path('', list_ddays, name="dday_list_view"),
    path('add_dday', create_dday, name="dday_creation_view")
]