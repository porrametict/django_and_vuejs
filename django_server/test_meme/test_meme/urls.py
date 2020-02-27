from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from borrowing import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(urls.urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
