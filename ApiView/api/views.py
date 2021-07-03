from django.shortcuts import render

from . seri import StudentSerializer
from rest_framework. response import Response
from .models import Student
from rest_framework import status
from rest_framework.views import APIView

class student_api(APIView): # just convert @api_viwe to class base viwe
    def get(self,request,id=None,format=None):
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)  # convert it in native python data
            return Response(serializer.data)  # data is varibale were serializer is store it will convert it into json and send response
        stu = Student.objects.all()  # if id is not given then it will excute
        serializer = StudentSerializer(stu, many=True)  # many need to write bcoz its query set
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)  # it will make it complex qury
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)  # it will give nonfield erroe

    def put(self,request,id,format=None):
        if request.method == 'PUT':
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'complete done put request'})
            return Response(serializer.errors)

    def patch(self,request,id,format=None):
        if request.method == 'PATCH':
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'partialy update  done put request'})
            return Response(serializer.errors)



    def delete(self,request,id,format=None):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'deeletd data '})
















# Create your views here.






    # Not: if you want for brower api you can remove id bcoz it getting from url we used third party app that we get id
    #
    # def student_api(request,id=None): only make this changes for browesr api
    #
    # if request.method == 'GET':
    #     id = id
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)  # convert it in native python data
    #         return Response(
    #             serializer.data)  # data is varibale were serializer is store it will convert it into json and send response
    #     stu = Student.objects.all()  # if id is not given then it will excute
    #     serializer = StudentSerializer(stu, many=True)  # many need to write bcoz its query set
    #     return Response(serializer.data)




