"""video_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from posts.views import FileView
from searches.views import search_view

from posts.views import (
        display_record,
        home_page,
        Post_list_view,
        model_form_upload,
    
  )  

urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls')),
    path('videos/<str:title>/',display_record),
    path('', home_page),
    path('videos/', Post_list_view),
    path('search/',search_view),
    path('upload/', model_form_upload),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

