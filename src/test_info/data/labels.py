from enum import Enum

from ..models.label_data import LabelData


class Label(Enum):
    maintenance = LabelData(
        name="maintenance",
        description="Test is under maintenance"
    )
    smoke = LabelData(
        name="smoke",
        description="Test from Smoke suite"
    )
