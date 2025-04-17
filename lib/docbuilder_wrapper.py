import re

from lib.docbuilder import DocumentBuilder, DocumentServer
from lib.script_helper import ScriptHelper
from lib.config import BUILDER_PLATFORM


class DocBuilderWrapper:

    def __init__(self):
        if BUILDER_PLATFORM == 'WEB':
            self.docbuilder = DocumentServer()
        else:
            self.docbuilder = DocumentBuilder()
        self.script_helper = ScriptHelper()
