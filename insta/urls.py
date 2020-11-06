from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='homepage'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login', views.login, name='login'),
    path('profile/<username>/', views.profile, name='user_profile'),
    path('profile/edit/<username>',views.edit_profile,name ='editProfile'),
    path('profile/create/<username>/', views.profile_form, name='createProfile'),
    path('serach/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)