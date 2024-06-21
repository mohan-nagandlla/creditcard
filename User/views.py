from django.shortcuts import render, redirect

# Create your views here.
from Admin.models import Sendquery
from User.forms import UserRegister_Form
from User.models import UserRegister_Model, UserAccount_Model, UserComplaint_Model, UserTransaction_Model



def home(request):
    return render(request,'user/home.html')

def base(request):
    return render(request,'user/base.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = UserRegister_Model.objects.get(username=username,password=password)
            request.session['name']=enter.id
            return redirect('user_account')
        except:
            pass
    return render(request, 'user/user_login.html')

def user_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =  request.POST.get('email')
        username =  request.POST.get('username')
        password =  request.POST.get('password')
        phoneno =  request.POST.get('phoneno')
        gender =  request.POST.get('gender')
        UserRegister_Model.objects.create(name=name, email=email, username=username, password=password,
                                         phoneno=phoneno,gender=gender)
        return redirect('user_login')


    return render(request, 'user/user_register.html')

def user_account(request):
    uuname = ''
    username = request.session['name']
    obj = UserRegister_Model.objects.get(id=username)

    if request.method == "POST":

        cardholder = request.POST.get('cardholder')
        carttype =  request.POST.get('carttype')
        issuingbank =  request.POST.get('issuingbank')
        cardnumber =  request.POST.get('cardnumber')
        cvv =  request.POST.get('cvv')
        issusedate =  request.POST.get('issusedate')
        expiredate =  request.POST.get('expiredate')
        pinnumber =  request.POST.get('pinnumber')
        creditlimit =  request.POST.get('creditlimit')
        UserAccount_Model.objects.create(uuname=obj,cardholder=cardholder,carttype=carttype,issuingbank=issuingbank,cardnumber=cardnumber,cvv=cvv,
                                         issusedate=issusedate,expiredate=expiredate,pinnumber=pinnumber,creditlimit=creditlimit)


    return render(request, 'user/user_account.html',{'form':obj})


def user_complaint(request):

    username = request.session['name']
    objs = UserRegister_Model.objects.get(id=username)
    if request.method == "POST":
        bank = request.POST.get('bank')
        branch =  request.POST.get('branch')
        accountnumber =  request.POST.get('accountnumber')
        username =  request.POST.get('username')
        mobilenumber =  request.POST.get('mobilenumber')
        complaint =  request.POST.get('complaint')
        date =  request.POST.get('date')
        time =  request.POST.get('time')
        UserComplaint_Model.objects.create(cuname=objs,bank=bank,branch=branch,accountnumber=accountnumber,username=username,mobilenumber=mobilenumber,complaint=complaint,date=date,time=time)

    return render(request, 'user/user_complaint.html')


def user_transaction(request):
    username = request.session['name']
    objs = UserRegister_Model.objects.get(id=username)
    if request.method == "POST":
        tcarttype = request.POST.get('tcarttype')
        tcardnumber = request.POST.get('tcardnumber')
        tccv = request.POST.get('tccv')
        texpiredate = request.POST.get('texpiredate')
        tpinnumber = request.POST.get('tpinnumber')
        tamount = request.POST.get('tamount')
        tdate = request.POST.get('tdate')
        ttime = request.POST.get('ttime')
        UserTransaction_Model.objects.create(tname=objs, tcarttype=tcarttype, tcardnumber=tcardnumber, tccv=tccv,
                                           texpiredate=texpiredate, tpinnumber=tpinnumber, tamount=tamount, tdate=tdate,
                                           ttime=ttime)

    return render(request,'user/user_transaction.html',{'form':objs})

def user_home(request):


    return render(request,'user/user_home.html')

def receivealert(request):
    name = request.session['name']
    admin_obj = UserRegister_Model.objects.get(id=name)
    to_name = admin_obj.name
    obj=Sendquery.objects.filter(name=to_name)

    return render(request, 'user/receivealert.html',{'de':obj})