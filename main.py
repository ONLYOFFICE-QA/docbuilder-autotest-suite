#!/usr/bin/env python3
from lib.document_builder import DocumentBuilder
from lib.script_js import ScriptJS
import os

# Initialize the script wrapper and document builder
script_wrapper = ScriptJS()
builder = DocumentBuilder()

# Path to the JavaScript script
script_path = "office-js-api/Examples/Word/Api/Methods/AddComment.js"

# Get the script name without extension for the output filename
script_name = os.path.splitext(os.path.basename(script_path))[0]

# Prepare the script (check if it needs 'builder.CreateFile("docx");' added)
prepared_script_path = script_wrapper.prepare_script(script_path)

try:
    # Run the prepared script
    builder.run_script(prepared_script_path)
    print(f"Script {script_name} executed successfully")
finally:
    # Clean up any temporary files
    script_wrapper.cleanup()
