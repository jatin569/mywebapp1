from django.shortcuts import render
from .models import signup
# Create your views here.
from django.contrib import auth
def index(request):

    if 'uid'in request.session:
       uid=request.session['uid']
       userrecord=signup.objects.get(id=uid)
       username=userrecord.Name
       context={'usernm':username}
       return render(request,'app/index.html',context)
    else:
       return render(request,'app/index.html',{})
def reg(request):
    if request.method=='POST':
        data1 = request.POST.get('nm','')
        data2 = request.POST.get('us', '')
        data3 = request.POST.get('em', '')
        data4 = request.POST.get('ps', '')

        song_obj = signup(Name=data1 ,Username=data2, Email=data3, Password=data4)
        song_obj.save()
        return render(request, 'app/index.html')
    else:
        return render(request, 'app/index.html')
def login(request):
    if request.method == 'POST':
        Uss = request.POST['us']
        Pss = request.POST['ps']
        try:
            d1 = signup.objects.get(Username=Uss)
            d2 = signup.objects.get(Password=Pss)
        except signup.DoesNotExist:
            d1 = None
            d2 = None
            if (Uss == d1 and Pss == d2):
              return render(request, 'app/index.html')
            else:
               return render(request, 'app/index.html')
        else:
            if (Uss == d1.Username and Pss == d2.Password):
                request.session['uid'] = d1.id
                return render(request, 'app/index.html')
            else:
                return render(request, 'app/index.html')
    return render(request, 'app/index.html')

def logout(request):
    auth.logout(request)
    try:
        del request.session['userid']
    except KeyError:
        pass
    return render(request,'appr/index.html')
