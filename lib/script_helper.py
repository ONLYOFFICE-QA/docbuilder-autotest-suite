import os
import re
import tempfile
from config import TMP_FOLDER


class ScriptHelper:

    def prepare_create_script(self, script_path: str) -> (str, str):
        """Prepare script with instruction CreateFile to run
        :param script_path: Path to the script file
        :return str, str: Prepared script file path and output file path
        """
        # Make sure the script path exists
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script file not found at: {script_path}")

        script_file, output_file = self.__get_tmp_files(script_path)
        file_extension = self.__get_extension(script_path)
        output_file += f'.{file_extension}'

        script_body = self.__read_script_body(script_path)
        lines = [script_body]

        if not self.__script_contains_close_commands(script_body):
            lines.append(f'builder.SaveFile("{file_extension}", "{output_file}");\n')
            lines.append('builder.CloseFile();\n')
        else:
            match = re.search(
                r'builder\.SaveFile\(["\'][^"]*["\'],\s*["\'][^"]*["\']\)\W*\n',
                script_body,
            )
            if not match:
                raise ValueError('Instruction SaveFile not found in script body')
            script_body = script_body.replace(
                match.group(),
                f'builder.SaveFile("{file_extension}", "{output_file}");\n',
            )
            lines[0] = script_body

        if not self.__script_contains_create_commands(script_body):
            lines.insert(0, f'builder.CreateFile("{file_extension}");\n')

        # Create a temporary file with the modified content
        with open(script_file, 'w') as file:
            file.writelines(lines)

        return script_file, output_file

    def prepare_open_script(self, script_path: str, open_file: str) -> (str, str):
        """Prepare script with instruction OpenFile to run
        :param script_path: Path to the script file
        :param open_file: Path to the opened document
        :return str, str: Prepared script file path and output file path
        """
        # Make sure the script and document paths exist
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script file not found at: {script_path}")
        if not os.path.isfile(open_file):
            raise FileNotFoundError(f"Opened document not found at: {script_path}")

        script_file, output_file = self.__get_tmp_files(script_path)
        file_extension = self.__get_extension(script_path)
        output_file += f'.{file_extension}'

        script_body = self.__read_script_body(script_path)
        lines = [script_body]

        if not self.__script_contains_create_commands(script_body):
            lines.insert(0, f'builder.OpenFile("{open_file}");\n')
        else:
            match = re.search(r'builder\.OpenFile\(["\'][^"]*["\']\)\W*\n', script_body)
            if not match:
                raise ValueError('Instruction OpenFile not found in script body')
            script_body = script_body.replace(match.group(), f'builder.OpenFile("{open_file}");\n')
            lines[0] = script_body

        if not self.__script_contains_close_commands(script_body):
            # lines.append(f'builder.SaveFile("{file_extension}", "{output_file}");\n')
            lines.append('builder.CloseFile();\n')

        # Create a temporary file with the modified content
        with open(script_file, 'w') as file:
            file.writelines(lines)

        return script_file, output_file

    @staticmethod
    def __read_script_body(script_path: str) -> str:
        with open(script_path, 'r') as file:
            script_body = file.read()
        if not script_body.endswith('\n'):
            script_body += '\n'
        return script_body

    @staticmethod
    def __script_contains_create_commands(script_body: str) -> bool:
         return any(item in script_body for item in ('builder.CreateFile', 'builder.OpenFile'))

    @staticmethod
    def __script_contains_close_commands(script_body: str) -> bool:
        return any(item in script_body for item in('builder.SaveFile', 'builder.CloseFile'))

    @staticmethod
    def __get_extension(script_path: str) -> str:
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
            raise ValueError('Cannot find doctype in script path')

    @staticmethod
    def __get_tempfile_name(prefix: str) -> str:
        return tempfile.mktemp(prefix=f'{prefix}_', dir=TMP_FOLDER)

    def __get_tmp_files(self, script_path: str) -> (str, str):
        """Create tmp pathes for script and output file
        :param script_path: path to original script
        :return: path to script and document in temp folder
        """
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        temp_name = self.__get_tempfile_name(script_name)
        script_file = f'{temp_name}.docbuilder'
        output_file = f'{temp_name}'
        return script_file, output_file
