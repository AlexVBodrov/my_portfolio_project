from django.shortcuts import render

# Create your views here.

def show_blogs(request):
    return render(request, 'blog/blog.html')