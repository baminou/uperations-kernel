from uperations.library import Library
import os

def test_slug():
    library = Library("my_slug")
    assert library.get_slug() == "my_slug"
    return

def test_library_dir():
    library = Library("my_slug")
    assert library.library_dir() == os.path.join(os.getcwd(),"uperations")
