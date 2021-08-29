from django.conf.urls import url
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTest(SimpleTestCase):
    def test_home_psge_status(self):
        #Arrange
        url = reverse('home')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        #Arrange
        url = reverse('about')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        #Arrange
        url = reverse('home')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_templete(self):
        #Arrange
        url = reverse('about')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')



