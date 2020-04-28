from django.shortcuts import render, get_object_or_404
from .models import Blogfields
# Create your views here.
def index(request):
    blogfield = Blogfields.objects.order_by('-date')[:5]
    context = {
        'blogfields' : blogfield
    }
    return render(request, 'blog/index.html',context)

def detail(request, blog_id):
    blog = get_object_or_404(Blogfields, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})