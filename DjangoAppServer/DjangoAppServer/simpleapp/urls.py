from django.urls import path
from DjangoAppServer.simpleapp import views

urlpatterns = [
    path(r'withauthapp/', views.withauthapp, name="withauthapp"),
    path(r'noauthapp/', views.noauthapp, name="noauthapp"),
    path(r'', views.noauthapp, name="noauthapp"),
]
