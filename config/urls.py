
from django.contrib import admin
from django.urls import path

from accounts.views import register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', register_view,  name='registration')
]
