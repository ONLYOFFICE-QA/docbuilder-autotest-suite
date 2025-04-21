import os
from pathlib import Path


class DataFilesHelper:

    @staticmethod
    def get_test_files(directory: str) -> list[str]:
        """Create list of data scripts
        :param directory: abs path to root scripts directory
        :return: list of scripts paths
        """
        # Make sure the directory is existing
        if not os.path.exists(directory):
            raise FileNotFoundError(f'Folder not found: {directory}')
        all_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[-1] == '.js':
                    all_files.append(os.path.join(root, file))
        return all_files

    @staticmethod
    def get_checker_path(template_path: str) -> str:
        script_path = list(Path(template_path).parts)
        if 'templates' not in script_path:
            raise ValueError("part 'templates' not found in script path")
        script_path[script_path.index('templates')] = 'checkers'
        return str(Path(*script_path))
