import os

from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants

from pmma.python_src.passport import PassportIntermediary

import pmma.python_src.utility.file_utils as file_utils

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
        self.file_matrix = {}

        self.update_locations(project_directory=project_directory, force_refresh=False)

        self.watcher = file_utils.DirectoryWatcher(self.locations, File)

        if passive_refresh:
            self.watcher.start()

        self.scan()

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
        if PassportIntermediary.project_python_src_directory is not None:
            self.locations.append(PassportIntermediary.project_python_src_directory)
        if PassportIntermediary.project_pyx_src_directory is not None:
            self.locations.append(PassportIntermediary.project_pyx_src_directory)
        if PassportIntermediary.project_c_src_directory is not None:
            self.locations.append(PassportIntermediary.project_c_src_directory)

        self.refresh(force=force_refresh)

    def scan(self):
        self.file_matrix = {}
        construction_matrix = {}
        for location in self.locations:
            for root, subdirs, files in os.walk(location):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file not in construction_matrix:
                        construction_matrix[file] = File(file_path)
                    else: # duplicate name resolver
                        original_file = construction_matrix[file].get_path()
                        del construction_matrix[file]

                        new_file = file_path

                        original_file_split = original_file.split(os.sep)
                        new_file_split = new_file.split(os.sep)

                        original_identifier = original_file_split[-1]
                        new_identifier = new_file_split[-1]

                        del original_file_split[-1]
                        del new_file_split[-1]

                        while original_identifier == new_identifier:
                            original_identifier = original_file_split[-1] + os.sep + original_identifier
                            new_identifier = new_file_split[-1] + os.sep + new_identifier

                            del original_file_split[-1]
                            del new_file_split[-1]

                        construction_matrix[original_identifier] = File(original_file)
                        construction_matrix[new_identifier] = File(new_file)

        self.file_matrix = self.watcher.sync_file_matrix(construction_matrix)

    def refresh(self, force=False):
        list_of_original_locations = self.locations
        if list_of_original_locations != self.locations or force:
            self.scan()
            self.watcher.update_all_locations(self.locations)

    def stop_passively_refreshing(self):
        self.watcher.stop()

    def start_passively_refreshing(self):
        self.watcher.start()

    def identify(self, identifier):
        if identifier in self.file_matrix:
            return self.file_matrix[identifier]