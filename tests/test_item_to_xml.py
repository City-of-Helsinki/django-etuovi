import os

from django.test import override_settings
from lxml import etree

from django_etuovi.etuovi import create_element_tree
from django_etuovi.utils.xml import object_to_xml_string
from tests.factories import ItemFactory


def test_all_item_attributes_in_xml_string():
    item = ItemFactory()
    xml_string = object_to_xml_string(item).decode("UTF-8")

    for key in item.__dict__.keys():
        assert key in xml_string

    assert isinstance(item.image, list)
    for key in item.image[0].__dict__.keys():
        assert key in xml_string

    assert isinstance(item.extralink, list)
    for key in item.extralink[0].__dict__.keys():
        assert key in xml_string

    assert isinstance(item.text, list)
    for key in item.text[0].__dict__.keys():
        assert key in xml_string

    assert isinstance(item.coordinate, list)
    for key in item.coordinate[0].__dict__.keys():
        assert key in xml_string

    assert isinstance(item.scontact, list)
    for key in item.scontact[0].__dict__.keys():
        assert key in xml_string


@override_settings(ETUOVI_TRANSFER_ID="test")
def test_validate_xml_against_dtd():
    # DTD downloaded from http://img.cromet.fi/dtds/transferdata.dtd
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)
    dtd = etree.DTD(os.path.join(current_directory, "test_data", "transferdata.dtd"))
    items = ItemFactory.create_batch(2)

    assert dtd.validate(create_element_tree(items))
