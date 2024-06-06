from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, PatternMatchingEventHandler

from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

class EventHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        print(event)

    def on_deleted(self, event):
        print(event)

class DirectoryWatcher:
    def __init__(self, locations):
        self.observer = Observer()
        self.watching = {}
        for location in locations:
            event_handler = EventHandler()
            watcher = self.observer.schedule(event_handler, location, recursive=True)
            self.watching[location] = watcher

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