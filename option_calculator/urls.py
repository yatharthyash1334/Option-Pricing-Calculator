"""option_calculator URL Configuration

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
from cal.views import two_step
from cal.views import n_step
from cal.views import black_scholes
from cal.views import home_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('Two steps', two_step),
    path('n steps', n_step),
    path('Black Scholes', black_scholes),
]
