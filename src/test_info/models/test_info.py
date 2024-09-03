from dataclasses import dataclass, field
from typing import Optional

from .maintenance_data import MaintenanceData
from ..data.labels import Label
from ..data.priorities import Priority
from ..data.services import Service


@dataclass
class TestInfo:
    summary: str
    description: str
    affected_services: list[Service]
    priority: Priority
    preconditions: list[str] = field(default_factory=list)
    postconditions: list[str] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)
    maintenance: Optional[MaintenanceData] = None
