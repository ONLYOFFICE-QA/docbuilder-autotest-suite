import logging
from lib.document_builder import DocumentBuilder
from lib.script_js import ScriptJS
import pytest

def test_run_script():
    logging.info("Testing the run_script method")
    builder = DocumentBuilder()
    script_wrapper = ScriptJS()
    
    # Assume 'script_path' is the path to a valid JavaScript script for the test
    script_path = "office-js-api/Examples/Word/Api/Methods/AddComment.js"
    
    try:
        # Prepare the script before running it
        prepared_script_path = script_wrapper.prepare_script(script_path)
        
        # Run the prepared script
        builder.run_script(prepared_script_path)
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
    script_path = "office-js-api/Examples/Word/Api/Methods/AddComment.js"

    with pytest.raises(RuntimeError):
        builder.run_script(script_path)
        logging.info("Correctly caught failure for unprepared script")
