from django.conf.urls import url, include
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('^$', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    url('accounts/', include('django.contrib.auth.urls')),
   # url(r'home/$', views.home, name='home'),
    url(r'^profile/(\d+)$', views.profile, name='profile'),
    url(r'^editprofile/',views.profile,name ='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)