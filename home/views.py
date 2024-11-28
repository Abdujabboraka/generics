from .models import FoodType, Food, Comment
from .serializer import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework import generics, filters, permissions


# Mixin views
class FoodTypeList(generics.ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','id']

    def get_queryset(self):
        query = self.request.query_params.get('query', False)
        if query:
            return Food.objects.filter(name__icontains=query)
        else:
            return Food.objects.all()


class FoodTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # ordering
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','price',]

    def get_queryset(self):
        query = self.request.query_params.get('query', False)
        if query:
            return Food.objects.filter(name__icontains=query)
        else:
            return Food.objects.all()




class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
