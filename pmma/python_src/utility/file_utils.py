from gc import collect as _gc__collect

from watchdog.observers import Observer as _Observer
from watchdog.events import FileSystemEventHandler as _FileSystemEventHandler

from pmma.python_src.constants import Constants as _Constants

from pmma.python_src.utility.initialization_utils import initialize as _initialize

class FileUtilityIntermediary:
    file_matrix = {}

class EventHandler(_FileSystemEventHandler):
    def __init__(self, file_class):
        _initialize(self)

        self.file_class = file_class

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def on_created(self, event):
        if event.is_directory is False:
            file_path = event.src_path
            file = file_path.split(_Constants.PATH_SEPARATOR)[-1]
            if file not in FileUtilityIntermediary.file_matrix:
                FileUtilityIntermediary.file_matrix[file] = self.file_class(file_path)
            else: # duplicate name resolver
                original_file = FileUtilityIntermediary.file_matrix[file].get_path()
                del FileUtilityIntermediary.file_matrix[file]

                new_file = file_path

                original_file_split = original_file.split(_Constants.PATH_SEPARATOR)
                new_file_split = new_file.split(_Constants.PATH_SEPARATOR)

                original_identifier = original_file_split[-1]
                new_identifier = new_file_split[-1]

                del original_file_split[-1]
                del new_file_split[-1]

                while original_identifier == new_identifier:
                    original_identifier = original_file_split[-1] + _Constants.PATH_SEPARATOR + original_identifier
                    new_identifier = new_file_split[-1] + _Constants.PATH_SEPARATOR + new_identifier

                    del original_file_split[-1]
                    del new_file_split[-1]

                FileUtilityIntermediary.file_matrix[original_identifier] = self.file_class(original_file)
                FileUtilityIntermediary.file_matrix[new_identifier] = self.file_class(new_file)

    def on_deleted(self, event):
        file_path = event.src_path
        local_file_matrix = dict(FileUtilityIntermediary.file_matrix)
        for file in local_file_matrix:
            if FileUtilityIntermediary.file_matrix[file].get_path() == file_path:
                del FileUtilityIntermediary.file_matrix[file]

class DirectoryWatcher:
    def __init__(self, locations, file_class):
        _initialize(self)

        self.observer = _Observer()
        self.watching = {}
        for location in locations:
            event_handler = EventHandler(file_class)
            watcher = self.observer.schedule(event_handler, location, recursive=True)
            self.watching[location] = watcher

    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def sync_file_matrix(self, file_matrix):
        new_file_matrix = file_matrix | FileUtilityIntermediary.file_matrix
        FileUtilityIntermediary.file_matrix = new_file_matrix
        return new_file_matrix

    def update_all_locations(self, locations):
        self.observer.stop()
        self.__init__(locations)
        self.observer.start()

    def remove_location(self, location):
        self.observer.unschedule(self.watching[location])
        del self.watching[location]

    def add_location(self, location):
        event_handler = EventHandler()
        watcher = self.observer.schedule(event_handler, location, recursive=True)
        self.watching[location] = watcher

    def start(self):
        self.observer.start()

    def stop(self):
        self.observer.stop()