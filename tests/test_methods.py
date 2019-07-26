from mollie.api.objects.method import Method

from .utils import assert_list_object


def test_list_methods(client, response):
    """Retrieve a list of available payment methods."""
    response.get('https://api.mollie.com/v2/methods', 'methods_list')

    methods = client.methods.list()
    assert_list_object(methods, Method)


def test_method_get(client, response):
    """Retrieve a single payment method by ID."""
    response.get('https://api.mollie.com/v2/methods/ideal', 'method_get_ideal')

    method = client.methods.get('ideal')
    assert isinstance(method, Method)
    assert method.id == Method.IDEAL
    assert method.minimum_amount == {'currency': 'EUR', 'value': '0.01'}
    assert method.maximum_amount == {'currency': 'EUR', 'value': '50000.00'}
    assert method.description == 'iDEAL'
    assert method.image_svg == 'https://www.mollie.com/external/icons/payment-methods/ideal.svg'
    assert method.image_size1x == 'https://www.mollie.com/external/icons/payment-methods/ideal.png'
    assert method.image_size2x == 'https://www.mollie.com/external/icons/payment-methods/ideal%402x.png'


def test_method_get_missing_images(client, response):
    """Ensure that retrieving image URLs doesn't break when URLs are missing."""
    response.get('https://api.mollie.com/v2/methods/ideal', 'method_get_ideal_wrong_images')

    method = client.methods.get('ideal')
    assert method.image_svg is None
    assert method.image_size1x is None
    assert method.image_size2x is None
