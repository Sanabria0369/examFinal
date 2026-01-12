from django.contrib import admin 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatters = [
    path('admin/', admin.site.urls),
]

urlpatters += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





#/from django.urls import path
#/from .views import home, analyze
#/urlpatterns=[path('',home),path('analyze/',analyze)]