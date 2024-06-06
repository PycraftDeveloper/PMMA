from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

from pmma.py_src.passport import PassportIntermediary

import pmma.py_src.utility.file_utils as file_utils

class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_path(self):
        return self.file_path

    def move(self, new_path):
        pass

    def delete(self):
        pass

    def rename(self, new_name):
        pass

    def read(self):
        pass

    def write(self, content):
        pass

class FileCore:
    def __init__(self, project_directory=None, passive_refresh=True):
        self.locations = []
        self.update_locations(project_directory=project_directory, force_refresh=False)

        self.watcher = file_utils.DirectoryWatcher(self.locations)

        if passive_refresh:
            self.watcher.start()

        self.file_matrix = {}

    def update_locations(self, project_directory=None, force_refresh=True):
        self.locations = [Registry.base_path]
        if project_directory is not None:
            self.locations.append(project_directory)
        if PassportIntermediary.project_directory is not None:
            self.locations.append(PassportIntermediary.project_directory)
        if PassportIntermediary.project_temporary_directory is not None:
            self.locations.append(PassportIntermediary.project_temporary_directory)
        if PassportIntermediary.project_resources_directory is not None:
            self.locations.append(PassportIntermediary.project_resources_directory)
        if PassportIntermediary.project_py_src_directory is not None:
            self.locations.append(PassportIntermediary.project_py_src_directory)
        if PassportIntermediary.project_pyx_src_directory is not None:
            self.locations.append(PassportIntermediary.project_pyx_src_directory)
        if PassportIntermediary.project_c_src_directory is not None:
            self.locations.append(PassportIntermediary.project_c_src_directory)

        print(self.locations)

        self.refresh(force=force_refresh)

    def scan(self):
        pass

    def refresh(self, force=False):
        list_of_original_locations = self.locations
        if list_of_original_locations != self.locations or force:
            self.scan()
            self.watcher.update_all_locations(self.locations)

    def stop_passively_refreshing(self):
        self.watcher.stop()

    def start_passively_refreshing(self):
        self.watcher.start()