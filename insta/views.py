from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect 
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url= '/accounts/login/')
def profile(request, id):
    try:
        user = User.objects.get(id = id)
        profile = Profile.objects.get(user = user)
    except:
        profile = None
    if profile == None:
        return redirect('profileupdate')
    else:
        return render(request, 'profile.html', {"user":profile})