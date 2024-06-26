from django.conf import settings
from django.urls import include, path

from . import views

app_name = "amor"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
