import logging
import os.path

import pytest
from lib.document_builder import DocumentBuilder
from lib.script_js import ScriptJS
from lib.static_data import DOCUMENTATION_EXAMPLES


def test_run_script():
    logging.info("Testing the run_script method")
    builder = DocumentBuilder()
    script_wrapper = ScriptJS()

    # Assume 'script_path' is the path to a valid JavaScript script for the test
    script_path = os.path.join(DOCUMENTATION_EXAMPLES, "Word/Api/Methods/AddComment.js")
    
    try:
        # Prepare the script before running it
        prepared_script_path, _ = script_wrapper.prepare_script(script_path)
        
        # Run the prepared script
        builder._run_script(prepared_script_path)
        logging.info("Script executed successfully")
    except RuntimeError as e:
        logging.error(f"Failed to execute script: {e}")
        pytest.fail(f"Script execution failed: {e}")
    finally:
        # Clean up any temporary files
        script_wrapper.cleanup()


def test_run_unprepared_script():
    logging.info("Testing the run_script method with an unprepared script")
    builder = DocumentBuilder()

    # Assume 'script_path' is the path to a valid JavaScript script for the test
    script_path = os.path.join(DOCUMENTATION_EXAMPLES, "Word/Api/Methods/AddComment.js")

    with pytest.raises(RuntimeError):
        builder._run_script(script_path)
        logging.info("Correctly caught failure for unprepared script")
