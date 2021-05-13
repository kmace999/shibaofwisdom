
from app.shiba import shiba_file_name


advicestr = "avocado"
shibalink = "https://cdn.shibe.online/shibes/c64a387d249909f280ebf3b2cb13b352c1539882.jpg"


def test_shiba_file_name():
    assert shiba_file_name("random",shibalink,advicestr) == "random_c64a387d249909f280ebf3b2cb13b352c1539882.jpg"
    assert shiba_file_name("ask",shibalink,advicestr) == "avocado_c64a387d249909f280ebf3b2cb13b352c1539882.jpg"
