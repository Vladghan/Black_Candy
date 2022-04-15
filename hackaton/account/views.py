from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .serializers import AccountSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class AccountListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer


@login_required(login_url='login')
def account(request):
    return render(request, 'account.html')
