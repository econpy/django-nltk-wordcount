from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns("")

if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )

urlpatterns += patterns("",
    url(r"", include('nltk_web.urls'))
)
