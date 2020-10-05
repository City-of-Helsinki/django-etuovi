import typing


def check_dataclass_typing(instance):
    for field_name, field_def in instance.__dataclass_fields__.items():
        actual_type = typing.get_origin(field_def.type) or field_def.type
        actual_value = getattr(instance, field_name)
        assert isinstance(actual_value, actual_type)
