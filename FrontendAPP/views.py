from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status


from .addition import add2_num
from .chatbot import chat1
from .models import AdditionRecord
from .serializers import AddSerializer, ChatSerializer

class IndexAPIView(APIView):
    def get(self, request):
        return render(request, 'FrontendAPP/home.html', {"message" : "Hello, world. You're at the FrontendAPP index."})

class AddAPIView(APIView):
    def post(self, request):
        serializer = AddSerializer(data = request.data)
        if serializer.is_valid():
            num1 = serializer.validated_data['num1']
            num2 = serializer.validated_data['num2']

            result = add2_num(num1, num2)
            AdditionRecord.objects.create(num1 = num1, num2 = num2, result = result)
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
def add_num(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        result = add2_num(num1, num2)
        AdditionRecord.objects.create(num1 = num1, num2 = num2, result = result)

    return render(request, 'FrontendAPP/index.html', {'result': result})
'''
class ChatAPIView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data = request.data)
        if serializer.is_valid():
            user_input = serializer.validated_data['user_input']

            result = chat1(user_input)
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
def chat(request):
    result = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        result = chat1(user_input)
    
    return render(request, 'FrontendAPP/chatbot.html', {'result': result})
'''