from django.conf.urls import url, include
from . import views
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('profile/$', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'Home/$', views.Home, name='Home'),
    url(r'^profile/(\d+)$', views.profile, name='profile'),
    url(r'^editprofile/',views.profile,name ='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)