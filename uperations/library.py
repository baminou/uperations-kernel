
from .documentable import Documentable
import inspect
import os


class Library(Documentable):

    def __init__(self, slug=None, dir_path=None):
        self._slug = slug
        return

    def set_slug(self, slug):
        self._slug = slug
        return


    @staticmethod
    def operations():
        return {}

    def library_dir(self):
        return os.path.dirname(inspect.getfile(self.__class__))

class LibraryException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(LibraryException, self).__init__(message)

class LibraryNotFound(LibraryException):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(LibraryNotFound, self).__init__(message)