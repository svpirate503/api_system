from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FormData
from .serializers import FormDataSerializer
from django.shortcuts import render


class FormSubmitView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Form data submitted successfully."})
        else:
            return Response(serializer.errors, status=400)

class FormPageView(generics.CreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer

def index(request):
    return render(request,'index.html')