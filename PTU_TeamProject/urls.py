from django.contrib import admin
from django.urls import path, include
import Card.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Card.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/social/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
