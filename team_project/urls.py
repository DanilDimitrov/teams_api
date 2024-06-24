from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.views import TeamViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'persons', PersonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]