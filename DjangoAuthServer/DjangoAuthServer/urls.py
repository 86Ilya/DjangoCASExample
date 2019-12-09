from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from DjangoAuthServer.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT, DEBUG

urlpatterns = [
    path(r'', include('mama_cas.urls')),
    path('credentials/', include('DjangoAuthServer.authapp.urls')),
    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
