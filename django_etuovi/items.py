from dataclasses import dataclass
from datetime import date
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
class Scontact(BaseClass):
    scontact_name: str
    scontact_title: str
    scontact_itempage_email: str
    scontact_mobilephone: str
    scontact_phone: str
    scontact_image_url: str

    class Meta:
        element_name = "scontact"


@dataclass
class Item(BaseClass):
    buildyear: int
    charges_parkingspace: Decimal
    chargesfinancebasemonth: Decimal
    chargesmaintbasemonth: Decimal
    chargeswater_period: str
    condition_name: Condition
    country: Country
    coordinate: List[Coordinate]
    currency_code: str  # EUR is only supported currency atm.
    cust_itemcode: str
    debtfreeprice: Decimal
    energyclass: str
    extralink: List[ExtraLink]
    floors: int
    holdingtype: HoldingType
    image: List[Image]
    itemgroup: ItemGroup
    livingaream2: Decimal
    loclvlid: int  # If coordinate exists, this needs to be 1.
    locsourceid: int  # If coordinate exists, this needs to be 4.
    lotarea: Decimal
    lotareaunitcode: str
    lotholding: str
    postcode: str
    price: Decimal
    price_m2: Decimal
    quarteroftown: str
    realtygroup: RealtyGroup
    realtyidentifier: str
    realty_itemgroup: ItemGroup
    realtytype: RealtyType
    realtyoption: List[str]
    rc_parkingspace_count: int
    roomcount: int
    scontact: List[Scontact]
    showingdate: date
    showing_date2: date
    street: str
    supplier_source_itemcode: str
    text: List[Text]
    town: str
    tradetype: TradeType
    zoningname: str

    class Meta:
        element_name = "item"
