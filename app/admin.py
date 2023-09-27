from django.contrib import admin
from .models import User, Product, Lesson, LessonStatus, ProductAccess

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductAccess)
admin.site.register(Lesson)
admin.site.register(LessonStatus)