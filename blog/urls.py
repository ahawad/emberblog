from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'blogs',views.PostViewSet)


urlpatterns = urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'rest-auth/registration/', include('rest_auth.registration.urls'))
]
