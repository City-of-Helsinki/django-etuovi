import typing


def _find_type_origin(type_hint):
    actual_type = typing.get_origin(type_hint) or type_hint
    if isinstance(actual_type, typing._SpecialForm):
        # case of typing.Union[…]
        for origins in map(_find_type_origin, typing.get_args(type_hint)):
            yield from origins
    else:
        yield actual_type


def check_dataclass_typing(instance):
    for field_name, field_def in instance.__dataclass_fields__.items():
        actual_types = tuple(
            type_origin for type_origin in _find_type_origin(field_def.type)
        )
        actual_value = getattr(instance, field_name)
        assert isinstance(actual_value, actual_types), (
            f"Value {actual_value} of field {field_name}"
            f"is not an instance of {actual_types}"
        )
