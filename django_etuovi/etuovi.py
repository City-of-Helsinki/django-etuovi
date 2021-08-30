import time
from ftplib import FTP
from os import path
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


def create_xml_file(items: List[BaseClass], file_path: str = ".") -> str:
    element_tree = ElementTree(create_element_tree(items))
    filename = get_filename()
    element_tree.write(
        path.join(file_path, filename), encoding="UTF-8", xml_declaration=True
    )
    return filename


def send_items(file_path, filename) -> None:
    session = get_session()
    with open(path.join(file_path, filename), "rb") as f:
        session.storbinary("STOR {}.temp".format(filename), f)
        session.rename("{}.temp".format(filename), filename)
        session.quit()
