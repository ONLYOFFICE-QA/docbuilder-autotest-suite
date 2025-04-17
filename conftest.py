import os
import shutil
from lib.config import TMP_FOLDER


def pytest_sessionstart():
    """Actions before start tests session
    """
    if not os.path.exists(TMP_FOLDER):
        os.makedirs(TMP_FOLDER)


def pytest_sessionfinish():
    """Actions after finish tests session
    """
    if os.path.exists(TMP_FOLDER):
        shutil.rmtree(TMP_FOLDER)
