from pmma.py_src.registry import Registry
from pmma.py_src.constants import Constants

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
    def __init__(self):
        self.file_matrix = {}

    def scan(self):
        pass

    def add(self, file_path):
        pass