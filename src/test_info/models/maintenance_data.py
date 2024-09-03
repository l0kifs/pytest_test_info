from dataclasses import dataclass

import pytest

from .label_data import LabelData


@dataclass
class MaintenanceData:
    reason: str
    issue_id: str
    skip_test: bool = True
    label = LabelData(
        name="maintenance",
        description="Test is under maintenance"
    )

    def get_skip_mark(self):
        return pytest.mark.skip(
            reason=f"Reason: {self.reason}. " +
                   f"Issue: {self.issue_id}"
        )
