from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from mpesa_api.views import getAccessToken, lipa_na_mpesa_online, pull_transaction
import json

'''
class LipaTests(SimpleTestCase):

    def test_url_is_resolved(self):
        url = reverse('lipa_na_mpesa')
        self.assertEquals(resolve(url).func, lipa_na_mpesa_online)



    def test_url_is_resolved(self):
        url = reverse('access_token')
        self.assertEquals(resolve(url).func, getAccessToken)




    def test_url_is_resolved(self):
        url = reverse('pull')
        self.assertEquals(resolve(url).func, pull_transaction)

'''

class ViewsTest(TestCase):
    def pull_transaction(self):
        client = Client()
        response = client.get(reverse('pull'))
        self.assertEquals(response.status_code, 200)













    def test_get_access_token(self):
        client = Client()
        response = client.get(reverse('access_token'))
        self.assertEquals(response.status_code, 200)







