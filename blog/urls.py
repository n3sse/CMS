from django.conf.urls import url
from .views import AllPostsView, IndexView, DetailPostView

urlpatterns = [
    url(r'^$', IndexView.as_view(template_name="blog/index.html"), name='index_view'),
    url(r'^blog/page/(?P<page>[0-9]+)/$', AllPostsView.as_view(template_name="blog/all_posts.html"), name='all_post_view'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', DetailPostView.as_view(template_name="blog/detail_post.html"), name='detail_view'),

]
