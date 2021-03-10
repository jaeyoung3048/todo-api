from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

import account.views as account_views

urlpatterns = [
    path('token/', account_views.SigninView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', account_views.SignupView.as_view(), name='sign_up')
]