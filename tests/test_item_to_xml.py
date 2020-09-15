from django_etuovi.utils import object_to_xml_string
from tests.factories import ItemFactory


def test_all_item_attributes_in_xml_string():
    item = ItemFactory()
    xml_string = object_to_xml_string(item).decode("utf-8")

    for key in item.__dict__.keys():
        assert key in xml_string

    assert isinstance(item.image, list)
    for key in item.image[0].__dict__.keys():
        assert key in xml_string

    assert isinstance(item.extralink, list)
    for key in item.extralink[0].__dict__.keys():
        assert key in xml_string
