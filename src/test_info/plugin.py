import pytest
from _pytest.nodes import Item

from .data.labels import Label
from .data.priorities import Priority
from .data.services import Service


class Plugin:
    def __init__(self):
        self.label: Label = None
        self.service: Service = None
        self.priority: Priority = None

    # def pytest_addoption(self, parser):
    #     parser.addoption(
    #         "--myoption",
    #         action="store",
    #         default="default_value",
    #         help="My custom option"
    #     )

    def pytest_configure(
        self,
        config: pytest.Config
    ):
        for label in Label:
            label.value.register_mark(config)
        for service in Service:
            service.value.register_mark(config)
        for priority in Priority:
            priority.value.register_mark(config)

    def pytest_collection_modifyitems(
        self,
        config: pytest.Config,
        items: list[Item]
    ):
        missing_test_info = []
        for item in items:
            if 'test_info' not in item.keywords:
                missing_test_info.append(item.name)
        if missing_test_info:
            print(f"Tests missing @test_info decorator: {', '.join(missing_test_info)}")
            # pytest.exit(f"Tests missing @test_info decorator: {', '.join(missing_test_info)}", returncode=1)


plugin = Plugin()
