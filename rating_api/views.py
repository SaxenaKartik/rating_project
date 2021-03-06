from django.shortcuts import render
# from rest_framework import viewsets
from rating_api import models
from rating_api import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import MyUser, Product, Rate
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
# from rest_auth.registration.views import RegisterView
# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     """ Handle creating and updating users"""
#
#     serializer_class = serializers.UserSerializer
#     queryset = models.MyUser.objects.all()
#
#
# class ProductViewSet(viewsets.ModelViewSet):
#     """ Handle creating and updating products"""
#
#     serializer_class = serializers.ProductSerializer
#     queryset = models.Product.objects.all()
# @transaction.atomic
class login(APIView):
    serializer_class = serializers.UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    # queryset = User.objects.all()

    def get(self, request):

        model = MyUser.objects.all()
        serializer = serializers.UserSerializer
        return Response({'serializer': serializer, 'model': model}, template_name = "registration/login.html")

    # def post(self, request):
    #     pass

# @transaction.atomic
class signup(APIView):
    serializer_class = serializers.UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    #
    def get(self, request):
        model = MyUser.objects.all()
        serializer = serializers.UserSerializer
        return Response({'serializer': serializer, 'model': model}, template_name = "registration/signup.html")

    def post(self, request):
        pass


class product(APIView):
    serializer_class = serializers.UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):
        model = Product.objects.all()
        serializer = serializers.ProductSerializer
        return Response({'serializer': serializer, 'model': model}, template_name = "product/index.html")


class rate(APIView):
    serializer_class = serializers.UserSerializer
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):

        total = set(Product.objects.all())
        rated = Rate.objects.filter(user = request.user).select_related('product')
        rated_products = set()
        for a in rated:
            rated_products.add(a.product)
        model = total.difference(rated_products)
        serializer = serializers.ProductSerializer
        return Response({'serializer': serializer, 'model': model}, template_name = "product/rate.html")

    def post(self, request):
        pass
