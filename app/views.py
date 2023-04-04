from django.shortcuts import render

# Create your views here.
def mdb(request):
    return render(request,'md5.html')

def child(request):
    return render(request,'child.html')
