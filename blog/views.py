from django.views.generic import DetailView, ListView, TemplateView
from .models import Post


class IndexView(TemplateView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title_page'] = "HomePage"
        context['posts'] = Post.objects.all()[:5]
        return context


class DetailPostView(DetailView):
    model = Post


class AllPostsView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6
