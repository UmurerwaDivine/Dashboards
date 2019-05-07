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

def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile})
# @login_required(login_url='/accounts/login/')
# def upload_profile(request):
#     current_user = request.user 
#     title = 'Upload Profile'
#     try:
#         requested_profile = Profile.objects.get(user_id = current_user.id)
#         if request.method == 'POST':
#             form = ProfileUploadForm(request.POST,request.FILES)

#             if form.is_valid():
#                 requested_profile.profile_pic = form.cleaned_data['profile_pic']
#                 requested_profile.bio = form.cleaned_data['bio']
#                 requested_profile.username = form.cleaned_data['username']
#                 requested_profile.save_profile()
#                 return redirect( 'profile' )
#         else:
#             form = ProfileUploadForm()
#     except:
#         if request.method == 'POST':
#             form = ProfileUploadForm(request.POST,request.FILES)

#             if form.is_valid():
#                 new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
#                 new_profile.save_profile()
#                 return redirect( 'profile' )
#         else:
#             form = ProfileUploadForm()   
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
             