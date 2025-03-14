from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, Tag
import markdown

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('search')
        
        if tag:
            queryset = queryset.filter(tags__name=tag)
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(excerpt__icontains=search)
            
        return queryset

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            md = markdown.Markdown(extensions=['fenced_code', 'codehilite'])
            content = self.object.content
            
            # Always try to decode with 'replace' strategy first
            if isinstance(content, bytes):
                try:
                    content = content.decode('utf-8', errors='replace')
                except UnicodeDecodeError:
                    # Fallback encodings with error replacement
                    fallback_encodings = ['latin-1', 'cp1252', 'iso-8859-1']
                    for encoding in fallback_encodings:
                        try:
                            content = content.decode(encoding, errors='replace')
                            break
                        except UnicodeDecodeError:
                            continue

            context['content'] = md.convert(content)
        except Exception as e:
            context['content'] = f"<p>Error rendering content: {str(e)}</p>"
        return context

def index(request):
    try:
        recent_posts = BlogPost.objects.all()[:3]
    except Exception as e:
        recent_posts = []
    return render(request, 'blog/index.html', {
        'recent_posts': recent_posts
    })
