from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .forms import *

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    avatar = Profile.objects.all()
    posts = Post.objects.filter(user=user).order_by("-date")
    
    post_count = Post.objects.filter(user=user).count()
    follower_count = Follow.objects.filter(following=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
    
    return render(request,'profile/profile.html', {'user':user, 'profile':profile, 'posts':posts, 'avatar':avatar, 'post_count':post_count, 
                                                   'follower_count':follower_count, 'following_count':following_count,'follow_status':follow_status})

@login_required
def edit_profile(request,username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    form = EditProfileForm(instance=profile)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.save()
            return HttpResponseRedirect(reverse('profile', args=[username]))
        else:
            form = EditProfileForm(instance=profile)
    legend = 'Edit Profile'
    return render(request, 'profile/update.html', {'legend':legend, 'form':ProfileForm})

@login_required
def profile_form(request,username):
    userX = request.user
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = userX
            data.save()
            return HttpResponseRedirect(reverse('MainPage'))
        else:
            form = ProfileForm()
    legend = 'Create Profile'
    
    return render(request, 'profile/upd_prof.html', {'form':ProfileForm, 'legend':legend, 'user':user, 
                                                   'userX':userX})

def search_results(request):
    
    if "users" in request.GET and request.GET["users"]:
        search_term = request.GET.get("users")
        searched_accounts = Post.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_accounts})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'/')
    
    return render(request, '/django_registration/login.html')
        
@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')