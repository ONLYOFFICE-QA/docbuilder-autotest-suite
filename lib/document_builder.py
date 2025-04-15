import logging
import os
import pytest
import subprocess

from lib.script_js import ScriptJS
from lib.static_data import DOCUMENT_BUILDER


class DocumentBuilder:
    def __init__(self, bin_path: str = DOCUMENT_BUILDER) -> None:
        if not os.path.isfile(bin_path):
            raise FileNotFoundError(f"DocumentBuilder binary not found at: {bin_path}")
        self.bin_path = bin_path

        self.script_wrapper = ScriptJS()

    def build(self, script_path: str) -> str:
        # Prepare the script before running it
        script_path, result_path = self.script_wrapper.prepare_script(script_path)
        try:
            self._run_script(script_path)
            logging.info("Script executed successfully")
            return result_path
        except RuntimeError as e:
            logging.error(f"Failed to execute script: {e}")
            pytest.fail(f"Script execution failed: {e}")
        # finally:
            # Clean up any temporary files
            # self.script_wrapper.cleanup()

    def _run_script(self, script_path: str) -> None:
        """
        Run DocumentBuilder with a JavaScript script file.

        Args:
            script_path (str): Path to JavaScript script file.
        """
        cmd = [
            self.bin_path,
            script_path
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(
                f"DocumentBuilder failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            )

        print(f"Script executed successfully: {script_path}")
