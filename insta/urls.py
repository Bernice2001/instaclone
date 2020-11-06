from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('profile/<username>/', views.profile, name='user_profile'),
    path('profile/edit/<username>',views.edit_profile,name ='editProfile'),
    path('serach/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)