import time
from ftplib import FTP
from xml.etree.ElementTree import ElementTree

from django.conf import settings
from lxml import etree


def get_filename():
    # TODO change this when actual filename confirmed.
    return "EO_realty2_{}.xml".format(
        time.strftime("%Y%m%d%H%M%S"),
    )


def send_items(items, transfer_type="all"):
    root = etree.Element("transferData", version="1.0")
    group = etree.Element(
        "transferGroup", type=transfer_type, name=settings.ETUOVI_TRANSFER_ID
    )
    root.append(group)
    for item in items:
        group.append(item.to_etree())
    tree = ElementTree(group)
    filename = get_filename()
    tree.write(filename, encoding="utf-8", xml_declaration=True)

    session = FTP(
        host=settings.ETUOVI_FTP_HOST,
        user=settings.ETUOVI_USER,
        passwd=settings.ETUOVI_PASSWORD,
    )
    # TODO Confirm if the temp filename is required and if quit is required.
    session.storbinary("{}.temp".format(filename), open(filename, "rb"))
    session.rename("{}.temp".format(filename), filename)
    session.quit()
