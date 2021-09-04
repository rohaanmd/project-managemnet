from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('account/', include("members.urls")),
    path('project/', include("projects.urls"))

]
