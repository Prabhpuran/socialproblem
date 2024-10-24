from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CaseForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# A protected view that requires login
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def home(request):
#     return render(request, 'home.html')

@login_required
def file_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            if form.cleaned_data['is_anonymous']:
                case.user = None
            else:
                case.user = request.user
            case.save()
            return redirect('case_submitted')
    else:
        form = CaseForm()
    return render(request, 'file_case.html', {'form': form})

# # core/views.py
def emergency_services(request):
    services = EmergencyService.objects.all()
    return render(request, 'emergency_services.html', {'services': services})
