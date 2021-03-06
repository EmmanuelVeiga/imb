from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('rimov.core.urls', namespace='core')),
    path('crm/', include('rimov.crm.urls', namespace='crm')),
    path('imovel/', include('rimov.imovel.urls', namespace='imovel')),
    path('usuario/', include('rimov.usuario.urls', namespace='usuario')),
    path('media/<path>/', serve, {'document_root = settings.MEDIA_ROOT'}),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
