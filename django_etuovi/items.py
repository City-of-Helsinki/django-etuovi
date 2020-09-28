from dataclasses import dataclass
from decimal import Decimal
from typing import List

from django_etuovi.enums import (
    Condition,
    Country,
    HoldingType,
    ItemGroup,
    LinkType,
    RealtyGroup,
    RealtyImageType,
    RealtyType,
    TextKey,
    TextLanguage,
    TradeType,
)


class BaseClass:
    def to_etree(self):
        from django_etuovi.utils import object_to_etree

        return object_to_etree(self)


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
class Text(BaseClass):
    text_key: TextKey
    text_value: str
    text_language: TextLanguage

    class Meta:
        element_name = "text"


@dataclass
class Coordinate(BaseClass):
    lat: Decimal  # WGS84
    lon: Decimal  # WGS84

    class Meta:
        element_name = "coordinate"


@dataclass
class Item(BaseClass):
    buildyear: int
    chargesmaintbasemonth: Decimal
    chargeswater2: Decimal
    chargeswater2_period: str
    condition_name: Condition
    country: Country
    coordinate: List[Coordinate]
    currency_code: str  # EUR is only supported currency atm.
    cust_itemcode: str
    debtfreeprice: Decimal
    dgitemcode: str
    energyclass: str
    holdingtype: HoldingType
    image: List[Image]
    itemgroup: ItemGroup
    extralink: List[ExtraLink]
    livingaream2: Decimal
    loclvlid: int  # If coordinate exists, this needs to be 1.
    locsourceid: int  # If coordinate exists, this needs to be 4.
    postcode: str
    price: Decimal
    quarteroftown: str
    realtygroup: RealtyGroup
    realtyidentifier: str
    realty_itemgroup: ItemGroup
    realtytype: RealtyType
    realtyoption: List[str]
    roomcount: int
    street: str
    supplier_source_itemcode: str
    text: List[Text]
    town: str
    tradetype: TradeType

    class Meta:
        element_name = "item"
