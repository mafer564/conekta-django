from django.conf.urls import url
from .views import Pago
from . import views
urlpatterns = [
    url(r'^pago', Pago.as_view(), name='pago_prro'),
    url(r'^historial/$', views.Histo.as_view(), name='historial_amiguitos'),
]
