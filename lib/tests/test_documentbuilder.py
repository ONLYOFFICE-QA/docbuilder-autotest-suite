import logging
import os.path

import pytest
from lib.docbuilder import DocumentBuilder
from lib.script_helper import ScriptHelper

file_path = os.path.abspath('scripts/smoke/templates/docx/api/create_paragraph.js')
builder = DocumentBuilder()


def test_run_script():
    logging.info("Testing the run_script method")
    # Assume 'script_path' is the path to a valid script for the test
    script_path, output_path = ScriptHelper().prepare_script(file_path)
    result = builder.run_script(script_path)
    assert result['code'] == 0, 'Script was not executed correctly'
    assert os.path.isfile(output_path) == True, 'Result file was not created'


def test_run_unprepared_script():
    logging.info("Testing the run_script method with an unprepared script")
    result = builder.run_script(file_path)
    assert result['code'] != 0, 'Script did not cause an error'
    assert result['stderr'] != '', 'Stderr is empty'
