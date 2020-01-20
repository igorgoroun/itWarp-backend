"""itaccounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    # JWT token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # TODO: WHAT A FUCK IS IT?
    # You can also include a route for Simple JWT's TokenVerifyView if you wish to allow API users
    # to verify HMAC-signed tokens without having access to your signing key
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # companies
    path('api/company/', include('company.urls')),

    # DEPRECATED: main frontend app
    # path('', views.index, name="frontend"),

]
