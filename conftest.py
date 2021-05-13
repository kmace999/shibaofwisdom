
#COMMENTS FROM CONFTEST.PY IN CODE BASE CLEANUP
# this is the conftest.py file
#
# ... which A) helps pytest collect and run all tests in the test dir
# ... and B) can contain some setup code we can use in our tests
#

#
# FIXTURES
#
# ... let us cache the result of an expensive operation (like a network request)
# ... and share it across multiple tests, without making additional requests.
# ... this minimizes the number of network requests and reduces the cost of running tests.
#

#import pytest
#
#@pytest.fixture(scope="module")
#def parsed_googl_response():
#    return "TODO: FETCH AND PARSE SOME REAL LIVE DATA"

#
# MOCK DATA
#
advicestr = "avocado"
shibalink = "https://cdn.shibe.online/shibes/c64a387d249909f280ebf3b2cb13b352c1539882.jpg"
