import importlib.util
import logging
import os


class ExternalImports:
    _log = logging.getLogger(__name__)

    @classmethod
    def _get_abs_file_path(
        cls,
        file_path: str
    ) -> str | None:
        """
        Get the absolute file path.
        :param file_path: Relative or abs file path.
        :return:
        """
        cls._log.debug(f"Get absolute file path for provided path: {file_path}")
        abs_file_path = None
        # provided absolute path
        if os.path.isabs(file_path):
            if os.path.exists(file_path):
                abs_file_path = file_path
        # provided relative path starting from the current working directory
        else:
            abs_path = os.path.join(os.getcwd(), file_path)
            if os.path.exists(abs_path):
                abs_file_path = abs_path
        return abs_file_path

    @classmethod
    def _find_file(
        cls,
        file_name: str
    ) -> str | None:
        """
        Find the file in the current working directory and all subdirectories.
        :param file_name: File name to search for.
        :return:
        """
        cls._log.debug(f"Searching for file: {file_name}")
        file_path = None
        for root, dirs, files in os.walk(os.getcwd()):
            if file_name in files:
                file_path = os.path.join(root, file_name)
        return file_path

    @classmethod
    def _import_module(
        cls,
        name: str,
        path: str
    ):
        """
        Import a module from a file.
        :param name: Module name. Can be anything.
        :param path: Module file path.
        :return:
        """
        cls._log.debug(f"Importing module: {name} from {path}")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    @classmethod
    def import_module(
        cls,
        name: str,
        file_name: str,
    ):
        """
        Import a module from a file.
        :param name: Module name. Can be anything.
        :param file_name: Module file name.
        :return:
        """
        module_path = cls._find_file(file_name)
        if not module_path:
            cls._log.error(f"Could not find file: {file_name}")
            return None
        return cls._import_module(name, module_path)
