from lib.static_data import DOCUMENT_BUILDER
import subprocess
import os


class DocumentBuilder:
    def __init__(self, bin_path=DOCUMENT_BUILDER):
        if not os.path.isfile(bin_path):
            raise FileNotFoundError(f"DocumentBuilder binary not found at: {bin_path}")
        self.bin_path = bin_path

    def run_script(self, script_path: str):
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
