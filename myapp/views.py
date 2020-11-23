from django.shortcuts import render

# Create your views here.
def fn_new(request):
    return render(request,'new.html')