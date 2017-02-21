import pytest

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from metarecord.models import Action, Attribute, AttributeValue, Function, Phase, Record


@pytest.fixture
def parent_function():
    return Function.objects.create(name='test parent function', function_id='00')


@pytest.fixture
def function(parent_function):
    return Function.objects.create(name='test function', function_id='00 00', parent=parent_function)


@pytest.fixture
def second_function(parent_function):
    return Function.objects.create(name='second test function', function_id='00 01', parent=parent_function)


@pytest.fixture
def phase(function):
    return Phase.objects.create(name='test phase', function=function)


@pytest.fixture
def action(phase):
    return Action.objects.create(name='test action', phase=phase)


@pytest.fixture
def record(action):
    return Record.objects.create(name='test record', action=action)


@pytest.fixture
def choice_attribute():
    return Attribute.objects.create(name='test choice attribute', identifier='ChoiceAttr')


@pytest.fixture
def free_text_attribute():
    return Attribute.objects.create(name='test free text attribute', identifier='FreeTextAttr')


@pytest.fixture
def choice_value_1(choice_attribute):
    return AttributeValue.objects.create(value='test choice value 1', attribute=choice_attribute)


@pytest.fixture
def choice_value_2(choice_attribute):
    return AttributeValue.objects.create(value='test choice value 2', attribute=choice_attribute)


@pytest.fixture
def free_text_value_1(free_text_attribute):
    return AttributeValue.objects.create(value='test free text value 1', attribute=free_text_attribute)


@pytest.fixture
def free_text_value_2(free_text_attribute):
    return AttributeValue.objects.create(value='test free text value 2', attribute=free_text_attribute)


@pytest.fixture
def template():
    return Function.objects.create(name='test template', is_template=True)


@pytest.fixture
def user():
    return get_user_model().objects.create(username='test_user')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_api_client(user):
    api_client = APIClient()
    api_client.force_authenticate(user)
    return api_client
