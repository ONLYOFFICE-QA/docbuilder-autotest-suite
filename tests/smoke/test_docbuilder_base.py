import os
import pytest
from lib.docbuilder import DocumentBuilder
from lib.data_files_helper import DataFilesHelper

SMOKES_PATH = os.path.abspath('scripts/smoke/templates')


@pytest.mark.parametrize(
    'file_path',
    DataFilesHelper.get_test_files(SMOKES_PATH),
)
def test_docbuilder_base(builder, file_path: str):
    script_path, output_path = builder.script_helper.prepare_script(file_path)
    result = builder.build(script_path)
    assert result['code'] == 0, result['stderr']

    script_path = file_path.replace('\\templates\\', '\\checkers\\')
    script_path, _ = builder.script_helper.prepare_script(script_path, output_path)
    result = DocumentBuilder().run_script(script_path)
    assert result['code'] == 0, result['stderr']
    assert result['stdout'] == '', result['stdout']
