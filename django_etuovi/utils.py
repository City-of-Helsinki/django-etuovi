from lxml import etree


def object_to_etree(obj, item_type="update"):
    if hasattr(obj, "Meta") and hasattr(obj.Meta, "element_name"):
        name = obj.Meta.element_name
    else:
        name = obj.__class__.__name__.lower()
    if name == "item":
        root = etree.Element(
            name,
            type=item_type,
            itemType="realty2",
            locale="FI",
            dataGroup="DEFAULT",
        )
    else:
        property_root = etree.Element("property", name=name)
        root = etree.Element("property")
        property_root.append(root)
    for key, val in obj.__dict__.items():
        if hasattr(val, "to_etree") and callable(getattr(val, "to_etree")):
            el = val.to_etree()
            root.append(el)
        else:
            el = etree.Element("property", name=key)
            value = etree.Element("value")
            el.append(value)
            value.text = str(val) if val is not None else val
            root.append(el)
    return root


def object_to_xml_string(obj, encoding="utf-8"):
    root = obj.to_etree()

    return etree.tostring(
        root, encoding=encoding, xml_declaration=True, pretty_print=True
    )
