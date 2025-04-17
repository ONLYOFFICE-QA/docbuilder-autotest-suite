import os
import pytest
from lib.data_files_helper import DataFilesHelper

DOCUMENTATION_EXAMPLES = os.path.abspath('..\\developer_tools\\office-js-api\\Examples')


@pytest.mark.parametrize(
    'file_path',
    [
        path for folder in ['Word', 'Cell', 'Slide', 'Forms']
        for path in DataFilesHelper.get_test_files(os.path.join(DOCUMENTATION_EXAMPLES, folder))
    ],
)
def test_office_js_api_scripts(builder, file_path: str):
    script_path, output_path = builder.script_helper.prepare_script(file_path)
    result = builder.build(script_path)
    assert result['code'] == 0, f"script_path: {file_path}\nstdout: {result['stdout']}\nstderr: {result['stderr']}"
