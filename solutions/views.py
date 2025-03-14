from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Solution, Platform, QuestionType
import markdown

class SolutionListView(ListView):
    model = Solution
    template_name = 'solutions/solution_list.html'
    context_object_name = 'solutions'
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = Platform.objects.all()
        context['question_types'] = QuestionType.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        platform = self.request.GET.get('platform')
        question_type = self.request.GET.get('type')
        search = self.request.GET.get('search')
        
        if platform:
            queryset = queryset.filter(platform__name=platform)
        if question_type:
            queryset = queryset.filter(question_type__name=question_type)
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)
            
        return queryset

class SolutionDetailView(DetailView):
    model = Solution
    template_name = 'solutions/solution_detail.html'
    context_object_name = 'solution'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        md = markdown.Markdown(extensions=['fenced_code', 'codehilite'])
        context['solution_code_html'] = md.convert(f"```\n{self.object.solution_code}\n```")
        context['description_html'] = md.convert(self.object.description)
        return context
