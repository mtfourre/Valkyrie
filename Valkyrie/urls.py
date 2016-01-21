from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
from Valkyrie import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^users/', views.users, name='users'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^orders/', views.orders, name='orders'),
) + staticfiles_urlpatterns()
