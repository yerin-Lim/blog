from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail, post_add, post_delete

urlpatterns = [
    url('admin/', admin.site.urls),
    url('list', post_list),
    url('post/<int:pk>', post_detail),
    url('post/add', post_add, name='post_add'),
    url('post/delete/<int:pk>', post_delete, name='post_delete'),
]
