from tests.factories import (
    CoordinateFactory,
    ExtraLinkFactory,
    ImageFactory,
    ItemFactory,
    TextFactory,
)
from tests.utils import check_dataclass_typing


def test_coordinate_factory_typing():
    instance = CoordinateFactory()
    check_dataclass_typing(instance)


def test_extra_link_factory_typing():
    instance = ExtraLinkFactory()
    check_dataclass_typing(instance)


def test_image_factory_typing():
    instance = ImageFactory()
    check_dataclass_typing(instance)


def test_item_factory_typing():
    instance = ItemFactory()
    check_dataclass_typing(instance)


def test_text_factory_typing():
    instance = TextFactory()
    check_dataclass_typing(instance)
