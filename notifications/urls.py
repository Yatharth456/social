from django.urls import path
from .views import home, send_push

urlpatterns = [
    path('', home),
    path('send_push', send_push),
    # path('webpush/', include('webpush.urls')),
]