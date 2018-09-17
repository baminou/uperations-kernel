
from uperations.documentable import Documentable

class TestDocumentable(Documentable):
    def name(cls):
        return "this_is_my_class_name"
    def description(cls):
        return "this_is_my_class_description"

class MissingNameDocumentable(Documentable):
    def description(cls):
        return "this_is_my_class_description"

class MissingDescriptionDocumentable(Documentable):
    def name(cls):
        return "this_is_my_class_name"

def test_name():
    doc_object = TestDocumentable()
    assert doc_object.name() == "this_is_my_class_name"
    return

def test_description():
    doc_object = TestDocumentable()
    assert doc_object.description() == "this_is_my_class_description"
    return

def test_missing_name():
    doc_object = MissingNameDocumentable()
    assert doc_object.name() == doc_object.__class__
    return

def test_missing_description():
    doc_object = MissingDescriptionDocumentable()
    assert doc_object.description() == str(doc_object.__class__)
    return
