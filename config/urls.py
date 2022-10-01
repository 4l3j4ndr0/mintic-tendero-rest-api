"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.controllers.BussinessController import Bussiness
from api.controllers.CustomersController import Customers
from api.controllers.ProvidersController import Providers
from api.controllers.ProductsController import Products
from api.controllers.UserController import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path("api/bussiness", Bussiness.as_view(), name="Bussiness"),
    path("api/bussiness/<int:id>",
         Bussiness.as_view(), name="Bussiness"),
    path("api/customer", Customers.as_view(), name="Customers"),
    path("api/customer/<int:id>/<int:bussiness_id>",
         Customers.as_view(), name="Customers"),
    path("api/provider", Providers.as_view(), name="Providers"),
    path("api/provider/<int:id>/<int:bussiness_id>",
         Providers.as_view(), name="Providers"),
    path("api/product", Products.as_view(), name="Products"),
    path("api/product/<int:id>/<int:bussiness_id>",
         Products.as_view(), name="Products"),
    path("api/user", User.as_view(), name="Users"),
]
