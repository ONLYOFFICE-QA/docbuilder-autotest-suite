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
        popen = subprocess.Popen(
            self.docbuilder_path + " \"" + file_path + "\"",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        result = {'returncode': 0, 'stdout': '', 'stderr': ''}
        try:
            stdout, stderr = popen.communicate()
            popen.wait()
            result['stdout'] = stdout.strip().decode('utf-8', errors='ignore')
            result['stderr'] = stderr.strip().decode('utf-8', errors='ignore')
            result['returncode'] = popen.returncode
        finally:
            popen.stdout.close()
            popen.stderr.close()
        return result
