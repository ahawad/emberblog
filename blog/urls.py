from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'blogs',views.PostViewSet)


urlpatterns = urlpatterns = [
    url(r'^', include(router.urls)),
]
