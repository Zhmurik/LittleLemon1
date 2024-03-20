from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):

    def setUp(self):
        self.item1 = Menu.objects.create(title='Soup', price=10, inventory=20)
        self.item2 = Menu.objects.create(title='Sushi', price=50, inventory=5)
        self.item3 = Menu.objects.create(title='Rice', price=5, inventory=20)

    def test_getall(self):
        all_items = Menu.objects.all()
        self.assertEqual(list(all_items), [self.item1, self.item2, self.item3])

    def test_get(self):
        menu_item = Menu.objects.get(title='Sushi')
        print(menu_item)
        self.assertEqual(menu_item, self.item2)
