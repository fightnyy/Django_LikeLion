from django.shortcuts import render

def home(request):
    return render(request,'home.html')
    #home 에서는 return render(request,여기서는 이동할 템플릿 이름 근데 temlplates 는 이미 들어간 걸로 친다) 

def usd(request):
    korea = request.POST['korea']
    korea = int(korea)
    usd = korea/1217.50
    return render(request,'usd.html',{'korea':korea,'usd':usd})
    #여기서는 return render(request,이동할 템플릿 이름, 거기서 사용할 변수들)



def jpy(request):
    korea = request.POST['korea']
    korea = int(korea)
    jpy = korea/1127.26*100
    return render(request,'jpy.html',{'korea':korea,'jpy':jpy})
     #여기서는 return render(request,이동할 템플릿 이름, 거기서 사용할 변수들)

def can(request):
    korea = request.POST['korea']
    korea = int(korea)
    can = korea/871.70
    return render(request,'can.html',{'korea':korea,'can':can})
     #여기서는 return render(request,이동할 템플릿 이름, 거기서 사용할 변수들)