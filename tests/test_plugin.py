from src.test_info.config.external_imports import ExternalImports


def test_example():
    label = ExternalImports.import_module("label", "labels.py").Label
    for label in label:
        print(label)
