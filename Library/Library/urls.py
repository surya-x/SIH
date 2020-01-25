from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from Library import settings
from Education import views

urlpatterns = [
    path('admin/', admin.site.urls),              
    path('Education/', include('Education.urls')), 
    path('', views.welcome.as_view()),
    path('accounts/', include('registration.backends.default.urls')),                 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
