import os
import pytest

DOCUMENTATION_EXAMPLES = os.path.abspath('..\\developer_tools\\office-js-api\\Examples')


def get_test_files():
    all_files = []
    for folder in ['Word', 'Cell', 'Slide', 'Forms']:
        for root, _, files in os.walk(os.path.join(DOCUMENTATION_EXAMPLES, folder)):
            for file in files:
                if os.path.splitext(file)[-1] == '.js':
                    all_files.append(os.path.join(root, file))
    return all_files


@pytest.mark.parametrize(
    'file_path',
    get_test_files(),
)
def test_office_js_api_scripts(builder, file_path: str):
    script_path, output_path = builder.script_helper.prepare_script(file_path)
    result = builder.docbuilder.run_script(script_path)
    assert result['code'] == 0, result['stderr']
