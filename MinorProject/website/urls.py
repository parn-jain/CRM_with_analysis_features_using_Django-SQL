from django.contrib import admin
from django.urls import path, include   
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index, name='home'),
    # path('home',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contactus, name='about'),
    path('services',views.services, name='services'),
    # path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('data',views.data, name='data'),
    path('qty', views.combined_view, name='combined_view'),
]


# Add the following line to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)