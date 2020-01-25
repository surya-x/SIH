from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q
from Education.models import Book, Dashboard
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
# Create your views here.

class welcome(TemplateView):
    template_name = "Education/welcome.html"
    
class logout(TemplateView):
    template_name = "Education/logout.html"

@method_decorator(login_required, name="dispatch")
class BookDetailView(DetailView):
    model = Book


@method_decorator(login_required, name="dispatch")
class aboutView(TemplateView):
    template_name = "Education/about.html"
 
@method_decorator(login_required, name="dispatch")
class homeView(TemplateView):
    template_name = "Education/home.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        bookList = Book.objects.all()

        authorList = []
        for e in bookList:
            authorList.append(e.author)

        si = self.request.GET.get("si")
        if si == None:
            si = ""
        bookList =  bookList.filter(Q(title__icontains = si) | Q(author__icontains = si)| Q(genre__icontains = si)).order_by("-id")

        context["book_list"] = bookList
        context["author_list"] = authorList
        
        return context


@method_decorator(login_required, name="dispatch")
class DashboardView(TemplateView):
    template_name = "Education/dashboard.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        dash = Dashboard.objects.all()
        context["dash"] = dash
        return context


@method_decorator(login_required, name="dispatch")    
class DashboardUpdateView(UpdateView):
    model = Dashboard
    fields = ["name", "age", "programme", "pic"]
