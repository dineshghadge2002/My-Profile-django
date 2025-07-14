from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .addition import add2_num
from .models import AdditionRecord


def index(request):
    return HttpResponse("Hello, world. You're at the FrontendAPP index.")

def add_num(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        result = add2_num(num1, num2)
        AdditionRecord.objects.create(num1 = num1, num2 = num2, result = result)

    return render(request, 'FrontendAPP/index.html', {'result': result})

