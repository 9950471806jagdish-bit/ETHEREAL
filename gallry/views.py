from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# pyrefly: ignore [missing-import]
from .models import Profile
# pyrefly: ignore [missing-import]
from .forms import ProfilePhotoForm
# pyrefly: ignore [missing-import]
from .models import Post 

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            password==password
            return redirect('Home')
        else:
            return redirect('login')

    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            return render(request,'signup.html',{'password':'password not match'})
        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    return render(request,'signup.html')

def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('Home')

def Home(request):
    return render(request,'Home.html')

@login_required
def userprofile(request):
    profile, created = Profile.objects.get_or_create(userprofile=request.user)

    if request.method == "POST":
        # Check if a post image or post video was uploaded
        if 'id_post_image' in request.FILES:
            post_img = request.FILES['id_post_image']
            Post.objects.create(post_image=post_img)
            return redirect('userprofile')
        elif 'id_post_video' in request.FILES:
            post_vid = request.FILES['id_post_video']
            Post.objects.create(post_image=post_vid)
            return redirect('userprofile')
        
    posts = Post.objects.all().order_by('-id')  # Fetch all uploaded posts
    return render(request, 'userprofile.html', {
        'profile': profile,
        'posts': posts
    })
    

    









@login_required
def editeuser(request):
    profile, created = Profile.objects.get_or_create(userprofile=request.user)
    
    if request.method == "POST":
        # Handle both Image upload and Profile Detail update
        form = ProfilePhotoForm(request.POST, request.FILES, instance=profile)
        
        # Capture text fields
        username1 = request.POST.get('username1')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        
        # Only update if fields are provided (so we don't overwrite with None)
        if username1: profile.Username = username1 
        if email: profile.email = email 
        if phone: profile.phone = phone 
        if bio: profile.bio = bio 
        if gender: profile.gender = gender 
        if category: profile.category = category 
        
        # Save image if form is valid
        if form.is_valid():
            form.save()
        else:
            profile.save() # save text fields if image form is not valid but other data exists
            
        return redirect('userprofile')
    
    else:
        form = ProfilePhotoForm(instance=profile)
        
    return render(request, 'editeuser.html', {'form': form, 'profile': profile})


    
