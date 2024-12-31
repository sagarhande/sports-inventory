from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Item

class TestItemViewSet(APITestCase):
    def setUp(self):
        # Create some sample items
        Item.objects.create(name="Cricket Bat", description="Cricket Bat", quantity=5, price=4000)
        Item.objects.create(name="Cricket Ball", description="Cricket Ball", quantity=0, price=500)
        Item.objects.create(name="Badminton Racket", description="Badminton Racket", quantity=1, price=1200)
        Item.objects.create(name="Shuttle", description="Shuttle", quantity=0, price=80)

    def test_list_items(self):
        """
        Ensure we can list items.
        """
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_filter_items_by_quantity(self):
        """
        Ensure we can filter items by quantity.
        """
        url = reverse('item-list') + '?quantity=0'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['quantity'], 0)
