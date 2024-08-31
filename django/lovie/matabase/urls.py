"""matabase URL Configuration

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
from django.contrib import admin
"""
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", MatabaseHome, name="homePage"),
    path("dashboard/", Dashboard, name="dashboardPage"),
    path("user/", Register, name="userPage"),
    path("update/<int:id>/", MatabaseUpdate, name="updatePage"),
    path("delete/<int:id>/", MatabaseDelete, name="deletePage"),
    ### class base views ###
    # path("login/", CLoginView.as_view(), name="login"),
    path("new/", CMatabaseCreateView.as_view(), name="newCMatabase"),
    path("list/", CMatabaseListView.as_view(), name="CMatabaseListView"),
    path("clist/", CustomMatabaseListView.as_view(), name="CustomMatabaseListView"),
    path("clist/<status>", CMatabaseListViewWithParameter.as_view(), name="CMatabaseListViewWithParameter"),
    path("detail/<pk>/", CMatabaseDetailView.as_view(), name="CMatabaseDetailView"),
    path("profile/", CMatabaseProfileView.as_view(), name="CMatabaseProfileView"),
    path("<pk>/update", CMatabaseUpdateView.as_view(), name="CMatabaseUpdateView"),
    path("<pk>/delete", login_required(CMatabaseDeleteView.as_view()), name="CMatabaseDeleteView"),
]
