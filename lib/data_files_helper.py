import os


class DataFilesHelper:

    @staticmethod
    def get_test_files(root: str) -> list[str]:
        all_files = []
        for root, _, files in os.walk(root):
            for file in files:
                if os.path.splitext(file)[-1] == '.js':
                    all_files.append(os.path.join(root, file))
        return all_files
