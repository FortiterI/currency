"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from currency import views as currency_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', currency_views.index),
    path('contact_us/contacts_list/', currency_views.show_all_contactus_records),
    path('rate/list/', currency_views.rate_list),
    path('rate/create/', currency_views.rate_create),
    path('rate/update/<int:pk>/', currency_views.rate_update),
    path('rate/delete/<int:pk>/', currency_views.rate_delete),
    path('source/list/', currency_views.source_list),
    path('source/create/', currency_views.source_create),
    path('source/update/<int:pk>/', currency_views.source_update),
    path('source/delete/<int:pk>/', currency_views.source_delete)
]
