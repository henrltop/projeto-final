from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_automa.urls')), 
    path('', include('app_usuarios.urls'))
]
