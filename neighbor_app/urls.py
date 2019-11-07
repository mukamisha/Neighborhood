from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^new/post/(\d+)', views.new_post, name='new_post'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^business/(\d+)',views.add_business,name='add_business'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.add_profile, name='add_profile'),
    url(r'^search/', views.search_business, name='search_business'),
 
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
  