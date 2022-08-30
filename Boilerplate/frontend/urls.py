from django.urls import path
from .views import index

urls = [
    '',
]
urlpatterns = [path(i, index) for i in urls]