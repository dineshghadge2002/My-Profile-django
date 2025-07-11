from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .addition import add2_num


def index(request):
    return HttpResponse("Hello, world. You're at the FrontendAPP index.")

def add_num(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        result = add2_num(num1, num2)

    return render(request, 'FrontendAPP/add.html', {'result': result})