from uperations.library import Library
from uperations.exceptions.library import LibraryException, LibraryNotFound
import os
import pytest

def test_get_slug():
    library = Library("my_slug")
    assert library.get_slug() == "my_slug"
    return

def test_set_slug():
    library = Library()
    library.set_slug('my_slug')
    assert library.get_slug() == "my_slug"
    return

def test_library_dir():
    library = Library("my_slug")
    assert library.library_dir() == os.path.join(os.getcwd(),"uperations")

def test_library_exception():
    with pytest.raises(LibraryException) as excinfo:
        raise LibraryException("This is a library exception")
    assert "Uperation library" in str(excinfo.value)

def test_library_not_found_exception():
    with pytest.raises(LibraryNotFound) as excinfo:
        raise LibraryNotFound("This is a library exception")
    assert "Uperation library not found" in str(excinfo.value)