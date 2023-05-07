from django.shortcuts import render , HttpResponse , redirect

# Create your views here.
import pgeocode
nomi = pgeocode.Nominatim('in')
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
        if city.isnumeric():
            loc = nomi.query_postal_code(city).place_name.split(',')[0]
            return render(request,'home.html',{'city': loc})
        else:
            return render(request,'home.html',{'city':city})
    else:
        return render(request,'home.html')
    
    
    