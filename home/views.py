from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import CaseForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

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

# core/views.py
def emergency_services(request):
    services = EmergencyService.objects.all()
    return render(request, 'emergency_services.html', {'services': services})
