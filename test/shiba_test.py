
from app.shiba_app import get_advice
import random

# TODO: test the code

def test_format_usd():
    #result = format_usd(1999.99)
    assert format_usd(1999.99) == "$1,999.99"

mock_products_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
mock_products_df = read_csv(mock_products_filepath)
mock_products = mock_products_df.to_dict("records")

def test_find_product():
    #with valid product id, returns the product info
    valid_result = find_product("8", mock_products)
    assert valid_result =={
        'aisle':'Aisle C',
        'department':'snacks',
        'id': 8,
        'name': 'Product 8',
        'price': 10.0
    }
    #with invalid product id, returns None:
    invalid_result = find_product("999999", mock_products)
    assert invalid_result == None


def test_get_advice():
