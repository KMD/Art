from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from artwork.views import ArtworkListView

# TODO delete csrf_exempt when authentication will done
urlpatterns = [
    url(r'^artworks/$', csrf_exempt(ArtworkListView.as_view())),
]
