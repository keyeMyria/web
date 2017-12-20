from django.conf.urls import url, include
from django.contrib import admin

from web.views import IndexView

urlpatterns = [
    url(r'^reservation/', include('make_queue.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', IndexView.as_view()),
]
