from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class Passport:
    """
    🟩 **R** -
    """
    def __init__(
            self,
            name=None,
            sub_name=None,
            short_description=None,
            long_description=None,
            project_url=None,
            documentation_url=None,
            project_directory=None,
            project_temporary_directory=None,
            project_resources_directory=None,
            project_python_src_directory=None,
            project_c_src_directory=None,
            project_pyx_src_directory=None,
            project_log_directory=None,
            license=None,
            author=None,
            version=None,
            supported_python_versions=None,
            project_size=None):
        """
        🟩 **R** -
        name example: "MyAwesomeGame"
        sub-name example: "ExpandedEdition"
        """

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._file__module = _ModuleManager.import_module("pmma.python_src.file")

        self._shut_down = False

        if _Registry.pmma_initialized:
            self._logger = self._logging_utils__module.InternalLogger()

            self._logger.log_development("Whilst it may not always be possible to do, configuring your \
application's passport is best done before calling 'pmma.init()'. Doing so, as you have done, \
afterwards may cause unintentional or unexpected behavior as some changes may not take effect.")

        _PassportIntermediary.passport_changed = True

        if name is not None:
            _PassportIntermediary.passport_file_location = self._file__module.path_builder(_Registry.base_path, "passports", f"passport_for_{name.lower()}.json")

        _PassportIntermediary.name = name
        _PassportIntermediary.sub_name = sub_name
        _PassportIntermediary.short_description = short_description
        _PassportIntermediary.long_description = long_description
        _PassportIntermediary.project_url = project_url
        _PassportIntermediary.documentation_url = documentation_url
        _PassportIntermediary.project_directory = project_directory
        _PassportIntermediary.project_temporary_directory = project_temporary_directory
        _PassportIntermediary.project_resources_directory = project_resources_directory
        _PassportIntermediary.project_python_src_directory = project_python_src_directory
        _PassportIntermediary.project_c_src_directory = project_c_src_directory
        _PassportIntermediary.project_pyx_src_directory = project_pyx_src_directory
        _PassportIntermediary.project_log_directory = project_log_directory
        _PassportIntermediary.license = license
        _PassportIntermediary.author = author
        _PassportIntermediary.version = version
        _PassportIntermediary.supported_python_versions = supported_python_versions
        _PassportIntermediary.project_size = project_size

        self._shut_down = False

    def get_project_log_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_log_directory

    def get_name(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.name

    def get_sub_name(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.sub_name

    def get_short_description(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.short_description

    def get_long_description(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.long_description

    def get_project_url(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_url

    def get_documentation_url(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.documentation_url

    def get_project_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_directory

    def get_project_temporary_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_temporary_directory

    def get_project_resources_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_resources_directory

    def get_project_python_src_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_python_src_directory

    def get_project_c_src_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_c_src_directory

    def get_project_pyx_src_directory(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_pyx_src_directory

    def get_license(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.license

    def get_author(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.author

    def get_version(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.version

    def get_supported_python_versions(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.supported_python_versions

    def get_project_size(self):
        """
        🟩 **R** -
        """
        return _PassportIntermediary.project_size

    def set_project_log_directory(self, project_log_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed
        _PassportIntermediary.project_log_directory = project_log_directory

    def set_name(self, name):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed
        _PassportIntermediary.name = name

    def set_sub_name(self, sub_name):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed
        _PassportIntermediary.sub_name = sub_name

    def set_short_description(self, short_description):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed
        _PassportIntermediary.short_description = short_description

    def set_long_description(self, long_description):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.long_description = long_description

    def set_project_url(self, project_url):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_url = project_url

    def set_documentation_url(self, documentation_url):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.documentation_url = documentation_url

    def set_project_directory(self, project_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_directory = project_directory

    def set_project_temporary_directory(self, project_temporary_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_temporary_directory = project_temporary_directory

    def set_project_resources_directory(self, project_resources_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_resources_directory = project_resources_directory

    def set_project_python_src_directory(self, project_python_src_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_python_src_directory = project_python_src_directory

    def set_project_c_src_directory(self, project_c_src_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_c_src_directory = project_c_src_directory

    def set_project_pyx_src_directory(self, project_pyx_src_directory):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_pyx_src_directory = project_pyx_src_directory

    def set_license(self, license):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.license = license

    def set_author(self, author):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.author = author

    def set_version(self, version):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.version = version

    def set_supported_python_versions(self, supported_python_versions):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.supported_python_versions = supported_python_versions

    def set_project_size(self, project_size):
        """
        🟩 **R** -
        """
        _PassportIntermediary.passport_changed = True
        _PassportIntermediary.project_size = project_size

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True