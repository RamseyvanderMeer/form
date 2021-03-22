from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

def send_json(request):

    post_obj = Post.objects.get()

    data = {
        "Event" : post_obj
    }

    return render(request, "json.html", data)
    
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'createpost.html')  

        else:
                return render(request,'createpost.html')


