from django.urls import path
from .views import register, home, signup,login, logout

urlpatterns = [
    path('register/', register, name='register' ),
    path('signup/', signup, name='signup'),
    path('signin/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', home, name= 'home' )
]

