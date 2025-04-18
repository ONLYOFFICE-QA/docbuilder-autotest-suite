import os
from pathlib import Path


class DataFilesHelper:

    @staticmethod
    def get_test_files(root: str) -> list[str]:
        all_files = []
        for root, _, files in os.walk(root):
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
