from django.contrib import admin
from django.urls import path
from .views import home_view, about_view


urlpatterns = [
  path("", view=home_view), # index page -> root page
  path("about/", view=about_view),
  path("hello-world/", view=home_view),
  path("hello-world.html", view=home_view),
  path('admin/', admin.site.urls),
]
