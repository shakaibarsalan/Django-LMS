from django.shortcuts import render

# Create your views here.
def Account_app(request):
        return render(request, 'accounts/accounts.html')
