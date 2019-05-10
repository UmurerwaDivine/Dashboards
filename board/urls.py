from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url('^$',views.index, name='index'),
    url(r'^users',views.users, name='users'),
    url(r'^client',views.client, name='client'),
    url(r'^drivers',views.drivers, name='drivers'),
    url(r'^driver',views.driver, name='driver'),
    url(r'^view/profile/(\d+)', views.view_profile, name='view-profile'),
    url(r'^$',views.profile,name = 'profile'),
    # url(r'^profile/', views.profile, name='profile'),
    # url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    url(r'dashboard',views.dashboard,name="dashboard")
]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)