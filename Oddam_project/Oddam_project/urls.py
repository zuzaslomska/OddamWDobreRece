"""Oddam_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from Oddam_app.views import LandingPage,Registration,Login,GiveawayView,AdminList, AdminUpdate, AdminDelete, AdminCreate, \
    FundationsList, FundationCreate, FundationUpdate, FundationDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='home'),
    path('register/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('giveaway/', GiveawayView.as_view(), name='giveaway'),
    path('admin/list', AdminList.as_view(), name='admin_list'),
    path('admin/update/<pk>/', AdminUpdate.as_view(), name='update_admin'),
    path('admin/delete/<pk>', AdminDelete.as_view(), name='delete_admin'),
    path('admin/create', AdminCreate.as_view(), name='create_admin'),
    path('fundations/list', FundationsList.as_view(), name='fundations_list'),
    path('fundations/create', FundationCreate.as_view(), name='create_fundation'),
    path('fundations/update/<pk>/', FundationUpdate.as_view(), name='update_fundation'),
    path('fundations/delete/<pk>/', FundationDelete.as_view(), name='delete_fundation'),


]
