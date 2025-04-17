import os
import pytest

SMOKES_PATH = os.path.abspath('scripts/smoke/build')

def get_test_files():
    all_files = []
    for root, _, files in os.walk(SMOKES_PATH):
        for file in files:
            if os.path.splitext(file)[-1] == '.js':
                all_files.append(os.path.join(root, file))
    return all_files


@pytest.mark.parametrize(
    'file_path',
    get_test_files(),
)
def test_docbuilder_base(builder, file_path: str):
    script_path, output_path = builder.script_helper.prepare_script(file_path)
    result = builder.docbuilder.run_script(script_path)
    assert result['code'] == 0, result['stderr']

    script_path = file_path.replace('\\build\\', '\\check\\')
    script_path, _ = builder.script_helper.prepare_script(script_path, output_path)
    result = builder.docbuilder.run_script(script_path)
    assert result['code'] == 0, result['stderr']
    assert result['stdout'] == '', result['stdout']
