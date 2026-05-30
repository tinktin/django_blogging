from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog,Category

def posts_by_category(request,category_id):
    #Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # use get_object_or_404 when you want to show 404 error page(provided by django or built-in) if the category doe not exists
    #category = get_object_or_404(category,pk=category_id)
    # for custom 404 page set Debug = False and allowed_hosts=['*'] in settings.py  and then use
    category = get_object_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category_id':category
    }
    return render(request,'posts_by_category.html',context)
