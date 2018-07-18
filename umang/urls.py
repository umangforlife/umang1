"""umang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^blog/$',blog),
    url(r'^about/$',about),
    url(r'^contact/$',contact),
    url(r'^login/$',login),
    url(r'^sign/$',sign),
    url(r'^team/$',team),
    url(r'^causes-grid/$',causes),
    url(r'^donate/$',donate),
    url(r'^events-grid/$',events),
    url(r'^feedback/$',feedback),
    url(r'^search/$',search),
    url(r'^animals/$',animals),
    url(r'^widow/$',widow),
    url(r'^oldage/$',oldage),
    url(r'^children/$',children),
    url(r'^check_user/$',auth_user),
    url(r'^logout/$',logout,name='logout'),
    url(r'^events-grid/(\w+)$',single_event),
    url(r'^nested/$',nested_comment,name='nested')
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)

