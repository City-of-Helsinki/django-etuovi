import string
import factory
from django.utils import timezone
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
from django_etuovi.items import Coordinate, ExtraLink, Image, Item, Scontact, Text
from factory import fuzzy


class ImageFactory(factory.Factory):
    class Meta:
        model = Image

    image_desc = fuzzy.FuzzyText()
    image_realtyimagetype = fuzzy.FuzzyChoice([c for c in RealtyImageType])
    image_seq = fuzzy.FuzzyText()
    image_transfer_id = fuzzy.FuzzyText()
    image_transfer_source = fuzzy.FuzzyText()
    image_url = fuzzy.FuzzyText()


class ExtraLinkFactory(factory.Factory):
    class Meta:
        model = ExtraLink

    link_url = fuzzy.FuzzyText()
    link_urltitle = fuzzy.FuzzyText()
    linktype_name = fuzzy.FuzzyChoice([c for c in LinkType])


class TextFactory(factory.Factory):
    class Meta:
        model = Text

    text_key = fuzzy.FuzzyChoice([c for c in TextKey])
    text_value = fuzzy.FuzzyText()
    text_language = fuzzy.FuzzyChoice([c for c in TextLanguage])


class CoordinateFactory(factory.Factory):
    class Meta:
        model = Coordinate

    lat = fuzzy.FuzzyDecimal(-90, 90)
    lon = fuzzy.FuzzyDecimal(-180, 180)


class ScontactFactory(factory.Factory):
    class Meta:
        model = Scontact

    scontact_name = fuzzy.FuzzyText()
    scontact_title = fuzzy.FuzzyText()
    scontact_itempage_email = fuzzy.FuzzyText()
    scontact_mobilephone = fuzzy.FuzzyText()
    scontact_phone = fuzzy.FuzzyText()
    scontact_image_url = fuzzy.FuzzyText()


class ItemFactory(factory.Factory):
    class Meta:
        model = Item

    buildyear = fuzzy.FuzzyInteger(0, 9999999999)
    charges_parkingspace = fuzzy.FuzzyDecimal(0, 99999999999)
    chargesfinancebasemonth = fuzzy.FuzzyDecimal(0, 99999999999)
    chargesmaintbasemonth = fuzzy.FuzzyDecimal(0, 99999999999)
    chargeswater_period = fuzzy.FuzzyText()
    condition_name = fuzzy.FuzzyChoice([c for c in Condition])
    coordinate = factory.List([factory.SubFactory(CoordinateFactory)])
    country = fuzzy.FuzzyChoice([c for c in Country])
    currency_code = "EUR"
    cust_itemcode = fuzzy.FuzzyText()
    debtfreeprice = fuzzy.FuzzyDecimal(0, 99999999999)
    extralink = factory.List([factory.SubFactory(ExtraLinkFactory) for _ in range(2)])
    floors = fuzzy.FuzzyInteger(0, 9999999999)
    energyclass = fuzzy.FuzzyText(length=10)
    holdingtype = fuzzy.FuzzyChoice([c for c in HoldingType])
    image = factory.List([factory.SubFactory(ImageFactory) for _ in range(2)])
    itemgroup = fuzzy.FuzzyChoice([c for c in ItemGroup])
    livingaream2 = fuzzy.FuzzyDecimal(0, 99999999999)
    loclvlid = 1
    locsourceid = 4
    lotarea = fuzzy.FuzzyDecimal(0, 99999999999)
    lotareaunitcode = fuzzy.FuzzyText(length=2)
    lotholding = fuzzy.FuzzyText()
    postcode = fuzzy.FuzzyText(length=5)
    price = fuzzy.FuzzyDecimal(0, 99999999999)
    price_m2 = fuzzy.FuzzyDecimal(0, 99999999999)
    quarteroftown = fuzzy.FuzzyText(length=60)
    realtygroup = fuzzy.FuzzyChoice([c for c in RealtyGroup])
    realtyidentifier = fuzzy.FuzzyText(length=40)
    realty_itemgroup = fuzzy.FuzzyChoice([c for c in ItemGroup])
    realtytype = fuzzy.FuzzyChoice([c for c in RealtyType])
    realtyoption = factory.List([fuzzy.FuzzyText() for _ in range(2)])
    rc_parkingspace_count = fuzzy.FuzzyInteger(0, 9999999999)
    roomcount = fuzzy.FuzzyInteger(0, 9999999999)
    roomnumber = fuzzy.FuzzyText(
        length=3, chars=string.ascii_letters + string.digits
    )
    scontact = factory.List([factory.SubFactory(ScontactFactory) for _ in range(2)])
    showingdate = fuzzy.FuzzyDateTime(timezone.now())
    showing_date2 = fuzzy.FuzzyDateTime(timezone.now())
    street = fuzzy.FuzzyText(length=200)
    supplier_source_itemcode = fuzzy.FuzzyText()
    text = factory.List([factory.SubFactory(TextFactory) for _ in range(2)])
    town = fuzzy.FuzzyText(length=60)
    tradetype = fuzzy.FuzzyChoice([c for c in TradeType])
    zoningname = fuzzy.FuzzyText()
