import requestspro


def test_can_access_urllib3_attribute():
    requestspro.packages.urllib3


def test_can_access_idna_attribute():
    requestspro.packages.idna


def test_can_access_chardet_attribute():
    requestspro.packages.chardet
