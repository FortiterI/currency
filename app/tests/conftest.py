import pytest


@pytest.fixture(autouse=True, scope="function") # noqa:  PT003
def enable_db_access_for_all_tests(db): # noqa:  PT004
    """
    give access to database for all tests
    """
