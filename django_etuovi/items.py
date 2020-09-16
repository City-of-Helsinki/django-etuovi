from dataclasses import dataclass
from decimal import Decimal
from typing import List

from django_etuovi.enums import (
    Country,
    HoldingType,
    ItemGroup,
    LinkType,
    RealtyGroup,
    RealtyImageType,
    RealtyType,
    TradeType,
)
from django_etuovi.utils import object_to_etree


class BaseClass:
    def to_etree(self, item_type="update"):
        return object_to_etree(self, item_type)


@dataclass
class ExtraLink(BaseClass):
    link_url: str
    link_urltitle: str
    linktype_name: LinkType

    class Meta:
        element_name = "extralink"


@dataclass
class Image(BaseClass):
    image_desc: str
    image_realtyimagetype: RealtyImageType
    image_seq: str
    image_transfer_id: str
    image_transfer_source: str
    image_url: str

    class Meta:
        element_name = "image"


@dataclass
class Item(BaseClass):
    country: Country
    currency_code: str
    cust_itemcode: str
    debtfreeprice: Decimal
    holdingtype: HoldingType
    image: List[Image]
    itemgroup: ItemGroup
    extralink: List[ExtraLink]
    postcode: str
    price: Decimal
    quarteroftown: str
    realtygroup: RealtyGroup
    realty_itemgroup: ItemGroup
    realtytype: RealtyType
    roomcount: int
    street: str
    supplier_source_itemcode: str
    town: str
    tradetype: TradeType

    class Meta:
        element_name = "item"
