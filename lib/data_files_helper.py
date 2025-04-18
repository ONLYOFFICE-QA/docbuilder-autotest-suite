import os
from pathlib import Path
from lib import ROOT_DIR


class DataFilesHelper:

    @staticmethod
    def get_test_files(directory: str) -> list[str]:
        all_files = []
        for root, _, files in os.walk(os.path.join(ROOT_DIR, os.path.normpath(directory))):
            for file in files:
                if os.path.splitext(file)[-1] == '.js':
                    all_files.append(os.path.join(root, file))
        return all_files

    @staticmethod
    def get_checker_path(template_path: str) -> str:
        script_path = list(Path(template_path).parts)
        if 'templates' not in script_path:
            raise ValueError("part 'templates' was not found in script path")
        script_path[script_path.index('templates')] = 'checkers'
        return str(Path(*script_path))
