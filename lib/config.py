import os
from platform import system
from config import ROOT_DIR

BUILDER_PLATFORM = 'DESKTOP'

DOCBUILDER_PATH = '/opt/onlyoffice/documentbuilder/docbuilder' if system() == 'Linux' \
    else os.path.join(ROOT_DIR, '..\\DocumentBuilder\\docbuilder.exe')
DOCSERVER_URL = 'https://doc-linux.teamlab.info'
