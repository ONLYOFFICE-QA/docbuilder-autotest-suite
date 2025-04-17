import os
import re
import tempfile
from argparse import ArgumentError

from lib.config import TMP_FOLDER


class ScriptHelper:

    def prepare_script(self, script_path: str, open_file: str = None) -> (str, str):
        """Prepare script to run.
        :param script_path: Path to the script file.
        :param open_file: Path to the document for OpenFile instruction
        :return str, str: Prepared script file path and output file path.
        """
        # Make sure the script path exists
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script file not found at: {script_path}")

        # Get the script name without extension for the output filename
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        temp_name = self.__get_tempfile_name(script_name)
        file_extension = self.__get_extension(script_path)
        script_file = f'{temp_name}.docbuilder'
        output_file = f'{temp_name}.{file_extension}'

        with open(script_path, 'r') as file:
            lines = file.readlines()
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        if open_file:
            lines.insert(0, f'builder.OpenFile("{open_file}");\n')
        else:
            lines.insert(0, f'builder.CreateFile("{file_extension}");\n')
            lines.append(f'builder.SaveFile("{file_extension}", "{output_file}.{file_extension}");\n')
        lines.append('builder.CloseFile();\n')

        # Create a temporary file with the modified content
        with open(script_file, 'w') as file:
            file.writelines(lines)

        return script_file, output_file

    @staticmethod
    def __get_extension(script_path) -> str:
        """Define file extension by its path
        :param script_path: Path to the script file.
        :return str: Document extension
        """
        extensions = {
            'Word': 'docx',
            'Cell': 'xlsx',
            'Slide': 'pptx',
            'Form': 'pdf',
        }
        result = re.search(
            r"[\\/](docx|xlsx|pptx|pdf|Word|Cell|Slide|Form)[\\/]",
            script_path,
        )
        if result:
            doc_type = result.group(1)
            if doc_type in extensions.keys():
                return extensions[doc_type]
            else:
                return doc_type
        else:
            raise ArgumentError(script_path, 'Cannot find doctype in script path')

    @staticmethod
    def __get_tempfile_name(prefix: str) -> str:
        return tempfile.mktemp(prefix=f'{prefix}_', dir=TMP_FOLDER)
