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
        return render(request, 'insta/profile.html', {"user":profile})

@login_required(login_url='/login')
def edit_profile(request):
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
    return render(request, 'insta/profile/new.html', locals())

def home(request):
    return render(request, 'insta/home.html')

def search_results(request):
    
    if "users" in request.GET and request.GET["users"]:
        search_term = request.GET.get("users")
        searched_accounts = Post.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_accounts})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
