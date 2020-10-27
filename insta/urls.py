from django.conf.urls import url, include
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    # url('^$', views.home, name='homepage'),
    # path('signup/', views.signup, name='signup'),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.home,name='home'), 
]