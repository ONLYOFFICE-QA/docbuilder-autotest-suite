import logging
import os.path

from lib.docbuilder import DocumentBuilder
from lib.script_helper import ScriptHelper
from config import OFFICE_JS_PATH

file_path = os.path.join(OFFICE_JS_PATH, os.path.normpath('Word/Api/Methods/GetDocument.js'))
builder = DocumentBuilder()


def test_run_script():
    logging.info("Testing the run_script method")
    # Assume 'script_path' is the path to a valid script for the test
    script_path, output_path = ScriptHelper().prepare_create_script(file_path)
    result = builder.run_script(script_path)
    assert result['returncode'] == 0, 'Script was not executed correctly'
    assert os.path.isfile(output_path) == True, 'Result file was not created'


def test_run_unprepared_script():
    logging.info("Testing the run_script method with an unprepared script")
    result = builder.run_script(file_path)
    assert result['returncode'] != 0, 'Script did not cause an error'
    assert result['stderr'] != '', 'Stderr is empty'
