from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

import account.views as account_views

urlpatterns = [
    path('auth/token', account_views.SigninView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', account_views.SignupView.as_view(), name='sign_up'),
    path('sms', account_views.sms_authentication, name='sms')
]