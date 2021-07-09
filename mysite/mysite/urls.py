# mysite urls

from django.contrib import admin
from django.urls import include, path

# Create urls here
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
