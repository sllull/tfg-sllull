import domain.views
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", domain.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("data", domain.views.data, name="data"),
    path("send", domain.views.send, name="send"),
    path("plot", domain.views.plot, name="plot"),
    path("plot1", domain.views.plot1, name="plot1"),
    path("plot2", domain.views.plot2, name="plot2"),

]
