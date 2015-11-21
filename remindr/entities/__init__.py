from schematics.models import Model
from schematics.types.base import (
    DateTimeType,
    GeoPointType,
    StringType,
    TextType,
    UUIDType,
)
from schematics.types.compound import (
    ListType,
    ModelType,
)


class Item(Model):
    uuid = UUIDType(required=True)
    name = StringType(required=True)
    description = TextType(required=False)
    location = GeoPointType(required=True)
    created_at = DateTimeType(required=True)


class User(Model):
    uuid = UUIDType(required=True)
    items = ListType(ModelType(Item), default=list)
