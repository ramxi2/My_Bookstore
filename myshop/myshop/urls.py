"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, re_path
app_name = 'rosetta'
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('coupons/', include(('coupons.urls', 'coupons'), namespace='coupons')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),

]
