from enum import Enum

from ..models.label_data import LabelData


class Service(Enum):
    bcgateway = LabelData(
        name="bcgateway",
        description="Test affects bcgateway service"
    )
    callbacks = LabelData(
        name="callbacks",
        description="Test affects callbacks service"
    )
