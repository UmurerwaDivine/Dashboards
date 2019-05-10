from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import ProfileForm,DriverForm,ClientForm
from django.contrib.auth.decorators import login_required
from . models import Profile, Driver, Client
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      title = 'Trucker'
      # comments = Comment.objects.all()

    #   print(pic_posts)
      return render(request,'index.html',{"title":title})
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['profile_photo']
            profile.user=current_user
            
            profile.save()
        return redirect('index')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_profile(request, id):

    profile=Profile.objects.get(user_id=id)
    return render(request, 'view_profile.html',{"profile":profile},)

   
@login_required(login_url='/accounts/login/')
def client(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form =ClientForm(request.POST ,request.FILES)

        if form.is_valid():
            client = form.save(commit = False)
            client.user_key = current_user
            client.save() 

            return redirect('users')
    else:
        form =ClientForm() 
    return render(request, 'users_form.html',{"form" : form}) 


def users(request):
      title = 'Client'
      all_users = Client.objects.all()
  
      return render(request,'users.html',{"title":title,"all_users":all_users})
def driver(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form =DriverForm(request.POST ,request.FILES)

        if form.is_valid():
            driver = form.save(commit = False)
            driver.user_key = current_user
            driver.save() 

            return redirect('drivers')
    else:
        form =DriverForm() 
    return render(request, 'driver_form.html',{"form" : form}) 


def drivers(request):
      title = 'Driver'
      states=['loading','unloading','on transit']
      import random
      choix=random.choice(states)
      all_driver = Driver.objects.all()
  
      return render(request,'driver.html',{"title":title,"all_driver":all_driver,"state":choix})      
def maps(request):
    ip_address = request.META.get('http://api.ipstack.com/105.178.36.183', '')
    response = request.get('http://api.ipstack.com/105.178.36.183?access_key=bf3dc84257db3e7928449bb12f3d5588&format=1')
    geodata = response.json()
    return render(request, 'core/maps.html', {
        'ip': '105.178.36.183',
        'country': 'Rwanda',
        'latitude': -1.9536,
        'longitude': 30.0606,
        'api_key': 'AIzaSyAGB0lhvVsO4ywn5RGjdLjWBVW9JyaVRTI'  

        # 
    })