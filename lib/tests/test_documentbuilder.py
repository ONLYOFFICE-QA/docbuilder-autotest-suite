import logging
import os.path

import pytest
from lib.docbuilder import DocumentBuilder
from lib.script_helper import ScriptHelper

file_path = 'scripts/docx/smoke/build/api_document/get_element.js'


def test_run_script():
    logging.info("Testing the run_script method")
    builder = DocumentBuilder()

    # Assume 'script_path' is the path to a valid script for the test
    script_path, output_path = ScriptHelper().prepare_script(file_path)
    try:
        # Run the prepared script
        builder.build(script_path)
        logging.info("Script executed successfully")
    except RuntimeError as e:
        logging.error(f"Failed to execute script: {e}")
        pytest.fail(f"Script execution failed: {e}")
    assert os.path.isfile(output_path) == True


def test_run_unprepared_script():
    logging.info("Testing the run_script method with an unprepared script")
    builder = DocumentBuilder()

    # Assume 'script_path' is the path to a valid script for the test
    with pytest.raises(RuntimeError):
        builder.build(file_path)
        logging.info("Correctly caught failure for unprepared script")
