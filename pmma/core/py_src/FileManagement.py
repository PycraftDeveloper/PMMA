import os, shutil, pathlib

import send2trash

from pmma.core.py_src.Utility import Registry
import pmma.core.py_src.Error as Error

from pmma.build.Logger import Logger

class File:
    def __init__(self, file_path):
        self.logger = Logger()
        if Registry.passport_instance is None:
            self.logger.internal_log_error(
                23,
                "You have not created a passport for this application yet. \
This is used by PMMA and by your operating system to identify your application. \
Please use `pmma.Passport` to start creating a passport for your application.",
                True)

            raise Error.PassportNotInitializedError("Passport not initialized")

        self.file_path = str(pathlib.Path(file_path))

    def get_absolute_file_path(self):
        if not Registry.passport_instance.is_registered():
            self.logger.internal_log_error(
                35,
                "You have not registered this application yet. \
This is used by PMMA and by your operating system to identify your application. \
Please use `pmma.Passport.register` to register your application.",
                True)

            raise Error.PassportNotRegisteredError("Passport has not been registered")

        root = Registry.passport_instance.get_product_path()
        return root + os.sep + self.file_path

    def get_relative_file_path(self):
        return "." + os.sep + self.file_path

    def is_file_exists(self):
        return os.path.exists(self.get_absolute_file_path())

    def move(self, destination):
        src_path = self.get_absolute_file_path()
        root = Registry.passport_instance.get_product_path()
        destination = str(pathlib.Path(destination))
        destination = root + os.sep + destination + os.sep + os.path.basename(src_path)

        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                36,
                f"This file does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise FileNotFoundError

        if os.path.exists(destination):
            self.logger.internal_log_error(
                37,
                f"A file already exists at the specified location: \
'{destination}' with this name. Please ensure that you specify a file \
location that does not already exist.",
                True)

            raise FileExistsError

        shutil.move(src_path, destination)

        self.file_path = destination.replace(root + os.sep, "")

    def copy(self, destination):
        src_path = self.get_absolute_file_path()
        root = Registry.passport_instance.get_product_path()
        destination = str(pathlib.Path(destination))
        destination = root + os.sep + destination + os.sep + os.path.basename(src_path)
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                36,
                f"This file does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise FileNotFoundError

        if os.path.exists(destination):
            self.logger.internal_log_error(
                37,
                f"A file already exists at the specified location: \
'{destination}'. Please ensure that you specify a file location that does \
not already exist.",
                True)

            raise FileExistsError

        shutil.copy(src_path, destination)

    def delete(self):
        src_path = self.get_absolute_file_path()
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                36,
                f"This file does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise FileNotFoundError

        os.remove(src_path)

    def recycle(self):
        send2trash.send2trash(self.get_absolute_file_path())

    def rename(self, new_name):
        src_path = self.get_absolute_file_path()
        root = Registry.passport_instance.get_product_path()
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                36,
                f"This file does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise FileNotFoundError

        if os.path.exists(new_name):
            self.logger.internal_log_error(
                37,
                f"A file already exists at the specified location: \
'{new_name}' with this name. Please ensure that you specify a file \
location that does not already exist.",
                True)

            raise FileExistsError

        directory = os.path.dirname(src_path)
        extension = os.path.splitext(src_path)[1]

        new_path = os.path.join(directory, new_name + extension)

        os.rename(src_path, new_path)

        self.file_path = new_path.replace(root + os.sep, "")

class Directory:
    def __init__(self, directory_name):
        self.logger = Logger()
        if Registry.passport_instance is None:
            self.logger.internal_log_error(
                23,
                "You have not created a passport for this application yet. \
This is used by PMMA and by your operating system to identify your application. \
Please use `pmma.Passport` to start creating a passport for your application.",
                True)

            raise Error.PassportNotInitializedError("Passport not initialized")

        self.directory_name = str(pathlib.Path(directory_name))

    def get_absolute_path(self):
        if not Registry.passport_instance.is_registered():
            self.logger.internal_log_error(
                35,
                "You have not registered this application yet. \
This is used by PMMA and by your operating system to identify your application. \
Please use `pmma.Passport.register` to register your application.",
                True)

            raise Error.PassportNotRegisteredError("Passport has not been registered")

        root = Registry.passport_instance.get_product_path()

        return root + os.sep + self.directory_name

    def get_relative_path(self):
        return "." + os.sep + self.directory_name

    def is_directory_exists(self):
        return os.path.exists(self.get_absolute_path())

    def move(self, destination):
        src_path = self.get_absolute_path()
        root = Registry.passport_instance.get_product_path()
        destination = str(pathlib.Path(destination))
        destination = root + os.sep + destination
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                38,
                f"The directory does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise Error.DirectoryNotFoundError

        if os.path.exists(destination):
            self.logger.internal_log_error(
                39,
                f"A directory already exists at the specified location: \
'{destination}' with this name. Please ensure that you specify a directory \
location that does not already exist.",
                True)

            raise Error.DirectoryAlreadyExistsError

        shutil.move(src_path, destination)

        self.directory_name = destination.replace(root + os.sep, "")

    def copy(self, destination):
        src_path = self.get_absolute_path()
        root = Registry.passport_instance.get_product_path()
        destination = str(pathlib.Path(destination))
        destination = root + os.sep + destination
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                38,
                f"The directory does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise Error.DirectoryNotFoundError

        if os.path.exists(destination):
            self.logger.internal_log_error(
                39,
                f"A directory already exists at the specified location: \
'{destination}' with this name. Please ensure that you specify a directory \
location that does not already exist.",
                True)

            raise Error.DirectoryAlreadyExistsError

        shutil.copytree(src_path, destination)

    def delete(self):
        src_path = self.get_absolute_path()
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                38,
                f"The directory does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise Error.DirectoryNotFoundError

        shutil.rmtree(src_path)

    def recycle(self):
        send2trash.send2trash(self.get_absolute_path())

    def rename(self, new_name):
        src_path = self.get_absolute_path()
        root = Registry.passport_instance.get_product_path()
        directory = os.path.dirname(src_path)
        destination = os.path.join(directory, new_name)
        if not os.path.exists(src_path):
            self.logger.internal_log_error(
                38,
                f"The directory does not exist at the specified location: \
'{src_path}'. Please ensure that you have specified the correct path from your \
registered product location.",
                True)

            raise Error.DirectoryNotFoundError

        if os.path.exists(new_name):
            self.logger.internal_log_error(
                39,
                f"A directory already exists at the specified location: \
'{destination}' with this name. Please ensure that you specify a directory location that does \
not already exist.",
                True)

            raise Error.DirectoryAlreadyExistsError

        os.rename(src_path, destination)
        self.directory_name = destination.replace(root + os.sep, "")