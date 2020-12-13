from django.shortcuts import render
from django.shortcuts import redirect
from customer.forms import Create_user_form
from django.contrib import messages
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@unauthenticated_user
def sign_up_view(request):
    form = Create_user_form()
    if request.method == 'POST':
        form = Create_user_form(request.POST)

        print("Verifying form contents")
        if form.is_valid():
            print("Form verification successful")
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for ' + username)
            return redirect('login_page')
        else:
            print("form verification failed")

    context = {'form': form}
    return render(request, "sign_up.html", context)

@unauthenticated_user
def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Incorrect Username or Password!')

    return render(request, "login_page.html", {})


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login_page')
