from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from Admin.models import Sendquery
from User.models import UserTransaction_Model, UserAccount_Model


def base2(request):


    return render(request, 'admin/base2.html')

def admin_login(request):
    if request.method == "POST":
        admin = request.POST.get('admin')
        password = request.POST.get('password')
        if admin==admin and password==password:
            return redirect('admin_home')

    return render(request, 'admin/admin_login.html')


def admin_home(request):
    obj = UserAccount_Model.objects.all()


    return render(request, 'admin/admin_home.html',{'objc':obj})


def admin_viewdetails(request):
    objs = UserTransaction_Model.objects.all()

    return render(request, 'admin/admin_viewdetails.html',{'obj':objs})





def riskalert(request,tuser):

    obj = UserTransaction_Model.objects.get(id=tuser)

    if request.method == "POST":
        admin = request.POST.get('name')
        names = request.POST.get('name1')
        Sendquery.objects.create(transid=obj,sendquery=admin, name=names)




    return render(request, 'admin/riskalert.html')

def riskuser(request):
    obj = UserTransaction_Model.objects.filter(tamount__range=(500000, 2500000))

    return render(request, 'admin/riskuser.html', {'objv': obj})


def charts(request,chart_type):
    chart = UserTransaction_Model.objects.values('tdate').annotate(dcount=Count('tdate'))

    return render(request, 'admin/charts.html', {'form':chart, 'chart_type':chart_type})