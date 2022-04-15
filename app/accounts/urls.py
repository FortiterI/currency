from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('signup/', views.SignUp.as_view(), name='sign-up'),

]
