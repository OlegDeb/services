from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

admin.site.site_header = 'Админ-панель название сайта'

admin.site.site_title = 'Админка'

admin.site.index_title = 'Добро пожаловать в интерфейс администратора!'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
