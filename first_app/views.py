from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')



def registration(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', context={"user_form": user_form, "profile_form": profile_form})



@login_required()
def dashboard(request):
    return render(request, 'first_app/dashboard.html')









#have an issue with the logout view
@login_required()
def logout(request):
    logout(request)
    return HttpResponseRedirect()










def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

        else:
            print('Error')
            form.save(commit=False)
    page_data = {'page_title': "Contact Page", "form": form}

    return render(request, 'first_app/contact.html', context=page_data)