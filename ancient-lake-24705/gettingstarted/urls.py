import domain.views
from django.urls import path

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("", domain.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("data", domain.views.data, name="data"),
    path("send", domain.views.send, name="send"),
    path("plot", domain.views.plot, name="plot"),
    path("plot1", domain.views.plot1, name="plot1"),
    path("plot2", domain.views.plot2, name="plot2"),
]
