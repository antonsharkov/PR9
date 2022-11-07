from django.urls import path
from . import views


urlpatterns = [
    path('<int:a>/<int:b>/<int:c>/<int:d>', views.index)
]