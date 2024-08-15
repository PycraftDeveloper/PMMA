import gc

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

class PassportIntermediary:
    name = None
    sub_name = None
    short_description = None
    long_description = None
    project_url = None
    documentation_url = None
    project_directory = None
    project_temporary_directory = None
    project_resources_directory = None
    project_python_src_directory = None
    project_c_src_directory = None
    project_pyx_src_directory = None
    license = None
    author = None
    version = None
    supported_python_versions = None
    project_size = None
    passport_changed = False

class Passport:
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
            license=None,
            author=None,
            version=None,
            supported_python_versions=None,
            project_size=None):
        """
        name example: "MyAwesomeGame"
        sub-name example: "ExpandedEdition"
        """

        if Registry.pmma_initialized:
            log_development("Whilst it may not always be possible to do, configuring your \
application's passport is best done before calling 'pmma.init()'. Doing so, as you have done, \
afterwards may cause unintentional or unexpected behavior as some changes may not take effect. \
This will only be true where limited by the capabilities of the operating system, as PMMA will \
try and work around this.")

        PassportIntermediary.passport_changed = True

        PassportIntermediary.name = name
        PassportIntermediary.sub_name = sub_name
        PassportIntermediary.short_description = short_description
        PassportIntermediary.long_description = long_description
        PassportIntermediary.project_url = project_url
        PassportIntermediary.documentation_url = documentation_url
        PassportIntermediary.project_directory = project_directory
        PassportIntermediary.project_temporary_directory = project_temporary_directory
        PassportIntermediary.project_resources_directory = project_resources_directory
        PassportIntermediary.project_python_src_directory = project_python_src_directory
        PassportIntermediary.project_c_src_directory = project_c_src_directory
        PassportIntermediary.project_pyx_src_directory = project_pyx_src_directory
        PassportIntermediary.license = license
        PassportIntermediary.author = author
        PassportIntermediary.version = version
        PassportIntermediary.supported_python_versions = supported_python_versions
        PassportIntermediary.project_size = project_size

        Registry.pmma_object_instances[id(self)] = self
        self._shut_down = False

    def set_name(self, name):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.name = name

    def set_sub_name(self, sub_name):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.sub_name = sub_name

    def set_short_description(self, short_description):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.short_description = short_description

    def set_long_description(self, long_description):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.long_description = long_description

    def set_project_url(self, project_url):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_url = project_url

    def set_documentation_url(self, documentation_url):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.documentation_url = documentation_url

    def set_project_directory(self, project_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_directory = project_directory

    def set_project_temporary_directory(self, project_temporary_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_temporary_directory = project_temporary_directory

    def set_project_resources_directory(self, project_resources_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_resources_directory = project_resources_directory

    def set_project_python_src_directory(self, project_python_src_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_python_src_directory = project_python_src_directory

    def set_project_c_src_directory(self, project_c_src_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_c_src_directory = project_c_src_directory

    def set_project_pyx_src_directory(self, project_pyx_src_directory):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_pyx_src_directory = project_pyx_src_directory

    def set_license(self, license):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.license = license

    def set_author(self, author):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.author = author

    def set_version(self, version):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.version = version

    def set_supported_python_versions(self, supported_python_versions):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.supported_python_versions = supported_python_versions

    def set_project_size(self, project_size):
        PassportIntermediary.passport_changed = True
        PassportIntermediary.project_size = project_size

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True