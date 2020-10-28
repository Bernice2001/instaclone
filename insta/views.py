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

@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    # profile_details = Profile.objects.get(owner_id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()
    return render(request, 'profile/new.html', locals())
