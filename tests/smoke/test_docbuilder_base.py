import os
import pytest
from lib.docbuilder import DocumentBuilder
from lib.data_files_helper import DataFilesHelper


@pytest.mark.parametrize(
    'template_path',
    DataFilesHelper.get_test_files('scripts/smoke/templates'),
)
def test_docbuilder_base(builder, template_path: str) -> None:
    prepared_script_path, output_path = builder.script_helper.prepare_script(template_path)
    result = builder.build(prepared_script_path)
    assert result['code'] == 0, result['stderr']
    assert result['stdout'] == '', 'STDOUT is not empty'
    assert os.path.exists(output_path) == True, 'Office file was not created'

    checker_path = DataFilesHelper.get_checker_path(template_path)
    prepared_script_path, _ = builder.script_helper.prepare_script(checker_path, output_path)
    result = DocumentBuilder().run_script(prepared_script_path)
    assert result['code'] == 0, result['stderr']
    assert result['stdout'] == '', result['stdout']
