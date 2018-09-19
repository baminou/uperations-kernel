
from .library import Library

class Kernel:

    __instance = None

    @staticmethod
    def get_instance():
        """
        Return the Kernel instance

        Return:
            Kernel: The created or not instance of the Kernel
        """
        if Kernel.__instance == None:
            Kernel()
        return Kernel.__instance

    def __init__(self):
        if Kernel.__instance != None:
            raise Exception("This class is a singleton")
        else:
            Kernel.__instance = self
        self._libraries = {}
        return

    def set_libraries(self, libraries):
        self._libraries = libraries

    def get_libraries(self):
        return self._libraries

    def find_operation(self, library, operation):
        for tmp_lib in self._libraries:
            if tmp_lib == library:
                for op in self._libraries()[tmp_lib].operations():
                    if self._libraries()[tmp_lib].operations()[op].name() == operation:
                        return self._libraries()[tmp_lib].operations()[op]
                raise Exception("The operation %s:%s does not exist. " % (library, operation))
            raise Exception("The libary %s does not exist." % (library))

    def find_library(self, library_name):
        """
        Find a library by name

        Args:
            library_name str: Name of the library

        Return:
            Library: The requested library
        """
        return self.get_libraries()[library_name]