import os
import pytest
from lib.data_files_helper import DataFilesHelper

@pytest.mark.parametrize(
    'file_path',
    [
        path for folder in ['Word', 'Cell', 'Slide', 'Forms']
        for path in DataFilesHelper.get_test_files(os.path.join('office-js-api/Examples', folder))
    ],
)
def test_office_js_api_scripts(builder, file_path: str):
    script_path, output_path = builder.script_helper.prepare_script(file_path)
    result = builder.build(script_path)
    assert result['code'] == 0, f"script_path: {file_path}\nstdout: {result['stdout']}\nstderr: {result['stderr']}"
    assert os.path.exists(output_path) == True, 'Office file was not created'
