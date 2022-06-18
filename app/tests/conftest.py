import pytest
from django.core.management import call_command



@pytest.fixture(autouse=True, scope="function") # noqa:  PT003
def enable_db_access_for_all_tests(db): # noqa:  PT004
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session") # noqa:  PT003
def load_fixture(django_db_setup, django_db_blocker): # noqa:  PT004
    with django_db_blocker.unblock():
        fixtures = (
            'source.json',
            'rates.json',
            'contact-us.json'
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')
