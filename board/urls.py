from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url('^$',views.index, name='index'),
    url(r'^users',views.users, name='users'),
    url(r'^client',views.client, name='client'),
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)