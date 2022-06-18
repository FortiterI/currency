from currency.models import ContactUs


def test_sanity():
    assert 200 == 200


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_contact_us_get(client):
    response = client.get('/currency/contact-us/create/')
    assert response.status_code == 200


def test_contact_us_empty_form(client, mailoutbox):
    response = client.post('/currency/contact-us/create/')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'reply_to': ['This field is required.'],
        'subject': ['This field is required.'],
        'body': ['This field is required.']}
    assert len(mailoutbox) == 0


def test_contact_us_valid_form(client, mailoutbox):
    initial_count = ContactUs.objects.count()
    data = {
        'name': 'test',
        'reply_to': 'test@trest.com',
        'subject': "test subject",
        'body': 'test text'
    }
    response = client.post('/currency/contact-us/create/', data=data)
    assert response.status_code == 302
    assert response.url == '/'
    assert len(mailoutbox) == 0  # TODO
    assert ContactUs.objects.count() == initial_count + 1


def test_contact_us_invalid_form(client, mailoutbox):
    initial_count = ContactUs.objects.count()
    data = {
        'name': 'test',
        'reply_to': 'test',
        'subject': "test subject",
        'body': 'test text'
    }
    response = client.post('/currency/contact-us/create/', data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'reply_to': ['Enter a valid email address.']}
    assert len(mailoutbox) == 0
    assert ContactUs.objects.count() == initial_count
