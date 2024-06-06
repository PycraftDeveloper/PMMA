from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

class PassportIntermediary:
    name = None
    short_description = None
    long_description = None
    project_url = None
    documentation_url = None
    project_directory = None
    project_temporary_directory = None
    project_resources_directory = None
    project_py_src_directory = None
    project_c_src_directory = None
    project_pyx_src_directory = None
    license = None
    author = None
    version = None
    supported_python_versions = None

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
            project_py_src_directory=None,
            project_c_src_directory=None,
            project_pyx_src_directory=None,
            license=None,
            author=None,
            version=None,
            supported_python_versions=None):

        PassportIntermediary.name = name
        PassportIntermediary.short_description = short_description
        PassportIntermediary.long_description = long_description
        PassportIntermediary.project_url = project_url
        PassportIntermediary.documentation_url = documentation_url
        PassportIntermediary.project_directory = project_directory
        PassportIntermediary.project_temporary_directory = project_temporary_directory
        PassportIntermediary.project_resources_directory = project_resources_directory
        PassportIntermediary.project_py_src_directory = project_py_src_directory
        PassportIntermediary.project_c_src_directory = project_c_src_directory
        PassportIntermediary.project_pyx_src_directory = project_pyx_src_directory
        PassportIntermediary.license = license
        PassportIntermediary.author = author
        PassportIntermediary.version = version
        PassportIntermediary.supported_python_versions = supported_python_versions