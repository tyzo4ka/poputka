from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import SignUp, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', SignUp.as_view(), name='create'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),

]