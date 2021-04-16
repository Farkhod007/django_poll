from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
]
