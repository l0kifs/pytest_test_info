from enum import Enum

from ..models.label_data import LabelData


class Priority(Enum):
    high = LabelData(
        name="priority_high",
        description="Test with priority High"
    )
    medium = LabelData(
        name="priority_medium",
        description="Test with priority Medium"
    )
    low = LabelData(
        name="priority_low",
        description="Test with priority Low"
    )
