from django.urls import reverse
from rest_framework.test import APIClient
from currency import model_choises as mch

from currency.models import Source, Rate


def test_rates_get_list():
    client = APIClient()
    response = client.get('/api/v1/rates/')
    assert response.status_code == 200


def test_rates_post_empty_data():
    client = APIClient()
    response = client.post(path='/api/v1/rates/', data={})
    assert response.status_code == 400
    assert response.json() == {'currency_type': ['This field is required.'],
                               'sale': ['This field is required.'],
                               'buy': ['This field is required.'],
                               'source': ['This field is required.']}


def test_rates_post_valid_data():
    client = APIClient()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]
    data = {
        'currency_type': 'USD',
        'sale': 23,
        'buy': 23,
        'source': source.id,
    }
    response = client.post(path='/api/v1/rates/', data=data)
    assert response.status_code == 201
    assert response.json() == {'id': 1, 'currency_type': 'USD', 'sale': '23.00', 'buy': '23.00', 'source': 1}


def test_rates_patch_valid_data():
    client = APIClient()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]
    rate = Rate.objects.create(currency_type='USD', sale='23.00', buy='23.00', source=source)
    data = {
        'sale': 140,
    }
    response = client.patch(reverse('api:v1:rate-detail', args=[rate.id]), data=data)
    assert response.status_code == 200
    assert response.json()['sale'] == '140.00'


def test_rates_delete():
    client = APIClient()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]
    rate = Rate.objects.create(currency_type='USD', sale='23.00', buy='23.00', source=source)
    response = client.delete(reverse('api:v1:rate-detail', args=[rate.id]),)
    assert response.status_code == 204
    assert response.content == b''
