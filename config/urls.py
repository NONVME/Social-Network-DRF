from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from content.views import PostViewSet, PostRateView

router = SimpleRouter()

router.register(r'api/post', PostViewSet)
router.register(r'api/post_rate', PostRateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
