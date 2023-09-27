from .models import User, Product, ProductAccess, Lesson, LessonStatus
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum

# Create your views here.


@api_view(["GET"])
def get_lessons(request):

    user_id = request.data["id"]

    product_accesses = ProductAccess.objects.filter(user=user_id)
    products_with_access = product_accesses.values_list('product', flat=True)

    lessons = Lesson.objects.filter(products__in=products_with_access)
    lesson_status = LessonStatus.objects.filter(lesson__in=lessons).values(
        "lesson", "viewed", "viewed_time")
    

    return Response({"lessons": lesson_status})


@api_view(["GET"])
def get_lessons_of_product(request, id):

    user_id = request.data['id']

    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"msg: product not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        product_access = ProductAccess.objects.filter(
            user=user_id, product=product).values_list('product', flat=True)
    except ProductAccess.DoesNotExist:
        return Response({"msg: Doesn't have access"}, status=status.HTTP_403_FORBIDDEN)

    lessons = Lesson.objects.filter(products__in=product_access)
    lesson_status = LessonStatus.objects.filter(lesson__in=lessons).values(
        "id", "viewed", "viewed_time", "last_viewed_at")
    
    print(lesson_status)
    
    return Response({"lessons": lesson_status})


@api_view(['GET'])
def product_statistics(request):

    products = Product.objects.all()
    stats = []

    for product in products:
        lesson = Lesson.objects.filter(products=product)
        lesson_status = LessonStatus.objects.filter(lesson__in=lesson)
        viewed_lessons = lesson_status.filter(viewed=True)
        total_view_time = lesson_status.aggregate(Sum('viewed_time'))['viewed_time__sum']
        total_students = lesson_status.values('user').distinct().count()
        purchase_percentage =(total_students / User.objects.count()) * 100 if User.objects.count() > 0 else 0

        stats.append({
            "product_id": product.id,
            "product_name": product.name,
            "total_viewed_lessons": viewed_lessons.count(),
            "total_viewing_time_seconds": total_view_time,
            "total_students": total_students,
            "purchase_percentage": purchase_percentage,
        })

    return Response({"stats": stats})

    