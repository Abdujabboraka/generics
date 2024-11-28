from django.urls import path

from .views import FoodTypeList, FoodTypeDetail, FoodList, FoodDetail ,CommentList, CommentDetail

urlpatterns = [
    path('foodtypes/', FoodTypeList.as_view(), name='foodtypes-list'),
    path('foodtypes/<int:pk>/', FoodTypeDetail.as_view(), name='foodtype-detail'),
    path('foods/', FoodList.as_view(), name='foods-list'),
    path('foodsgen/', FoodList.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodDetail.as_view(), name='food-detail'),
    path('comments/', CommentList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]