from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

class PassportIntermediary:
    name = None
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

class Passport:
    def __init__(
            self,
            name=None,
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

        self.attributes = []

        PassportIntermediary.name = name
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

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                gc.collect()

    def quit(self):
        self.__del__()
        self._shut_down = True