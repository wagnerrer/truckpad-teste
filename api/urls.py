"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from ebook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/create-ebook/', views.CreateEbookView.as_view(), name='create-ebook'),
    path('api/update-ebook/<int:pk>', views.UpdateEbookView.as_view(), name='update-ebook'),
    path('api/list-ebook/', views.ListEbookView.as_view(), name='list-ebook'),
    path('api/delete-ebook/<int:pk>', views.DeleteEbookView.as_view(), name='delete-ebook'),
    path('api/crate-author/', views.CreateAuthorView.as_view(), name='crate-author'),
    path('api/list-author/', views.ListAuthorView.as_view(), name='list-author'),

]
