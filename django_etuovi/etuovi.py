import time
from ftplib import FTP
from typing import List
from xml.etree.ElementTree import ElementTree

from django.conf import settings
from lxml import etree

from django_etuovi.items import BaseClass


def create_element_tree(items: List[BaseClass]) -> etree.Element:
    root = etree.Element("transferData", version="1.0")
    group = etree.Element("transferGroup", type="all", name=settings.ETUOVI_TRANSFER_ID)
    root.append(group)
    for item in items:
        group.append(item.to_etree())
    return root


def get_filename() -> str:
    return "{}_all_{}.xml".format(
        settings.ETUOVI_COMPANY_NAME,
        time.strftime("%Y%m%d%H%M%S"),
    )


def get_session() -> FTP:
    return FTP(
        host=settings.ETUOVI_FTP_HOST,
        user=settings.ETUOVI_USER,
        passwd=settings.ETUOVI_PASSWORD,
    )


def send_items(items: List[BaseClass]) -> None:
    element_tree = ElementTree(create_element_tree(items))
    filename = get_filename()
    element_tree.write(filename, encoding="ISO-8859-1", xml_declaration=True)

    session = get_session()
    session.storbinary("{}.temp".format(filename), open(filename, "rb"))
    session.rename("{}.temp".format(filename), filename)
    session.quit()
