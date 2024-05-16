from django.urls import path
from .views import (
    login_view,
    home_view
)


app_name = "sena_genius"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
]
