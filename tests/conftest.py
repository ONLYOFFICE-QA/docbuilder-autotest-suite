import pytest
from lib.docbuilder_wrapper import DocBuilderWrapper


@pytest.fixture(scope='function')
def builder() -> DocBuilderWrapper:
    return DocBuilderWrapper()
