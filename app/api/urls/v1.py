from django.conf.urls import url, include
from rest_framework import routers
from app.api.views.v1 import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls))
]