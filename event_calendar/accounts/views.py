from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .forms import CreateUser
import pprint


def index(request):
    pp = pprint.PrettyPrinter(indent=1, depth=3)
    pp.pprint(request)
    return render(request, 'accounts/index.html')

@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        form_data = CreateUser(request.POST)
        if form_data.is_valid():
            print('form is valid')
            email = request.POST.get("email")
            password = request.POST.get("password1")
            new_user = User.objects.create_user(
                email = email,
                password = password,
            )
        new_user.save()
        login(request, new_user) # automatically log-in the user
        return redirect("accounts:account")
    else: # if method == "GET"
        form_data = CreateUser()
    
    data = {
        "form": form_data,
    }
    
    return render(request, 'accounts/signup.html', data)

@csrf_exempt
def log_in(request):
    login(request)
    # return render(request, 'accounts/index.html')

@csrf_exempt
def log_out(request):
    logout(request)
    # return render(request, 'accounts/index.html')

# @csrf_exempt
# def who_am_i(request):
#     # print(dir(request.user))
#     if request.user.is_authenticated:
#         return JsonResponse({
#             'email': request.user.email
#         })
#     else:
#         return JsonResponse({'user': None})

# login
# logout
# password_change
# password_change_done
# password_reset
# password_reset_done
# password_reset_confirm
# password_reset_complete