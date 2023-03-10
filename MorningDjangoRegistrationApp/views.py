from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required



def registration(request):
    if request.method == "POST":
        form == UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully")
            return redirect('user-registration')
        else:
            messages.error(request, 'account not successfully created')
            return redirect('user-registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})






@login_required
def home(request):
    return render(request, 'home.html')
