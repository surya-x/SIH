from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls.conf import include
from Education import views
from django.views.generic.base import RedirectView


urlpatterns = [ 
        path('', RedirectView.as_view(url="home/")),
        path('home/', views.homeView.as_view()),   
        path('about/', views.aboutView.as_view()),   
        path('books/<int:pk>', views.BookDetailView.as_view()),
        path('dashboard/<int:pk>', views.DashboardView.as_view()),
        path('dashboard/edit/<int:pk>', views.DashboardUpdateView.as_view(success_url="/Education/home")),

        # path('', RedirectView.as_view(url="home/")),   
]
