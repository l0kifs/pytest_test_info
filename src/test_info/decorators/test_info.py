from ..models.test_info import TestInfo


def test_info(info: TestInfo):
    def composition(func):
        if info.maintenance:
            func = info.maintenance.label.get_mark()(func)
            if info.maintenance.skip_test:
                func = info.maintenance.get_skip_mark()(func)
        for label in info.labels:
            func = label.value.get_mark()(func)
        for service in info.affected_services:
            func = service.value.get_mark()(func)
        func = info.priority.value.get_mark()(func)
        return func
    return composition
