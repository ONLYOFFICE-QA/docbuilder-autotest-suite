import pytest
from lib.document_builder import DocumentBuilder


@pytest.fixture(scope='function')
def builder() -> DocumentBuilder:
    return DocumentBuilder()
