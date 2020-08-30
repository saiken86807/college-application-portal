from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant, Status

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

    return render(request, 'appStatus/apply.html')


def applicant(request, pk_test):
    applicant = Applicant.objects.get(id=pk_test)

    applicants = Applicant.objects.all()

    context = {'applicant': applicant, 'applicants': applicants}
    return render(request, 'appStatus/applicant.html', context)
