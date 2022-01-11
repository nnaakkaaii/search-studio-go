from django.contrib import admin
from django.urls import path, include

from crud.urls import router as crud_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/entities/', include(crud_router.urls)),
]
