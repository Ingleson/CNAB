from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer

class StoreView(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
