from decimal import Decimal
from typing import Union

from lxml import etree

from django_etuovi.items import BaseClass


def get_name(obj: BaseClass) -> str:
    if hasattr(obj, "Meta") and hasattr(obj.Meta, "element_name"):
        return obj.Meta.element_name
    else:
        return obj.__class__.__name__.lower()


def get_root(name: str) -> etree.Element:
    if name == "item":
        return etree.Element(
            name,
            type="update",
            itemType="realty2",
            locale="FI",
            dataGroup="DEFAULT",
        )
    else:
        return etree.Element("property")


def create_value_property(
    key: Union[str, None], value: Union[int, str, Decimal], root: etree.Element
) -> None:
    if key is None:
        property_element = etree.Element("property")
    else:
        property_element = etree.Element("property", name=key)
    value_element = etree.Element("value")
    property_element.append(value_element)
    # Don't want to stringify None.
    value_element.text = str(value) if value is not None else value
    root.append(property_element)


def handle_property(
    key: Union[str, None], value: Union[int, str, Decimal], root: etree.Element
) -> None:
    if isinstance(value, BaseClass):
        el = value.to_etree()
        root.append(el)
    else:
        # value is a literal attribute
        create_value_property(key, value, root)


def get_property_root(
    key: str, value: Union[int, str, Decimal], root: etree.Element
) -> etree.Element:
    if isinstance(value, BaseClass):
        property_name = get_name(value)
        property_root = etree.Element("property", name=property_name)
        root.append(property_root)
    else:
        # value is a literal attribute
        property_root = etree.Element("property", name=key)
        root.append(property_root)
    return property_root


def handle_list_property(key: str, list_value: list, root: etree.Element) -> None:
    property_root = None
    for value in list_value:
        if property_root is None:
            # Use the same property root for all the list members.
            property_root = get_property_root(key, value, root)
        handle_property(None, value, property_root)


def object_to_etree(obj: BaseClass) -> etree.Element:
    name = get_name(obj)
    root = get_root(name)

    for key, value in obj.__dict__.items():
        if isinstance(value, list):
            handle_list_property(key, value, root)
        else:
            handle_property(key, value, root)
    return root


def object_to_xml_string(obj: BaseClass, encoding: str = "ISO-8859-1") -> bytes:
    root = obj.to_etree()

    return etree.tostring(
        root, encoding=encoding, xml_declaration=True, pretty_print=True
    )
