from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Team_members


def demo(request):
    obj=Place.objects.all()
    obj1=Team_members.objects.all()
    return render(request,"index.html",{'result':obj,'members':obj1})


# Create your views here.
# def home(request):
#     return render(request,"home.html")

# def home(request):
#     return render(request,"calculator.html")

# def calculator(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sum=x+y
#     dif=x-y
#     mul=x*y
#     div=x/y
#     return render(request, "result.html",{'num1':x,'num2':y,'sum':sum,'dif':dif,'mul':mul,'div':div})




    


# def about(request):
#     return HttpResponse("Hai, Hellooooo.... Welcome to About page.")

# def contact(request):
#     return render(request,"contact.html")

# def details(request):
#     return HttpResponse("Hai, Hellooooo.... Welcome to Details page.")

# def thanks(request):
#     return render(request,"thanks.html")