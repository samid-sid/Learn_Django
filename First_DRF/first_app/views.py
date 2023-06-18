from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets

from .models import Students,Course
from .serializer import Student_Serialize , Course_Serialize

# Create your views here.





class Student_view(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = Student_Serialize


# class Student_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = Student_Serialize



class Course_view(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Course_Serialize


# class Course_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = Course_Serialize



# class Student_view(APIView):
#     def get(self,request):
#         student_data = Students.objects.all()
#         serializer = Student_Serialize(student_data,many = True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = Student_Serialize(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class Student_Detail(APIView):
#     def get(self,request,pk):
#         obj = Students.objects.get(pk= pk)
#         serializer = Student_Serialize(obj)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         obj = Students.objects.get(pk=pk)
#         serializer = Student_Serialize(obj,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
#     def delete(self,request, pk):
#         obj = Students.objects.get(pk=pk)
        
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)