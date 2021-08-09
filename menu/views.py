from django.shortcuts import render
from .models import Genre

# Create your views here.
def home(request):
    genres = Genre.objects.all()
    return render(request, 'home.html', {'genres': genres})

    def get_context_data(self, *args, **kwargs):
        genre_menu = Genre.objects.all()
        context = super(home, self).get_context_data(*args, **kwargs)
        context["genre_menu"] = genre_menu
        return context

def show_genres(request):

    return render(request, "home.html", {'genres': Genre.objects.all()})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
        
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.replace('-', ' '), 'category_posts':category_posts})