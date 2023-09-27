from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_lessons),
    path('products/<int:id>', views.get_lessons_of_product),
    path('products/get_stats', views.product_statistics)
]
