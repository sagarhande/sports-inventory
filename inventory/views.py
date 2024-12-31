from rest_framework import viewsets, status
from rest_framework import serializers
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        quantity = self.request.query_params.get('quantity', None)
        try:
            if quantity is not None:
                queryset = queryset.filter(quantity=quantity)
        except ValueError as e:
            raise serializers.ValidationError({'quantity': 'Invalid quantity value'})
        return queryset

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        response.data = {
            'error': 'Request failed',
            'details': response.data
        }
        response.status_code = status.HTTP_400_BAD_REQUEST if response.status_code == 200 else response.status_code
        return response
