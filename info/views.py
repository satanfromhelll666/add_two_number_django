from django.shortcuts import render

# Create your views here.


def home(request):

    context = {

        
    }

    return render(request,'info/main.html',context)


def add(request):


    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    result = val1 + val2

    context = {

        'result' : result
    }

    return render(request,'info/result.html',context)

    
