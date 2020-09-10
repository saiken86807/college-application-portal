from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
from .models import Application
from .forms import ApplicantForm, DecisionForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='applicant')
            user.groups.add(group)

            Application.objects.create(
                user=user,
                name=user.username
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'appStatus/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(
                request, 'Username OR password is incorrect, please try again')

    context = {}
    return render(request, 'appStatus/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    applicants = Application.objects.all()

    total_applicants = applicants.count()

    decision_pending = applicants.filter(status='Pending').count()
    decision_accepted = applicants.filter(status='Accepted').count()
    decision_deny = applicants.filter(status='Denied').count()

    context = {'applicants': applicants, 'total_applicants': total_applicants,
               'decision_pending': decision_pending, 'decision_accepted': decision_accepted, 'decision_deny': decision_deny}

    return render(request, 'appStatus/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['applicant'])
def userPage(request):
    if request.user.is_authenticated:
        print('AUTH', request.user)
        print('ID', request.user.id)
        applicants = Application.objects.filter(user=request.user)

        decision_pending = applicants.filter(status='Pending').count()
        decision_accepted = applicants.filter(status='Accepted').count()
        decision_deny = applicants.filter(status='Denied').count()
        decision_none = applicants.filter(status='None').count()

        context = {'applicants': applicants,
                   'decision_pending': decision_pending, 'decision_accepted': decision_accepted, 'decision_deny': decision_deny,
                   'decision_none': decision_none}
        return render(request, 'appStatus/user.html', context)
    else:
        print('NO AUTH')
        return redirect('/')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def applications(request):
    application = Application.objects.all()

    return render(request, 'appStatus/applications.html', {'applications': application})


@login_required(login_url='login')
@allowed_users(allowed_roles=['applicant'])
def apply(request):
    applicants = Application.objects.filter(user=request.user)
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST,)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'applicants': applicants, 'form': form}
    return render(request, 'appStatus/apply.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def applicationReview(request, pk):
    applicant = Application.objects.get(id=pk)
    applicants = Application.objects.all()
    form = DecisionForm(instance=applicant)

    if request.method == 'POST':
        form = DecisionForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'applicants': applicants}
    return render(request, 'appStatus/applicant.html', context)
