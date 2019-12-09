from django.urls import path, include
import django_cas_ng.views as cas_views

urlpatterns = [
    path('djangoapp1/accounts/login/', cas_views.LoginView.as_view(), name='cas_ng_login'),
    path('djangoapp1/accounts/logout/', cas_views.LogoutView.as_view(), name='cas_ng_logout'),
    path('djangoapp1/accounts/callback/', cas_views.CallbackView.as_view(), name='cas_ng_proxy_callback'),
    path('', include('DjangoAppServer.simpleapp.urls')),
]
