import factory
from factory import fuzzy

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
from django_etuovi.items import ExtraLink, Image, Item


class ImageFactory(factory.Factory):
    class Meta:
        model = Image

    image_desc = fuzzy.FuzzyText(length=16)
    image_realtyimagetype = RealtyImageType.MAIN_IMAGE
    image_seq = fuzzy.FuzzyText(length=16)
    image_transfer_id = fuzzy.FuzzyText(length=16)
    image_transfer_source = fuzzy.FuzzyText(length=16)
    image_url = fuzzy.FuzzyText(length=16)


class ExtraLinkFactory(factory.Factory):
    class Meta:
        model = ExtraLink

    link_url = fuzzy.FuzzyText(length=16)
    link_urltitle = fuzzy.FuzzyText(length=16)
    linktype_name = LinkType.NEW_HOUSE


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    country = Country.FINLAND
    currency_code = fuzzy.FuzzyText(length=16)
    cust_itemcode = fuzzy.FuzzyText(length=16)
    debtfreeprice = fuzzy.FuzzyDecimal(0, 1000000)
    holdingtype = HoldingType.OWN
    image = factory.List([factory.SubFactory(ImageFactory)])
    itemgroup = ItemGroup.DWELLING
    extralink = factory.List([factory.SubFactory(ExtraLinkFactory)])
    postcode = fuzzy.FuzzyText(length=16)
    price = fuzzy.FuzzyDecimal(0, 1000000)
    quarteroftown = fuzzy.FuzzyText(length=16)
    realtygroup = RealtyGroup.RESIDENTIAL_APARTMENT
    realty_itemgroup = ItemGroup.DWELLING
    realtytype = RealtyType.BLOCK_OF_FLATS
    roomcount = fuzzy.FuzzyInteger(0, 100)
    street = fuzzy.FuzzyText(length=16)
    supplier_source_itemcode = fuzzy.FuzzyText(length=16)
    town = fuzzy.FuzzyText(length=16)
    tradetype = TradeType.SALE
