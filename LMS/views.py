from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def About(request):
    return render(request, 'website/about.html')

def Contact(request):
    return render(request, 'website/contact.html')

def Enrollment(request):
    return render(request, 'website/enrollment.html')

def Assignment(request):
    return render(request, 'website/assignment.html')

def Programs(request):
    return render(request, 'website/programs.html')

def Resources(request):
    return render(request, 'website/resources.html')

def AuditLog(request):
    return render(request, 'website/auditLog.html')

# def Accounts(request):
#     return render(request, 'website/Accounts.html')