
from .documentable import Documentable
import inspect
import os
from abc import abstractmethod


class Library(Documentable):

    def __init__(self, slug=None):
        self._slug = slug
        return

    @abstractmethod
    def operations(self):
        """
        Return a directory containing the list of operations
        :return:
        """
        raise NotImplementedError

    def set_slug(self, slug):
        """
        Assign a slug to the library

        Param:
            slug str: The slug to be assigned
        """
        self._slug = slug
        return

    def get_slug(self):
        """
        Return the library's slug

        Return:
            str: Library's slug
        """
        return self._slug

    def library_dir(self):
        """
        Return the directory path of the library

        Return:
            str: The path of the library directory in the project
        """
        return os.path.join(os.path.dirname(inspect.getfile(self.__class__)),self.name())

    def operations_dir(self):
        return os.path.join(self.library_dir(),'operations')