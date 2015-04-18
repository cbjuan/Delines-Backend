from django.conf.urls import patterns, include, url
from api.views import *
from rest_framework.routers import SimpleRouter
from django.contrib import admin

router = SimpleRouter()
router.register(r'routes', RouteViewSet)
router.register(r'users', UserViewSet)
router.register(r'positions', PositionViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'h4gSalamanca_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'populate/$', PopulateData),
)
