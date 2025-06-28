from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,'main/index.html')

def about(request):
    return render('<h4>TEST123</h4>')
