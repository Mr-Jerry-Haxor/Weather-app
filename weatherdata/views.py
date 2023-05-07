from django.shortcuts import render , HttpResponse , redirect

# Create your views here.


def index(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # return HttpResponse("Welcome! You are visiting from: {}".format(ip))
    return render(request,'index.html')
   


def home(request):
    if request.method == 'POST':
        city = request.POST.get('cityname')
        print(city)
        return render(request,'home.html',{'city':city})
    else:
        return render(request,'home.html')
    
    
    