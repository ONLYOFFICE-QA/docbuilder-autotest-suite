import os
from platform import system

BUILDER_PLATFORM = 'DESKTOP'

DOCBUILDER_PATH = '/opt/onlyoffice/documentbuilder/docbuilder' if system() == 'Linux' \
    else os.path.abspath('..\\DocumentBuilder\\docbuilder.exe')
DOCSERVER_URL = 'https://doc-linux.teamlab.info'

TMP_FOLDER = os.path.abspath(os.path.dirname(__file__) + '/../tmp')
