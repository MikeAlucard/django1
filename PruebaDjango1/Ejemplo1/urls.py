from django.conf.urls import url
from Ejemplo1 import views
from Ejemplo1.views import fecha

urlpatterns = [
    url(r'^land/$', views.current_datetime),
    url(r'^fecha/$', fecha.as_view(), name="fecha"),
]