"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import tickets.views as views


urlpatterns = [
    path("next", views.NextClientView.as_view()),
    path('processing', views.ProcessingView.as_view()),
    path('welcome/', views.WelcomeView.as_view()),
    path('menu/', views.MenuView.as_view()),
    path('get_ticket/change_oil/', views.ChangOilView.as_view()),
    path('get_ticket/inflate_tires/', views.InflateTires.as_view()),
    path('get_ticket/diagnostic/', views.DiagnosticView.as_view()),
]
