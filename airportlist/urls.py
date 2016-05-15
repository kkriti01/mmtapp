from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


from airportlist.views import AirportViewSet, index

router = routers.DefaultRouter()
router.register(r'airport', AirportViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^home/$', index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
