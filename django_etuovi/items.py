from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

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
        from django_etuovi.utils.xml import object_to_etree

        return object_to_etree(self)


@dataclass
class ExtraLink(BaseClass):
    link_url: str
    linktype_name: LinkType
    link_urltitle: Optional[str] = None

    class Meta:
        element_name = "extralink"


@dataclass
class Image(BaseClass):
    image_realtyimagetype: RealtyImageType
    image_seq: str
    image_transfer_id: str
    image_transfer_source: str
    image_url: str
    image_desc: Optional[str] = None

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
    scontact_name: Optional[str] = None
    scontact_title: Optional[str] = None
    scontact_itempage_email: Optional[str] = None
    scontact_mobilephone: Optional[str] = None
    scontact_phone: Optional[str] = None
    scontact_image_url: Optional[str] = None

    class Meta:
        element_name = "scontact"


@dataclass
class Item(BaseClass):
    country: Country
    cust_itemcode: str
    debtfreeprice: Decimal
    holdingtype: HoldingType
    itemgroup: ItemGroup
    postcode: str
    price: Decimal
    realtygroup: RealtyGroup
    realty_itemgroup: ItemGroup
    realtytype: RealtyType
    roomcount: int
    supplier_source_itemcode: str
    town: str
    tradetype: TradeType
    buildyear: Optional[int] = None
    charges_parkingspace: Optional[Decimal] = None
    chargesfinancebasemonth: Optional[Decimal] = None
    chargesmaintbasemonth: Optional[Decimal] = None
    chargeswater_period: Optional[str] = None
    condition_name: Optional[Condition] = None
    coordinate: Optional[List[Coordinate]] = None
    currency_code: Optional[str] = None  # EUR is only supported currency atm.
    energyclass: Optional[str] = None
    extralink: Optional[List[ExtraLink]] = None
    floors: Optional[int] = None
    image: Optional[List[Image]] = None
    livingaream2: Optional[Decimal] = None
    loclvlid: Optional[int] = None  # If coordinate exists, this needs to be 1.
    locsourceid: Optional[int] = None  # If coordinate exists, this needs to be 4.
    lotarea: Optional[Decimal] = None
    lotareaunitcode: Optional[str] = None
    lotholding: Optional[str] = None
    price_m2: Optional[Decimal] = None
    quarteroftown: Optional[str] = None
    realtyidentifier: Optional[str] = None
    realtyoption: Optional[List[str]] = None
    rc_parkingspace_count: Optional[int] = None
    scontact: Optional[List[Scontact]] = None
    showingdate: Optional[datetime] = None
    showing_date2: Optional[datetime] = None
    street: Optional[str] = None
    text: Optional[List[Text]] = None
    zoningname: Optional[str] = None

    class Meta:
        element_name = "item"
