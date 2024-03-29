from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # jwtの認証を行うためのurlを追加
    path('authen/', include('djoser.urls.jwt'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)