import os as _os
import shutil as _shutil

import send2trash as _send2trash

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary
from pmma.python_src.utility.file_utils import DirectoryWatcher as _DirectoryWatcher
from pmma.python_src.utility.initialization_utils import initialize as _initialize

def path_builder(*args):
    """
    🟩 **R** -
    """
    result = ""
    for arg in args:
        if result != "" and _os.path.exists(result) is False:
            _os.mkdir(result)

        result += arg
        result += _Constants.PATH_SEPARATOR
    result = result[:-1]
    return result

class File:
    """
    🟩 **R** -
    """
    def __init__(self, file_path):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._file_path = file_path

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def exists(self):
        """
        🟩 **R** -
        """
        return _os.path.exists(self._file_path)

    def get_path(self):
        """
        🟩 **R** -
        """
        return self._file_path

    def get_directory(self):
        """
        🟩 **R** -
        """
        return _os.path.dirname(self._file_path)

    def get_file_name_and_type(self):
        """
        🟩 **R** -
        """
        return self._file_path.split(_Constants.PATH_SEPARATOR)[-1]

    def get_file_name(self):
        """
        🟩 **R** -
        """
        return self.get_file_name_and_type().split(".")[0]

    def get_file_type(self):
        """
        🟩 **R** -
        """
        return self.get_file_name_and_type().split(".")[-1]

    def move(self, new_path):
        """
        🟩 **R** -
        """
        _shutil.move(self._file_path, new_path)
        self._file_path = new_path

    def delete(self):
        """
        🟩 **R** -
        """
        _os.remove(self._file_path)

    def recycle(self):
        """
        🟩 **R** -
        """
        _send2trash.send2trash(self._file_path)

    def rename(self, new_name):
        """
        🟩 **R** -
        """
        file_type = self.get_file_type()
        new_file_path = _os.path.dirname(self._file_path) + _Constants.PATH_SEPARATOR + new_name + "." + file_type
        _os.rename(self._file_path, new_file_path)
        self._file_path = new_file_path

    def read(self):
        """
        🟩 **R** -
        """
        with open(self._file_path, "r") as file:
            return file.read()

    def write(self, content):
        """
        🟩 **R** -
        """
        with open(self._file_path, "w") as file:
            file.write(content)

class FileCore:
    """
    🟩 **R** -
    """
    def __init__(self, project_directory=None, passive_refresh=True):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_Constants.FILECORE_OBJECT, add_to_pmma_module_spine=True)

        self._locations = []
        self._file_matrix = {}

        self.update_locations(project_directory=project_directory, force_refresh=False)

        self._watcher = _DirectoryWatcher(self._locations, File)

        if passive_refresh:
            self._watcher.start()

        self.scan()

    def __del__(self):
        """
        🟩 **R** -
        """
        if self._shut_down is False:
            self._watcher.stop()

    def quit(self):
        """
        🟩 **R** -
        """
        self.__del__()
        self._shut_down = True

    def update_locations(self, project_directory=None, force_refresh=True):
        """
        🟩 **R** -
        """
        self._locations = [_Registry.base_path]
        if project_directory is not None:
            self._locations.append(project_directory)
        if _PassportIntermediary.project_directory is not None:
            self._locations.append(_PassportIntermediary.project_directory)
        if _PassportIntermediary.project_temporary_directory is not None:
            self._locations.append(_PassportIntermediary.project_temporary_directory)
        if _PassportIntermediary.project_resources_directory is not None:
            self._locations.append(_PassportIntermediary.project_resources_directory)
        if _PassportIntermediary.project_python_src_directory is not None:
            self._locations.append(_PassportIntermediary.project_python_src_directory)
        if _PassportIntermediary.project_pyx_src_directory is not None:
            self._locations.append(_PassportIntermediary.project_pyx_src_directory)
        if _PassportIntermediary.project_c_src_directory is not None:
            self._locations.append(_PassportIntermediary.project_c_src_directory)

        self.refresh(force=force_refresh)

    def scan(self):
        """
        🟩 **R** -
        """
        self._file_matrix = {}
        construction_matrix = {}
        for location in self._locations:
            for root, subdirs, files in _os.walk(location):
                for file in files:
                    file_path = _os.path.join(root, file)
                    if file not in construction_matrix:
                        construction_matrix[file] = File(file_path)
                    else: # duplicate name resolver
                        original_file = construction_matrix[file].get_path()
                        del construction_matrix[file]

                        new_file = file_path

                        original_file_split = original_file.split(_os.sep)
                        new_file_split = new_file.split(_os.sep)

                        original_identifier = original_file_split[-1]
                        new_identifier = new_file_split[-1]

                        del original_file_split[-1]
                        del new_file_split[-1]

                        while original_identifier == new_identifier:
                            original_identifier = original_file_split[-1] + _os.sep + original_identifier
                            new_identifier = new_file_split[-1] + _os.sep + new_identifier

                            del original_file_split[-1]
                            del new_file_split[-1]

                        construction_matrix[original_identifier] = File(original_file)
                        construction_matrix[new_identifier] = File(new_file)

        self._file_matrix = self._watcher.sync_file_matrix(construction_matrix)

    def refresh(self, force=False):
        """
        🟩 **R** -
        """
        list_of_original_locations = self._locations
        if list_of_original_locations != self._locations or force:
            self.scan()
            self._watcher.update_all_locations(self._locations)

    def stop_passively_refreshing(self):
        """
        🟩 **R** -
        """
        self._watcher.stop()

    def start_passively_refreshing(self):
        """
        🟩 **R** -
        """
        self._watcher.start()

    def identify(self, identifier):
        """
        🟩 **R** -
        """
        if identifier in self._file_matrix:
            return self._file_matrix[identifier]