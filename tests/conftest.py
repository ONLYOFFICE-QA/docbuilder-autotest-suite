import os
import pytest
import shutil
from lib.docbuilder_wrapper import DocBuilderWrapper
from lib.config import TMP_FOLDER


@pytest.fixture(scope='function')
def builder() -> DocBuilderWrapper:
    return DocBuilderWrapper()


def pytest_sessionstart(session):
    """Actions before start tests session
    """
    if not os.path.exists(TMP_FOLDER):
        os.makedirs(TMP_FOLDER)


def pytest_sessionfinish(session):
    """Actions after finish tests session
    """
    if os.path.exists(TMP_FOLDER):
        shutil.rmtree(TMP_FOLDER)
