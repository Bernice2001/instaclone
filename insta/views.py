from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect 
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):   
    image_form = PostForm()   
    images = Post.objects.all()    
    commentform = CommentForm()   
    if request.method == 'POST':       
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():              
            request.user.profile.post(form)  
    return render(request, 'insta/home.html', locals())