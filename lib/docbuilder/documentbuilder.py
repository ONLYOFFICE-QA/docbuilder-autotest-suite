import os
import subprocess
from lib.config import DOCBUILDER_PATH


class DocumentBuilder:
    def __init__(self, bin_path: str = None) -> None:
        if bin_path and not os.path.isfile(bin_path):
            raise FileNotFoundError(f'DocumentBuilder binary not found at: {bin_path}')
        self.docbuilder_path = bin_path or self.default_path

    @property
    def default_path(self) -> str:
        return DOCBUILDER_PATH

    def run_script(self, file_path: str) -> dict:
        """Run DocumentBuilder with a script file.
        file_path: Path to script file.
        """
        cmd = [
            self.docbuilder_path,
            file_path,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {'code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
