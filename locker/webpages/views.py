from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.http import HttpResponse
import os

from .forms import SignUpForm
from .models import SignUpModel
# Create your views here.


def test_view(request):
    return render(request, 'base.html', {})


def home_page_view(request):
    print(request.user)
    return render(request, 'home.html', {})


def login_page_view(request):
    context = {}
    if request.method == 'POST':
        login = request.POST

        email = login['email_address']
        password = login['password']

        context = {'email': email}

        if(SignUpModel.objects.filter(email_address=email)):
            user = SignUpModel.objects.get(email_address=email) or None
            username = user.username

            user = authenticate(request, username=username, password=password)

            if(user is not None):
                auth_login(request, user)
                return redirect('../files/')

            else:
                context['message'] = "Email address and/or Password is incorrect."

        else:
            context['message'] = "Email address and/or Password is incorrect."

    return render(request, 'login.html', context)


def signup_page_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = User.objects.create_user(
                username=form.cleaned_data['username'], password=request.POST['password'], email=form.cleaned_data['email_address'])
            user.save()

        else:
            context = {'form': form.cleaned_data, 'errors': []}
            if str(form.errors.as_data().get('username')[0]).find('already exists'):
                context['errors'].append("Username already exists.")

            if str((form.errors.as_data()).get('email_address')[0]).find('already exists'):
                context['errors'].append("Email address already exists.")

            return render(request, 'sign_up.html', context)

    return render(request, 'sign_up.html', {})


def file_page_view(request):
    context = dict()
    user = request.user
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.join(BASE_DIR, 'media')

    if request.method == 'POST':
        file = request.FILES

        if os.path.exists(os.path.join(BASE_DIR, user.username)):
            BASE_DIR = os.path.join(BASE_DIR, user.username)

        else:
            os.makedirs(os.path.join(BASE_DIR, user.username))
            BASE_DIR = os.path.join(BASE_DIR, user.username)

        file_name = file.items()

        for key, values in file_name:
            print(key)
            file_name = values

        with open(os.path.join(BASE_DIR, str(file_name)), 'wb+') as destination:
            for chunk in file['file'].chunks():
                destination.write(chunk)

    if os.path.exists(os.path.join(BASE_DIR, user.username)):
        BASE_DIR = os.path.join(BASE_DIR, user.username)

        file_names = os.listdir(BASE_DIR)

        context['files_present'] = True

        context['file'] = dict()

        url = '../download'
        for item in file_names:
            context['file'][item] = url + '/?file=' + item

        print(context)

    return render(request, 'file.html', context)


def download_file_view(request):
    # print(request.method['GET']['file'])
    if request.method == 'GET':
        print(request.GET.get('file'))

    return HttpResponse('<h1>Hello world</h1>')


def logout_page_view(request):
    logout(request)
    return redirect('../login/')
