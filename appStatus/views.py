from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Applicant, Status
from .forms import ApplicantForm, DecisionForm

# Create your views here.


def home(request):
    status = Status.objects.all()
    applicants = Applicant.objects.all()

    total_applicants = applicants.count()

    decision_pending = status.filter(status='Pending').count()
    ready_review = status.filter(status='Accepted').count()

    context = {'status': status, 'applicants': applicants, 'total_applicants': total_applicants,
               'decision_pending': decision_pending, 'ready_review': ready_review}

    return render(request, 'appStatus/dashboard.html', context)


def applications(request):
    application = Applicant.objects.all()

    return render(request, 'appStatus/applications.html', {'applications': application})


def apply(request):
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'appStatus/apply.html', context)


def applicant(request, pk_test):
    applicant = Applicant.objects.get(id=pk_test)

    applicants = Applicant.objects.all()

    context = {'applicant': applicant, 'applicants': applicants}
    return render(request, 'appStatus/applicant.html', context)


def applicationReview(request, pk):
    applicant = Applicant.objects.get(id=pk)
    form = DecisionForm(instance=applicant)

    if request.method == 'POST':
        form = DecisionForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'appStatus/applicant.html', context)
