from django.shortcuts import render, redirect


# Create your views here.
from User.models import UserAccount_Model, UserComplaint_Model, UserTransaction_Model


def base1(request):

    return render(request, 'user/base.html')


def bank_login(request):
    if request.method == "POST":
        bank = request.POST.get('bankname')
        password = request.POST.get('password')
        if bank==bank and password==password:
            return redirect('bank_home')

    return render(request, 'bank/bank_login.html')



def user_usercarddetails(request):
    objs = UserTransaction_Model.objects.all()


    return render(request, 'bank/user_usercarddetails.html',{'obj':objs})

def view_complaint(request):
    obj = UserComplaint_Model.objects.all()
    return render(request, 'bank/view_complaint.html',{'objc':obj})

def bank_home(request):
    obj =UserAccount_Model.objects.all()

    return render(request, 'bank/bank_home.html',{'objc':obj})