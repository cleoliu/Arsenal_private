from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.urls import reverse

from .forms import LoginForm, ProfileForm, PwdChangeForm, RegistrationForm
from .models import ProjectTable, UserProfile


def login_page(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})


@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/profile.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # 基本欄位
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)

            # 擴充欄位
            account_type = form.cleaned_data['account_type']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            tax_id = form.cleaned_data['tax_id']
            tester = form.cleaned_data['tester']
            viewer = form.cleaned_data['viewer']
            user_profile = UserProfile(user=user, account_type=account_type, address=address, phone=phone, tax_id=tax_id if tax_id else 0, estimate_tester=tester, estimate_viewer=viewer)
            user_profile.save()

            # 表 Project_table
            project_table = ProjectTable(account_id=user.id, creator=username)
            project_table.save()

            return render(request, 'index.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form, 'form_data':form.data, 'range': range(1, 11)})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'range': range(1, 11)})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        print("form.is_valid()", form.is_valid())
        print(form.errors)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            # 登入成功
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('team:teams'))
            # 登入失敗
            else:
                return render(request, 'index.html', {'form': form, 'message':'Wrong password Please Try agagin'})
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form})
