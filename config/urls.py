
from django.contrib import admin
from django.urls import path
from chat.views import index_view

from accounts.views import register_view, login_view, logout_view, profile_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', index_view, name='index'),
    path('registration/', register_view,  name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile')
]
