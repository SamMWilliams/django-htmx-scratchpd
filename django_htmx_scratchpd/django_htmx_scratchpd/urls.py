from django.contrib import admin
from django.urls import include, path
from django.urls import include, path
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path("", include("amor.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
