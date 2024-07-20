from django.contrib import admin
from django.urls import path
from .views import home_page_view


urlpatterns = [
  path("", view=home_page_view), # index page -> root page
  path("hello-world/", view=home_page_view),
  path("hello-world.html", view=home_page_view),
  path('admin/', admin.site.urls),
]
