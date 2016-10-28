from django.conf.urls import url, include
from django.contrib import admin
from pago import urls as Pagourls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pago/', include(Pagourls, namespace='pagos'))
]
