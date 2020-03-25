from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import SignUp, UserDetailView
from webapp.views import IndexView, AnnounceCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('announce/create/', AnnounceCreateView.as_view(), name='announce_create'),
]