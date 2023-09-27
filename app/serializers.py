from rest_framework import serializers
from .models import User, Product, Lesson, LessonStatus, ProductAccess

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Product
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Lesson
        fields = "__all__"

class LessonStatusSerializer(serializers.ModelSerializer):

    class Meta: 
        model = LessonStatus
        fields = "__all__"
    
class ProductAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAccess
        fields = "__all__"