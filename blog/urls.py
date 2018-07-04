from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
]