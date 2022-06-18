from django.urls import reverse
from rest_framework.test import APIClient
from currency.models import Source, Rate, ContactUs


def test_rates_get_list():
    client = APIClient()
    response = client.get('/api/v1/rates/')
    assert response.status_code == 200
    assert response.json()


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
    source = Source.objects.last()
    data = {
        'currency_type': 'USD',
        'sale': 23,
        'buy': 23,
        'source': source.id,
    }
    response = client.post(path='/api/v1/rates/', data=data)
    assert response.status_code == 201
    assert response.json() == {'id': 4, 'currency_type': 'USD', 'sale': '23.00', 'buy': '23.00', 'source': 3}


def test_rates_patch_valid_data():
    client = APIClient()
    source = Source.objects.last()
    rate = Rate.objects.create(currency_type='USD', sale='23.00', buy='23.00', source=source)
    data = {
        'sale': 140,
    }
    response = client.patch(reverse('api:v1:rate-detail', args=[rate.id]), data=data)
    assert response.status_code == 200
    assert response.json()['sale'] == '140.00'


def test_rates_delete():
    client = APIClient()
    source = Source.objects.last()
    rate = Rate.objects.create(currency_type='USD', sale='23.00', buy='23.00', source=source)
    response = client.delete(reverse('api:v1:rate-detail', args=[rate.id]),)
    assert response.status_code == 204
    assert response.content == b''


def test_contact_us_get_list():
    client = APIClient()
    response = client.get('/api/v1/contactus/')
    assert response.status_code == 200


def test_contact_us_post_empty_data():
    client = APIClient()
    response = client.post(path='/api/v1/contactus/', data={})
    assert response.status_code == 400
    assert response.json() == {'name': ['This field is required.'],
                               'reply_to': ['This field is required.'],
                               'subject': ['This field is required.']
                               }


def test_contact_us_post_valid_data(mailoutbox):
    initial_count = ContactUs.objects.count()
    client = APIClient()
    data = {
        'name': 'test_name',
        'reply_to': 'test.mail@mail.com',
        'subject': 'test'
    }
    response = client.post(reverse('api:v1:contactus-list'), data=data)
    assert response.status_code == 201
    assert response.json()
    assert len(mailoutbox) == 0  # TODO
    assert ContactUs.objects.count() == initial_count + 1


def test_contact_us_post_invalid_data():
    client = APIClient()
    data = {
        'name': 'test_name',
        'reply_to': '',
        'subject': 'test'
    }
    response = client.post(reverse('api:v1:contactus-list'), data=data)
    assert response.status_code == 400
    assert response.json() == {'reply_to': ['This field may not be blank.']}


def test_contact_us_patch_valid_data():
    client = APIClient()
    contact_us = ContactUs.objects.last()
    data = {
        'name': 'test_name2',
        'reply_to': 'test.mail@mail.com',
        'subject': 'test'
    }
    response = client.patch(reverse('api:v1:contactus-detail', args=[contact_us.id]), data=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'test_name2'


def test_contact_us_delete():
    initial_count = ContactUs.objects.count()
    client = APIClient()
    contact_us = ContactUs.objects.last()
    response = client.delete(reverse('api:v1:contactus-detail', args=[contact_us.id]))
    assert response.status_code == 204
    assert response.content == b''
    assert ContactUs.objects.count() == initial_count - 1
