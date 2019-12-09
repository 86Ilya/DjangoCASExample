from django.urls import path
from DjangoAuthServer.authapp import views

urlpatterns = [
    path(r'signup/', views.signup_view, name="signup"),
]
