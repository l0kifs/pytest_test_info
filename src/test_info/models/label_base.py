from abc import ABC
from enum import Enum

from .label_data import LabelData


class LabelBase(Enum, ABC):
    def __new__(cls, value):
        if not isinstance(value, LabelData):
            raise TypeError(f"Value must be a LabelData, got {type(value).__name__}")
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
