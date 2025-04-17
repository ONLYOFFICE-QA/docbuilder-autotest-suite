import re

from lib.docbuilder import DocumentBuilder, DocumentServer
from lib.script_helper import ScriptHelper
from lib.config import BUILDER_PLATFORM


class DocBuilderWrapper:

    def __init__(self):
        if BUILDER_PLATFORM == 'WEB':
            self.__docbuilder = DocumentServer()
        else:
            self.__docbuilder = DocumentBuilder()
        self.script_helper = ScriptHelper()

    def build(self, script_path):
        return self.__docbuilder.run_script(script_path)
